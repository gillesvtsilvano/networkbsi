import random

class MAC:
	def __init__(self):
		self.mac = [ random.randint(0x00, 0xff),
				random.randint(0x00, 0xff),
				random.randint(0x00, 0xff),
				random.randint(0x00, 0xff),
				random.randint(0x00, 0xff),
				random.randint(0x00, 0xff) ]

	def generate(self):
		mac = [ random.randint(0x00, 0xff),
				random.randint(0x00, 0xff),
				random.randint(0x00, 0xff),
				random.randint(0x00, 0xff),
				random.randint(0x00, 0xff),
				random.randint(0x00, 0xff) ]

		return mac

	def __repr__(self):
		return(':'.join(map(lambda x: "%02x" % x, self.mac)))


