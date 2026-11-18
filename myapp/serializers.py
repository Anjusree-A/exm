from rest_framework import serializers

from myapp.models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('username', 'email','password')
    def create(self, validated_data):
        u= Employee.objects.create(**validated_data)
        u.save()
        return u

