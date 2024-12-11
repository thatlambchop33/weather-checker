import requests

def send_sms(message, phone_number, optus_api_key):
    sms_url = "https://api.optus.com.au/sms/v1/messages"
    headers = {
        "Authorization": f"Bearer {optus_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "to": phone_number,
        "message": message
    }
    #TESTING - My number to test SMS
    #data = {
    #    "to": "+6438422298,
    #    "message": message
    #}
    response = requests.post(sms_url, json=data, headers=headers)
    return response.status_code == 201

def is_weather_bad(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        return f"Error: {response.get('message', 'Invalid location')}", False

    weather = response['weather'][0]['main'].lower()
    temp = response['main']['temp']
    
    bad_weather_conditions = {'rain', 'snow', 'thunderstorm'}
    is_bad = weather in bad_weather_conditions or temp < 0 or temp > 35

    return f"Weather: {weather.title()}, Temp: {temp}°C", is_bad

if __name__ == "__main__":
    location = input("Enter location: ").strip()
    phone_number = input("Enter phone number: ").strip()
    api_key = "HIDDEN"
    optus_api_key = "HIDDEN"
    
    weather_info, is_bad = is_weather_bad(location, api_key)
    print(weather_info)
    
    if is_bad:
        print("The weather is bad.")
        if send_sms(f"Alert: {weather_info}", phone_number, optus_api_key):
            print("SMS sent successfully.")
        else:
            print("Failed to send SMS.")
    else:
        print("The weather is not bad.")
