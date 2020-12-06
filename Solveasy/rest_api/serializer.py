from rest_framework import serializers
from Authority.models import problem, otherDetails

class AvblSerializer(serializers.ModelSerializer):
    class Meta:
        model = problem
        fields = "__all__"


# class ReqSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FoodReq
#         fields = "__all__"


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = otherDetails
        fields = "__all__"
