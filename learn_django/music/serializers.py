from django.core.validators import MaxLengthValidator
from rest_framework.serializers import ModelSerializer, CharField, URLField
from .models import Song


class SongSerializer(ModelSerializer):
    title = CharField(max_length=300, validators=[MaxLengthValidator])
    url = URLField(max_length=1000)
    artist = CharField(max_length=255)

    class Meta:
        model = Song

    # def create(self, validated_data):
    #     return Song.objects.create(**validated_data)
