from api import get_weather
from utils import format_weather

def main():
    city = input("Enter city: ")
    data = get_weather(city)
    print(format_weather(data))

if __name__ == "__main__":
    main()
