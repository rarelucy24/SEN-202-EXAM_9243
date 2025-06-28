from django.db import models

class StaffBase(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    class Meta:
        abstact = True
        
    def get_role(self):
         return "staff"   
     
     
class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)
    
    class Meta:
        abstact = True
        
    def get_role(self):
         return "Manager"
            
class Intern(StaffBase):
     mentor = models.ForeignKey(Manager,on_delete=models.CASCADE,related_name="Internt")
     intership_name = models.DateField()
     
     class Meta:
        abstact = True
         
        def get_role(self):
         return "internt"      
     
class Address(models.Model):
    street= models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def _str_(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country},{self.zip_code}"
      

