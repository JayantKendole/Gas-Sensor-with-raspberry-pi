import machine
import utime

# Define GPIO pins for the traffic light LEDs
RED_PIN = 0
GREEN_PIN = 1
YELLOW_PIN = 2

# Initialize GPIO pins for LEDs
red_led = machine.Pin(RED_PIN, machine.Pin.OUT)
yellow_led = machine.Pin(YELLOW_PIN, machine.Pin.OUT)
green_led = machine.Pin(GREEN_PIN, machine.Pin.OUT)

# Initialize an ADC object on GPIO pin 26.
mq2_AO = machine.ADC(26)

# Function to control the traffic light based on gas sensor reading
def control_traffic_light(gas_value):
    if gas_value > 14000:
        green_led.off()
        yellow_led.off()
        red_led.on()
    elif 12000 <= gas_value <= 14000:
        red_led.off()
        green_led.off()
        yellow_led.on()
    else:
        red_led.off()
        yellow_led.off()
        green_led.on()

# Continuously read and control traffic light based on sensor data
while True:
    gas_value = mq2_AO.read_u16()  # Read and convert analog value to 16-bit integer
    print("AO:", gas_value)  # Print the analog value
    control_traffic_light(gas_value)
    utime.sleep_ms(1000)  # Wait for 300 milliseconds before next reading and control
