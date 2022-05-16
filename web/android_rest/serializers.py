from rest_framework import serializers
from zerofire.models import Manager

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['mno','id','workarea','rno']