class person:
  def setPersonData(self,firstName,lastName,age):
      self.firstName=firstName
      self.lastName=lastName
      self.age=age
  def displayData(self):
      print(self.firstName,self.lastName,self.age)

personInfo=person()
personInfo.setPersonData("Rohan","Kratos",21)
personInfo.displayData()
