class student:
	def __init__(self,name,age,rollno,sex):
		self.name = name
		self.age = age
		self.rollno = rollno
		self.sex = sex
		print(name)
		print(age)
		print(rollno)
		print(sex,"\n\n")
		
search = input("Enter the student name : ")
student1 = student("Dattu",18,3,"Male")
student2 = student("Rahul",19,8,"Male")
student3 = student("Surya",5,42,"Female")