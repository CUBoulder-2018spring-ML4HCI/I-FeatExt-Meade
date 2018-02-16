"""
A utility to send OSC messages using pythonosc.
"""

from pythonosc import osc_message_builder
from pythonosc import udp_client
import argparse

class OSCRunner:
    ip = ""
    port = 0
    output = ""

    def __init__(self, _ip, _port, _output):
        self.ip = _ip
        self.port = _port
        self.output = _output

    def instantiate_udp(self):
        self.client = udp_client.SimpleUDPClient(self.ip, self.port)

    def send_message(self, message):
        self.client.send_message(self.output, message)
        print("Sent message '" + str(message) + "' to " + self.ip + ":" + str(self.port))