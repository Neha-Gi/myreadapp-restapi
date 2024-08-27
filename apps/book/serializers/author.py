from rest_framework import serializers
from apps.book.models import Author
class AuthorSerializer(serializers.ModelSerializer):
    #specify the model ie going to link with seriallizer
    name = serializers.CharField(read_only=True)
    def validate_first_name(self,value):
        if '-' in value:
            raise serializers.ValidationError('first name should not contain hyphrn (-)')
    
        return value
    
    def validate(self, attrs):
        if attrs.get('first_name') == attrs.get('last_name'):
           raise serializers.ValidationError('first name and last name should npot be same ')
          
        return attrs
    
    def get_username(self,obj) :

        return '_'.join([obj.first_name,obj.last_name])

    class Meta :
        model = Author
        field = '_all_'#'id','first_name')