from .models import CustomUser

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'url' ,'id', 'username', 'email', 'is_staff']



class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    # password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['url','username', 'email', 'password', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}
    
    # Vérifier que l'email est unique
    def validated_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('Un utilisateur avec cet Email existe déjà')
        return value
    
    # verifier que le mot finish must occur after startde passe est différent du nom d'utilisateur
    def validate(self, data):
        if data['username'] in data['password']:
            raise serializers.ValidationError("Le mot de passe ne doit pas contenir le nom d'utilisateur")
        return data

    # Créer l'utilisateur avec son mot de passe
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email = validated_data['email'],
            username= validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user