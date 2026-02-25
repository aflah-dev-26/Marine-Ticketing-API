from rest_framework import serializers
from .models import Booking,Payment

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','route','travel_date']

class OtpVerifySerializer(serializers.Serializer):
    class Meta:
        booking_id = serializers.IntegerField()
        otp = serializers.CharField(max_length=6)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','booking','payment_method','amount']
        read_only_fields = ['booking']    