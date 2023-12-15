import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QTextCursor
import os

class ChatClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        self.send_message(f"JOIN {self.username}")

    def send_message(self, message):
        self.socket.sendall(message.encode())

    def receive_messages(self):
        while True:
            message = self.socket.recv(1024).decode()
            if message.startswith("FILE"):
                self.receive_file(message[5:])
            else:
                self.ui.update_chat(message)

    def send_file(self, file_path):
        filename = os.path.basename(file_path)
        self.send_message(f"FILE {filename}")
        with open(file_path, "rb") as file:
            file_data = file.read(1024)
            while file_data:
                self.socket.sendall(file_data)
                file_data = file.read(1024)

    def receive_file(self, filename):
        file_path = os.path.join("downloads", filename)
        with open(file_path, "wb") as file:
            file_data = self.socket.recv(1024)
            while file_data:
                file.write(file_data)
                file_data = self.socket.recv(1024)
        self.ui.update_chat(f"Received file: {filename}")

class ChatUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat Application")
        self.setGeometry(100, 100, 800, 600)

        self.chat_history = QTextBrowser()
        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_file_button = QPushButton("Send File")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.chat_history)
        self.layout.addWidget(self.message_input)
        self.layout.addWidget(self.send_button)
        self.layout.addWidget(self.send_file_button)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.client = None

        self.send_button.clicked.connect(self.send_message)
        self.send_file_button.clicked.connect(self.send_file)

    def init_client(self, host, port, username):
        self.client = ChatClient(host, port, username)
        self.client.ui = self
        self.client.connect()
        threading.Thread(target=self.client.receive_messages, daemon=True).start()

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.client.send_message(message)
            self.message_input.clear()

    def send_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Send File", "", "All Files (*)")
        if file_path:
            self.client.send_file(file_path)

    def update_chat(self, message):
        self.chat_history.append(message)
        self.chat_history.moveCursor(QTextCursor.End)

def main():
    app = QApplication(sys.argv)
    window = ChatUI()

    # Set the host, port, and username
    host = "127.0.0.1"
    port = 5555
    username = "YourUsername"

    window.init_client(host, port, username)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
