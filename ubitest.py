from ubidots import ApiClient
import random
import time

# Create an ApiClient object

api = ApiClient(token='wseZ3mpbc7vPzM4tlANdLo5Tqngf48')

# Get a Ubidots Variable

try:
    variable1 = api.get_variable("581b254f76254250326a2d51")
    variable2 = api.get_variable("581b2f797625420481362aac")
    variable3 = api.get_variable("581b2f887625420434ecd29c")
    variable4 = api.get_variable("581b2f957625420481362b11")
    variable5 = api.get_variable("581b2f9f762542045e7a598c")
    variable6 = api.get_variable("581b25f676254253526c72c1")
    variable7 = api.get_variable("581b2f5f7625420318a83176")
except ValueError:
    print"It is not possible to obtain the variable"

while(1):
    try:

        # We'll just send a random value as an example.
        # Please replace this value with the sensor reading
        # you'd like to send from your device.
        value1 = random.randint(18,28)
        # We'll just send a random value as an example.
        # Please replace this value with the sensor reading
        # you'd like to send from your device.
        value2 = random.randint(50, 80)
        # We'll just send a random value as an example.
        # Please replace this value with the sensor reading
        # you'd like to send from your device.
        value3 = random.randint(3, 6)
        # We'll just send a random value as an example.
        # Please replace this value with the sensor reading
        # you'd like to send from your device.
        value4 = random.randint(1, 3)
        # We'll just send a random value as an example.
        # Please replace this value with the sensor reading
        # you'd like to send from your device.
        value5 = value3*value4;
	value6 = random.randint(1, 90)
	value7 = random.randint(1, 180)
        variable1.save_value({'value': value1})
        variable2.save_value({'value': value2})
        variable3.save_value({'value': value3})
        variable4.save_value({'value': value4})
        variable5.save_value({'value': value5})

        print "Value sent"
        time.sleep(1)
    except ValueError:
        print "Value not sent"
