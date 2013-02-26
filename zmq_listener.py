#!/usr/bin/python

import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:5000")

while True:
  msg = socket.recv()
  print "Received %s" % msg