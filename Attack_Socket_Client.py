from socketIO_client import SocketIO, LoggingNamespace


 
socketIO = SocketIO('localhost', 3000)


'''def on_aaa_response(*args): #a tuple is returned
	for i in args:
		att_list.append(i)
	print(att_list)'''



class Att_Sock:
	def __init__(self):
		self.att_list = []
		self.proper_att_list = []

	def on_aaa_response(self, *args): #a string is returned
		self.att_list = args[0]


	def get_attack(self):
		socketIO.emit('message', {'client_message' : 'hello from the client-side'})
		socketIO.on('on_aaa_response', self.on_aaa_response)
		socketIO.wait(seconds=1)
		#return selfatt_list
