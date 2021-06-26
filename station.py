import network

from lamp import Lamp

led = Lamp()


class Station:
    def __init__(self, ssid, password):
        self.password = password
        self.ssid = ssid
        self.station = ''

        self.connect()

    def connect(self):
        station = network.WLAN(network.STA_IF)
        station.active(True)

        station.disconnect()

        self.station = station

        if not station.isconnected():
            led.blink(1)
            station.connect(self.ssid, self.password)

            while not station.isconnected():
                pass

        led.blink(2)
