class Employee:

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		
	def displayEmployee(self):
		print "Name : ", self.name, ", Salary : ", self.salary


if __name__=="__main__":
	emp1 = Employee('Dipesh', 19000)
	emp1.displayEmployee()

