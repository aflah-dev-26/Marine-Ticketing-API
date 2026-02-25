from django.db import models
from django.conf import settings


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Company(TimeStampModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    registration_number =models.CharField(max_length=100,unique=True) 
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ship(TimeStampModel):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='ships')
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='ship/',null=True,blank=True)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    ship_code = models.CharField(max_length=20,unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
            

class Route(TimeStampModel):
    ship = models.ForeignKey(Ship,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    departure_port = models.CharField(max_length=150)
    arrival_port = models.CharField(max_length=150)
    departure_time = models.TimeField(null=True,blank=True)
    arrival_time = models.TimeField(null=True,blank=True)
    distance_km = models.PositiveIntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.departure_port}-{self.arrival_port}"

# class Ship(TimeStampModel):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='ships')
#     route = models.OneToOneField(Route,on_delete=models.CASCADE,related_name='ships')
#     name = models.CharField(max_length=150)
#     image = models.ImageField(upload_to='ship/',null=True,blank=True)
#     capacity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10,decimal_places=2)
#     ship_code = models.CharField(max_length=20,unique=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name
    
