import abc

class Scanner(abc.ABC):
	def scan_document(self, doc):
		print ("document {} was scanned".format(doc))
	@abc.abstractmethod
	def get_scanner_status(self):
		pass

class Printer(abc.ABC):
	def print_document(self, doc):
		print ("document {} was printed".format(doc))
	@abc.abstractmethod
	def get_printer_status(self):
		pass

class MFD1(Scanner, Printer):
	def get_scanner_status(self):
		return "a cheap scanner, device capabilities (resolution) should be low; "
	def get_printer_status(self):
		return "a cheap printer, device capabilities (resolution) should be low; "

mfd1 = MFD1()
mfd1.print_document("doc")
mfd1.scan_document("doc")
print(mfd1.get_printer_status())
print(mfd1.get_scanner_status())