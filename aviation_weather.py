import time
import datetime
import math

# Define constants
SENSOR_READ_INTERVAL = 150  # 2 minutes and 30 seconds
MESSAGE_UPDATE_INTERVAL = 180  # 3 minutes
LATITUDE = 00.00000
LONGITUDE = 00.00000
ELEVATION = 1097.3

# Define sensor readings
def read_sensors():
    current_time = datetime.datetime.utcnow().strftime('%H:%M')
    # Simulated sensor data, replace with actual sensor readings
    wind_direction_degrees = 180
    wind_speed_knots = 5
    visibility_miles = 2.5
    sky_condition = "Scattered"
    cloud_base_agl = 2000
    temperature_celsius = 20
    dewpoint_celsius = 15
    altimeter_inches_mercury = 29.92

    return current_time, wind_direction_degrees, wind_speed_knots, visibility_miles, sky_condition, cloud_base_agl, temperature_celsius, dewpoint_celsius, altimeter_inches_mercury

# Define functions to convert wind direction to cardinal direction
def degrees_to_cardinal(d):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = round(d / (360. / len(dirs)))
    return dirs[ix % len(dirs)]

# Define function to round visibility to nearest 1/4 statute mile
def round_visibility(visibility):
    return math.floor(visibility * 4) / 4

# Define function to generate verbal weather message
def generate_weather_message(sensor_data):
    current_time, wind_direction_degrees, wind_speed_knots, visibility_miles, sky_condition, cloud_base_agl, temperature_celsius, dewpoint_celsius, altimeter_inches_mercury = sensor_data
    
    # Convert wind direction to cardinal direction
    if wind_speed_knots < 3:
        wind_message = "Winds calm."
    else:
        wind_message = f"Winds {degrees_to_cardinal(wind_direction_degrees)} at {wind_speed_knots} knots."

    # Round visibility to nearest 1/4 statute mile
    visibility_message = round_visibility(visibility_miles)
    if visibility_message > 10:
        visibility_message = 10

    # Generate sky condition message
    sky_condition_message = f"Sky condition {sky_condition}."
    if cloud_base_agl:
        sky_condition_message += f" Cloud base {cloud_base_agl} feet AGL."

    # Generate verbal weather message
    message = f"DBQ County Remote Weather Automated Weather Observation. Time {current_time} zulu. {wind_message} Visibility {visibility_message} miles. {sky_condition_message} Temperature {temperature_celsius} Celsius. Dewpoint {dewpoint_celsius} Celsius. Altimeter {altimeter_inches_mercury} inches of mercury."

    return message

# Main function
def main():
    print("Starting Aviation Weather Machine and AWOS System...")
    print("Press Ctrl+C to exit.")

    last_message_time = 0
    while True:
        try:
            current_time = time.time()

            # Check if it's time to read sensors and update message
            if current_time - last_message_time >= MESSAGE_UPDATE_INTERVAL:
                last_message_time = current_time
                
                # Read sensor data
                sensor_data = read_sensors()

                # Generate verbal weather message
                weather_message = generate_weather_message(sensor_data)

                # Output verbal weather message
                print(weather_message)

                # Output remarks
                print("Remarks... Remote Weather Observation updated every 3 minutes. This Observation is not for any airport. For Dubuque A.T.I.S, contact One Two Seven Decimal Two Five megahertz.")

            time.sleep(SENSOR_READ_INTERVAL)

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
