def format_weather(data):
    if data is None:
        return "City not found!"

    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    desc = data["weather"][0]["description"]

    return (
        f"Weather Report for {city}\n"
        f"--------------------------------\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind} m/s\n"
        f"Condition: {desc.capitalize()}\n"
    )
