class Patient:
  
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    return "{}’s estimated insurance costs is {} dollars.".format(self.name,str(estimated_cost))
  
  def update_age(self, new_age):
    self.age = new_age
    return "{} is now {} years old.".format(self.name, str(self.age)) 
  
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print("{} has {} child.".format(self.name, str(self.num_of_children)))
    else:
      print("{} has {} children.".format(self.name, str(self.num_of_children)))

  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print("{} has a body mass index of {}.".format(self.name, str(self.bmi)))

  def update_smoking_status(self, new_smoking_status):
    self.smoker = new_smoking_status
    if self.smoker == 1:
      print("{} is a smoker.".format(self.name))
    else:
      print("{} is not a smoker.".format(self.name))
      
  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information

###### Example of patient information ######
  
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)

##### Examples of patient information update ######

print(patient1.bmi)
print(patient1.estimated_insurance_cost())
print(patient1.update_age(26))
print(patient1.estimated_insurance_cost())
print(patient1.update_num_children(1))
print(patient1.estimated_insurance_cost())
print(patient1.patient_profile())
print(patient1.update_bmi(28))
print(patient1.update_smoking_status(0))
