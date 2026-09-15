from mac import MAC

class NIC:
	def __init__(self, name=None, mac=None, cable=None):
		if not mac:
			self.mac = MAC()
		else:
			self.mac = mac
		
		self.name = name
		if cable:
			self.connectCable(cable)

	def connect_cable(self, cable):
		self.cable = cable
		self.cable.connect()

	def disconnect_cable(self):
		self.cable.disconnect()
		self.cable = None

	def send_frame(self, datagram):
		self.cable.writeBuffer(datagram)

	def recv_frame(self):
		return self.cable.readBuffer()
		
