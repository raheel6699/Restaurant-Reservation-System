from rest_framework.serializers import ModelSerializer, SerializerMethodField
from dashboard.models import *


class RestaurantSerializer(ModelSerializer):
    user_name = SerializerMethodField("get_user_name")

    class Meta:
        fields = "__all__"
        model = RestaurantInformation

    def get_user_name(self, obj):
        return obj.user_id.first_name + obj.user_id.last_name


class DateSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = RestaurantDate


class SeatAMSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = RestaurantSeatAM


class SeatPmSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = RestaurantSeatPM


class ReservationSeatSerializer(ModelSerializer):
    restaurant_name = SerializerMethodField("get_restaurant_name")
    seat_am = SerializerMethodField("get_seat_am")
    seat_pm = SerializerMethodField("get_seat_pm")
    seat_am_date = SerializerMethodField("get_seat_am_date")
    seat_pm_date = SerializerMethodField("get_seat_pm_date")

    class Meta:
        fields = "__all__"
        model = Reservation

    def get_restaurant_name(self, obj):
        try:
            return obj.restaurant_id.restaurant_name
        except :
            return ""

    def get_seat_am(self, obj):
        try:
            if obj.seat_slot_am is None:
                return ""
            else:
                return obj.seat_slot_am.seat_slot_am
        except:
            return ""

    def get_seat_pm(self, obj):
        try:
            if obj.seat_slot_pm is None:
                return ""
            else:
                return obj.seat_slot_pm.seat_slot_pm
        except:
            return ""

    def get_seat_am_date(self, obj):
        try:
            if obj.seat_slot_am is None:
                return ""
            else:
                return obj.seat_slot_am.date_id.date
        except:
            return ""

    def get_seat_pm_date(self, obj):
        try:
            if obj.seat_slot_pm is None:
                return ""
            else:
                return obj.seat_slot_pm.date_id.date
        except:
            return ""