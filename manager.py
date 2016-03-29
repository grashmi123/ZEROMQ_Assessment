import zmq
import time

#push
context = zmq.Context()
socket = context.socket(zmq.PUSH)

socket.bind("tcp://127.0.0.1:5555")


for x in range(20):
    msg = str(x) + " , " + str(time.time())
    print x
    socket.send(msg)
    time.sleep(1) 
