from django.db import models

class Department(models.Model):
    # Model to store department information
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    # Model to store course information
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Order(models.Model):
    # Model to store order information
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    PURPOSE_CHOICES = [('Enquiry', 'For Enquiry'), ('Order', 'Place Order'), ('Return', 'Return')]
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    notebook = models.BooleanField()
    pen = models.BooleanField()



