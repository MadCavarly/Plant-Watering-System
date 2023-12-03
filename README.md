# Smart Plant Watering System and Data Logger
## Team Members
- **Onur Tezgel** (Micropython Code and Documentation)
- **Kaan Bayraktar** (Circuit Design and Documentation)

## Theoretical description and explanation
The Smart Plant Watering System with Data Logging Feature is designed to provide an intelligent and automated solution for plant care. Using soil moisture sensors, humidity sensors, temperature sensors, a relay, and a Microcontroller Unit (MCU), the system aims to optimize the watering process based on real-time environmental conditions. Additionally, the project incorporates data logging capabilities for users to track and analyze the plant's environment over time, ensuring optimal growth conditions.

## Hardware description of demo application

### Soil Moisture Sensor:

<img src= "https://github.com/MadCavarly/Smart-Plant-Watering-System/assets/147071482/6b9351d7-f9d5-4eb1-8d23-2d2ba74eba97" width="450" height="350">

Utilized to measure the moisture content in the soil.

### Temperature and Humidity Sensor:
<img src= "https://github.com/MadCavarly/Smart-Plant-Watering-System/assets/147071482/d35677be-fb79-433a-96b1-bc8369ef481a" width="450" height="350">

Monitors the temperature of the soil and the humidity levels in the surrounding air.
Ensures that the plant is in an environment with an appropriate temperature and humidity range.

### Relay:
Controls the water supply based on the sensor readings.
Emulates activation or deactivation of the water pump or irrigation system.

### OLED Display
Real-time feedback on soil moisture, humidity and temperature displayed on the OLED.

### Microcontroller Unit (MCU):
Acts as the brain of the system, processing sensor data and making decisions.

## Software Description
### List of Used Packages

#### `main.py`: Main program responsible for coordinating various modules: soil moisture measurement, temperature and air humidity measurement, display management, relay control(watering), Wi-Fi connection, and data transmission to ThingSpeak.

#### `wifi_connection.py`: Handles the ESP32's Wi-Fi connectivity, providing functions to connect and disconnect from a network.

#### `thingspeak.py`: Enables communication with ThingSpeak, allowing data transmission to specified fields using the ThingSpeak API key. Includes functions to send sensor data to ThingSpeak.

#### `temperature_sensor.py`: Defines a class for the temperature sensor, utilizing I2C communication to read temperature and air humidity values.

#### `soil_moisture_sensor.py`: Implements a class for the soil moisture sensor, utilizing ADC to determine soil moisture percentage.

#### `relay.py`: Manages the relay module, enabling activation and deactivation of the relay pin based on specified conditions and duration.

#### `parameters.py`: Defines a class to calculate and manage various parameters related to soil moisture limits based on temperature and air humidity readings.

#### `oled_display.py`: Handles the OLED display functionality, initializing and controlling display content for showing soil moisture, temperature, and humidity readings.

## Instructions
### How to Use the Smart Plant Watering System

1. **Configure Wi-Fi Connection:**
   - Provide your Wi-Fi credentials in the program (`main.py`) to enable connectivity for data transmission.
  
2. **Set Up ThingSpeak:**
   - Configure the ThingSpeak API key within the program (`thingspeak.py`) to enable data transmission to ThingSpeak's specified fields.
   
3. **Adjust Sensor Parameters:**
   - Inside the `parameters.py` file, set the desired parameters for sensor checking times and limits for soil moisture, temperature, and humidity based on your plant's needs.
   
4. **Sensor Placement:**
   - Place the soil moisture sensor inside the ground near the plant but away from the watering system for accurate soil moisture readings.
   - Position the temperature sensor in a safe location, away from direct contact with water or the watering system, to monitor ambient temperature.
   
5. **Starting the Application:**
   - Once configurations and sensor placements are done, run the `main.py` application.
   
6. **Monitoring:**
   - The system will continuously monitor soil moisture, temperature, and humidity based on the configured parameters.
   - It will autonomously control the watering system to maintain optimal soil moisture levels.



