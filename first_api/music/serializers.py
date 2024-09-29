from rest_framework import serializers

from music.models import Artist, Album, Song

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']


class AlbumSerializer(serializers.Serializer):
    title = serializers.CharField()
    artist = ArtistSerializer()
    release_year = serializers.IntegerField()

    class Meta:
        fields = ['title', 'artist', 'release_year']

    def create(self, validated_data):
        artist_data = validated_data.pop('artist')
        artist, created = Artist.objects.get_or_create(name=artist_data['name'])
        return Album.objects.create(artist=artist, **validated_data)

    def update(self, instance, validated_data):
        artist_data = validated_data.pop('artist')
        artist, created = Artist.objects.get_or_create(name=artist_data['name'])

        album.title =  validated_data.get('title', instance.title)
        album.release_year = validated_data.get('release_year', instance.release_year)
        album.artist = artist
        album.save()

        return album


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['author', 'title', 'artist', 'album', 'duration']