from rest_framework import serializers

from .models import User, School



class SchoolSerializer(serializers.ModelSerializer):

    class Meta:

        model = School
        fields = ['name']



class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()
    school = SchoolSerializer(many= True)

    class Meta:

        model = User
        fields = [
            'full_name',
            'token',
            'school'
        ]

    def get_full_name(self, ob):
        return '{} {}'.format(ob.name, ob.last_name)

    
