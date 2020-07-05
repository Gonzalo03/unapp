from rest_framework import serializers

from .models import Admin


class AdminSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:

        model = Admin
        fields = ['full_name']

    def get_full_name(self, ob):
        return '{} {}'.format(ob.name, ob.last_name)