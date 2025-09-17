# Definiing the class for future instanciation (hope I've written this correctly yunno!?). Pretty sick of jobs... I'm a fucking founder.

class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, hoursWorked, salary, name):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def contents(self):
    print(f"{self.name} has a nice job as a lawyer in NYC with a salary of {self.salary}$ for {self.hoursWorked} hours of work")

jobb = job(80, 300000.99, "Harvey Specter")
jobb.contents()
print()

# Now writing the doctor class with a few tweaks

class doctor(job):

  speciality = None
  yearsXP = None
  
  def __init__(self):
    self.name = "Jonno"
    self.salary = 120000.99
    self.hoursWorked = 60
    self.speciality = "Pediatric Consultant"
    self.yearsXP = 7

  def contents(self):
    print(f"{self.name} has a salary of {self.salary}$ for {self.hoursWorked} hours of work. Additionally, he has {self.yearsXP} years of experience as a {self.speciality}.")

drHouse = doctor()
drHouse.contents()
print()

# Now writing the teacher class with a few tweaks. Pretty sick of this kind of job. Very few of them are doing it right, VEEEERY few

class teacher(job):

  subject = None
  position = None

  def __init__(self):
    self.name = "Jonno222"
    self.salary = 70000.99
    self.hoursWorked = 40
    self.subject = "Computer Science"
    self.position = "teacher"

  def contents(self):
    print(f"{self.name} has a salary of {self.salary}$ for {self.hoursWorked} hours of work as a {self.subject} {self.position}.")

prfXavier = teacher()
prfXavier.contents()
