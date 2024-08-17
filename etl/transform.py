def transform_weather_data(raw_data):
    transformed_data = []
    for entry in raw_data:
        transformed_entry = {
            "city": entry["name"],
            "temperature": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "weather": entry["weather"][0]["description"],
            "timestamp": entry["dt"],
        }
        transformed_data.append(transformed_entry)
    return transformed_data
