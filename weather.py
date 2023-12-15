import requests
from bs4 import BeautifulSoup

def get_weather(location):
    try:
        url = f"https://wttr.in/{location}?format=%t+%h+%c"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        if response.status_code == 200:
            return soup.get_text()
        else:
            print(f"Error: Unable to fetch weather data. {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data}")
    else:
        print("Unable to fetch weather data.")

def main():
    location = input("Enter a city name or location: ")
    
    weather_data = get_weather(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
