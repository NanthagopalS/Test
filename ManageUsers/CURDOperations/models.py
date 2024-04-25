from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=60, null=False)
    dob = models.DateField()
    email = models.EmailField()
    mobile_number = models.BigIntegerField()
    class Meta:
        db_table = 'UserDetails'

class AddressDetails(models.Model):
    address_line1 = models.TextField(max_length=100, null=False)
    address_line2 = models.TextField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    pincode = models.BigIntegerField(null=False)
    user = models.OneToOneField(UserDetails, on_delete=models.CASCADE)
    class Meta:
        db_table = 'AddressDetails'
