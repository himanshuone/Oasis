import tkinter as tk
from statistics import mean, stdev
from datetime import date


def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    category = ["Underweight", "Normal", "Overweight", "Obese Class I", "Obese Class II", "Obese Class III"]
    bmi_range = [(0, 18.5), (18.5, 24.9), (25, 29.9), (30, 34.9), (35, 39.9), ("over 40")]
    for i, range in enumerate(bmi_range):
        if bmi >= range[0] and bmi <= range[1]:
            return bmi, category[i]
    return bmi, "Invalid"

users = {}  
def save_data(name, weight, height, date):
    users[name] = users.get(name, []) + [(weight, height, date)]

def get_history(name):
    return users.get(name, [])

import matplotlib.pyplot as plt

def plot_bmi_history(name):
    history = get_history(name)
    dates, bmis = zip(*history)
    plt.figure(figsize=(8, 5))
    plt.plot(dates, bmis, marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.title(f"{name}'s BMI History")
    plt.grid(True)
    plt.show()

root = tk.Tk()
root.title("BMI Calculator")

lbl_name = tk.Label(root, text="Name:")
lbl_name.grid(row=0, column=0)
ent_name = tk.Entry(root)
ent_name.grid(row=0, column=1)

lbl_weight = tk.Label(root, text="Weight (kg):")
lbl_weight.grid(row=1, column=0)
ent_weight = tk.Entry(root)
ent_weight.grid(row=1, column=1)

lbl_height = tk.Label(root, text="Height (m):")
lbl_height.grid(row=2, column=0)
ent_height = tk.Entry(root)
ent_height.grid(row=2, column=1)

btn_calculate = tk.Button(root, text="Calculate", command=lambda: calculate())
btn_calculate.grid(row=3, column=0, columnspan=2)

lbl_result = tk.Label(root, text="BMI and Category:", font=("Arial", 12))
lbl_result.grid(row=4, column=0, columnspan=2)

btn_save = tk.Button(root, text="Save Data")
btn_save.grid(row=5, column=0)

btn_history = tk.Button(root, text="View History", command=lambda: plot_bmi_history(ent_name.get()))
btn_history.grid(row=5, column=1)

def calculate():
    try:
        weight = float(ent_weight.get())
        height = float(ent_height.get())

        bmi, category = calculate_bmi(weight, height)
        result_text = f"BMI: {bmi:.2f} ({category})"
        lbl_result.config(text=result_text)

        save_data(ent_name.get(), weight, height, date.today())

    except ValueError:
        lbl_result.config(text="Invalid input! Please enter numbers.")

root.mainloop()
