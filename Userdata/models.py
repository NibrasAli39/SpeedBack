from django.db import models
from django.contrib.auth.models import User
# Create your models here.


transaction_type_choices = (
    ('shop', 'shop'),
    ('bitcoin', 'bitcoin')
)
status_choices_content = (
    ('Unpaid', 'Unpaid'),
    ('Paid', 'Paid')
)
expertise_choices_content = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
)


class StoreDetails(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True)
    store_name = models.CharField(max_length=300,  blank=True)
    branchmanager_mobilenumber = models.IntegerField(default=0)
    branch_mobilenumber = models.IntegerField(default=0)
    storemanager_mobilenumber = models.IntegerField(default=0)
    store_number = models.IntegerField(default=0)
    activity = models.CharField(max_length=300, null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    commercial_Regno = models.IntegerField(default=0)
    storeManager_name = models.CharField(max_length=300, null=True, blank=True)
    store_application = models.CharField(max_length=300, null=True, blank=True)
    unified_number = models.IntegerField(default=0)
    email = models.CharField(max_length=300, null=True, blank=True)
    phone_order = models.IntegerField(default=0)

    def __str__(self):
        return str(self.store_name)


class DriverDetails(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True)
    membership_number = models.IntegerField(default=0)
    fullName = models.CharField(max_length=300, null=True, blank=True)
    nationality = models.CharField(max_length=300, null=True, blank=True)
    indentitynumber = models.IntegerField(default=0)
    driving_license = models.ImageField(upload_to="licenses")
    car_form = models.ImageField(upload_to="carForms")
    preffered_city = models.CharField(max_length=300, null=True)
    mobile_number = models.IntegerField(default=0)
    mobile_type = models.CharField(max_length=300, null=True, blank=True)
    free_time = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.fullName)


class AddressDetails(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    street_address = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class OrderDetails(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True)
    notes = models.CharField(max_length=300, null=True, blank=True)
    pickup_location = models.CharField(max_length=300, null=True, blank=True)
    dropoff_location = models.CharField(max_length=300, null=True, blank=True)
    dropoff_lat = models.FloatField(default=0)
    dropoff_lon = models.FloatField(default=0)
    customer_name = models.CharField(max_length=300, null=True, blank=True)
    customer_address = models.CharField(max_length=300, null=True, blank=True)
    customer_number = models.CharField(max_length=300, null=True, blank=True)
    order_status = models.CharField(max_length=300, null=True, blank=True)
    order_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.title)
