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

	def connectCable(self, cable):
		self.cable = cable
		self.cable.connect()

	def disconnectCable(self):
		self.cable.disconnect()
		self.cable = None

	def sendFrame(self, datagram):
		self.cable.writeBuffer(datagram)

	def recvFrame(self):
		return self.cable.readBuffer()
		
