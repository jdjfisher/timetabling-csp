import module
#Class for storing a tutor object, tracks their name, and expertise
#Expertise is a list of strings
#name is a string
class Tutor:

	def __init__(self,name="", expertise=list()):
		self.name=name
		self.expertise=expertise

	#this is used during set up and should not be used in your solution
	def setName(self,name):
		self.name = name

	#this is used during set up and should not be used in your solution
	def setExpertise(self,expertise):
		self.expertise =expertise

	#this is used during set up and should not be used in your solution
	def addExpertise(self,expertise):
		self.expertise.add(expertise)

	def __str__(self):
		return str([self.name, self.expertise])

	def __repr__(self):
		return str(self)

	def __lt__(self, other):
		return False
