# Weather Checker with SMS Alert

## Overview

This Python script checks the weather for a specified location using the OpenWeatherMap API. If the weather is bad (rain, snow, thunderstorms, or extreme temperatures), it sends an SMS alert using the Optus SMS API.

## Features

- Fetches real-time weather data.
- Identifies bad weather conditions.
- Sends SMS alerts when bad weather is detected.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. Clone this repository.
2. Install the required Python package:
   ```bash
   pip install requests
   ```

## How to Use

1. Run the script:
   ```bash
   python check_weather_bad.py
   ```
2. Enter the following when prompted:
   - **Location:** City name (e.g., "Sydney")
   - **Phone Number:** A valid phone number for SMS alerts

## How It Works

1. The script fetches current weather data from OpenWeatherMap.
2. It evaluates the weather conditions:
   - Bad weather includes rain, snow, thunderstorms, temperatures below 0°C or above 35°C.
3. If bad weather is detected:
   - Displays a weather alert.
   - Sends an SMS notification to the provided phone number.

## Example Output
```
Enter location: Sydney
Enter phone number: +614XXXXXXXX
Weather: Rain, Temp: 18°C
The weather is bad.
SMS sent successfully.
```

## License
This project is open-source and available under the MIT License.

## Disclaimer
- Ensure that API keys are kept secure.
- SMS charges may apply based on your Optus API subscription plan.

## Contributions
Feel free to submit issues or pull requests to enhance the functionality.
