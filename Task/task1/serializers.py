# to convert objects to JSON

from rest_framework import serializers
from task1.models import task1

#import task1 here
class task1Serializer(serializers.ModelSerializer):
    class Meta:
        model = task1
        fields = "__all__" #we are serializing all the fields

#create view after this
