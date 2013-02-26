#!/usr/bin/python

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect('tcp://127.0.0.1:5000')
socket.send("Hello World!")