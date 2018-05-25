#from socketIO_client import SocketIO
#from time import sleep
#from datetime import datetime
from timeit import Timer
from socketIO_client import SocketIO, LoggingNamespace

 
socketIO = SocketIO('localhost', 3000)

def pleaseUpdate_cb(*args):
    #socketIO.emit('update_from_worker', "socket_client.py: finished update - %s" % (datetime.now(),))
    print('on_bbb_response', args)
    

def on_aaa_response(*args): #a tuple is returned
	print(args[0])
 

def get():
	socketIO.emit('message', {'client_message' : 'hello from the client-side'})
	socketIO.on('on_aaa_response', on_aaa_response)
	socketIO.wait(seconds=0.1)
	#while 1:
	#socketIO.wait_for_callbacks(seconds=3)
		#socketIO.wait()


if __name__=='__main__':
	t = Timer('get()', "from __main__ import get")
	#elapsed = (10 * t.timeit(number=1))
	#print("Function preload_resources() takes %0.3f microseconds/pass" % elapsed)
	print(str(t.timeit(number=1)))
