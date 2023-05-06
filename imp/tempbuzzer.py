import RPi.GPIO as g
import dht11
import time

g.setmode(g.BOARD)
g.setup(7,g.OUT,initial=g.LOW)

def main():
    while 1:
        instance=dht11.DHT11(pin=12)
        result=instance.read()
        if result.is_valid():
            print("Temerature : ", result.temperature)
            print("Humidity:", result.humidity)
            if result.temperature>25:
                g.output(7,g.HIGH)
                print("Temperature reached above 24 C")
                time.sleep(0.2)
                g.output(7,g.LOW)
        time.sleep(2)
try:
    main()
except KeyboardInterrupt:
    pass
finally:
    g.cleanup()

