
from nic import *

class Switch:
	def __init__(self, name=None, num_ports=24):
		self.num_ports = num_ports
		self.nic_array = []
		for nic in nic_array:
			nic = NIC()

class Hub:
	def __init__(self, name = None, num_ports=24):
		self.num_ports = num_ports
		self.nic_array = []
		for nic in nic_array:
			nic = NIC()


class Host:
	def __init__(self, name = None):
		self.name = name
		self.nic = NIC()

