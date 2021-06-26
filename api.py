import socket
import json
import machine


class Rest:
    def __init__(self, chat, wlan):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chat = chat
        self.wlan = wlan

        try:
            self.main()
        except Exception as e:
            print(str(e))
            self.chat.send_message('Fan: Error occurred. Trying to do a reboot. ' + str(e))
            machine.reset()

    def process_connection(self, connection, _dict):
        connection.send('HTTP/1.1 200 OK\n')
        connection.send('Content-Type: application/json\n')
        connection.send('Connection: close\n\n')

        connection.sendall(json.dumps(_dict))
        connection.close()

    def main(self):
        self.s.bind(('', 80))
        self.s.listen(3)

        try:
            self.chat.send_message('Fan: Boot succeeded. Endpoint: ' + 'http://' + self.wlan.station.ifconfig()[0] + '?message=')
        except Exception as e:
            self.chat.send_message(str(e))

        while True:
            connection, address = self.s.accept()
            request = str(connection.recv(1024))

            path = request.split(' ')[1] + ' '
            query = path[2:-1]
            arguments = query.split('=')
            message = {}

            if len(arguments) == 2:
                self.chat.send_message(arguments[1])
                message = {"message": arguments[1]}

            self.process_connection(connection, message)
