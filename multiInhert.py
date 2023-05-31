class Printer:
	def print (self, context):
		print("\tscan() method from Printer class")
class Fax:
	def send(self, context):
		print("\tsend() method from Fax class")
	def print (self, context):
		print("\tprint() method from Fax class")

class Scanner:
	def scan(self, context):
		print("\tscan() method from Scanner class")

class MFD_SPF (Scanner, Printer, Fax):
    pass

class MFD_SFP (Scanner, Fax, Printer):
    pass

mfd_sfp = MFD_SFP()
mfd_sfp.scan("test")
mfd_sfp.print("test")
mfd_sfp.send("test")

mfp_spf = MFD_SPF()
mfp_spf.scan("test")
mfp_spf.print("test")
mfp_spf.send("test")