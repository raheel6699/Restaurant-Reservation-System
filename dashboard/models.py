from django.db import models
from users.models import *
# Create your models here.


class RestaurantInformation(models.Model):
    restaurant_name = models.CharField(max_length=255, null=True, blank=True)
    restaurant_description = models.TextField(null=True)
    restaurant_address = models.TextField(null=True)
    restaurant_city = models.CharField(max_length=255, null=True, blank=True)
    restaurant_telephone = models.CharField(max_length=255, null=True, blank=True)
    restaurant_zip = models.CharField(max_length=255, null=True, blank=True)
    restaurant_state_code = models.CharField(max_length=255, null=True, blank=True)
    restaurant_country_code = models.CharField(max_length=255, null=True, blank=True)
    restaurant_longitude = models.CharField(max_length=255, null=True, blank=True)
    restaurant_latitude = models.CharField(max_length=255, null=True, blank=True)
    restaurant_email = models.CharField(max_length=255, null=True, blank=True)
    restaurant_logo = models.CharField(max_length=255, null=True, blank=True)
    min_seat = models.IntegerField(null=True)
    max_seat = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant_name


class RestaurantDate(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField(null=True)
    restaurant_id = models.ForeignKey(RestaurantInformation, on_delete=models.CASCADE)


class RestaurantSeatAM(models.Model):
    date_id = models.ForeignKey(RestaurantDate, on_delete=models.CASCADE)
    seat_slot_am = models.CharField(max_length=550, null=True)
    is_book = models.BooleanField(default=False)
    restaurant_id = models.ForeignKey(RestaurantInformation, on_delete=models.CASCADE)


class RestaurantSeatPM(models.Model):
    date_id = models.ForeignKey(RestaurantDate, on_delete=models.CASCADE)
    seat_slot_pm = models.CharField(max_length=550, null=True)
    is_book = models.BooleanField(default=False)
    restaurant_id = models.ForeignKey(RestaurantInformation, on_delete=models.CASCADE)


class Reservation(models.Model):
    restaurant_id = models.ForeignKey(RestaurantInformation, on_delete=models.CASCADE)
    seat_slot_am = models.ForeignKey(RestaurantSeatAM, on_delete=models.CASCADE, null=True)
    seat_slot_pm = models.ForeignKey(RestaurantSeatPM, on_delete=models.CASCADE, null=True)
    total_person = models.IntegerField(null=True)
    first_name = models.CharField(max_length=525, null=True)
    last_name = models.CharField(max_length=525, null=True)
    phone_number = models.CharField(max_length=525, null=True)
    email = models.CharField(max_length=525, null=True)



