import json
import socket
import os

# maybe use async instead?
import threading

# make a config if it doesn't already exist
if(not os.path.isfile("./config.json")):
    import setup
    print("Configure the config file, then run again.")
    quit()

# load json config
with open("./config.json", "r") as file:
    config = json.load(file)

class handler:

    def __init__(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind(("0.0.0.0", int(config["port"])))
        self.listener.listen()
        self.conn, self.addr = self.listener.accept()
        print('Connected by', self.addr)

    def __del__(self):
        self.listener.close()

    def process_input(self):
        while True:
            data = self.conn.recv(1024).decode("UTF-8","ignore")
            print(data)


def main():
    c = handler()
    c.process_input()
main()
