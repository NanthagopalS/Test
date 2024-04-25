from rest_framework import serializers
from .models import UserDetails,AddressDetails

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = ["address_line1", "address_line2", "city", "state","pincode","user"]

class UserSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField(method_name="get_address", read_only = True)
    class Meta:
        model = UserDetails
        fields = ["id", "name", "dob", "email","mobile_number","address"]

    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = super().create(validated_data)
        self.initial_data.update(user=user.id)
        address_serializer = UserAddressSerializer(data=self.initial_data)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()
        return user
    def get_address(self, user):
        # print(dir(user))
        # print(user.addressdetails)
        address = UserAddressSerializer(user.addressdetails)
        # print(address.data)
        return address.data