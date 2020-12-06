from rest_framework import serializers
from Authority.models import foodAvbl, otherDetails
from Student.models import FoodReq


class AvblSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodAvbl
        fields = "__all__"


class ReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReq
        fields = "__all__"


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = otherDetails
        fields = "__all__"
