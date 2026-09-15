#!/usr/bin/env python

class Cable:
	def __init__(self):
		self.name = 'cable'
		self.connections = 2
		self.buffer = ''
		self.available = True

	def read_buffer(self):
		self.available = True
		return self.buffer

	def write_buffer(self, frame):
		if not self.available:
			raise ColisionError
		else:
			self.buffer = frame
			self.available = False

	def is_available(self):
		return self.available

	def connect(self):
		if self.connections > 0:
			self.connections -= 1
		else:
			raise NoConnectorsAvailable
	
	def disconnect(self):
		if self.connections < 2:
			self.connections += 1

class ColisionError(Exception):
	pass

class NoConnectorsAvailable(Exception):
	pass
