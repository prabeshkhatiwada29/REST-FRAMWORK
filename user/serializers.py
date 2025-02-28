from rest_framework import serializers
from .models import User

def age_vaildator(age):
    if age < 18:
        raise serializers.ValidationError('Age must be greater than 18')
    return age


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created_at','id')
        extra_kwargs = {
            
            'age':{
                'validators':[age_vaildator]
        }
        }



