from rest_framework import serializers
from apps.book.models import Tag

class TagSerializer(serializers.ModelSerializer):
   
    def validate_name(self,value):
        if any (char in value for char in '!@#$%^&*' ):
            raise serializers.ValidationError('first name should not contain special characters')
    
        return value
    class Meta :
        model = Tag
        filed = '_all_'
        read_only_fields =('id')