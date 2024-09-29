from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from music.models import Artist, Album, Song
from music.serializers import ArtistSerializer, AlbumSerializer, SongSerializer


def index(_request):
    return HttpResponse("My first API!")


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def list(self, request):
        """
        List the resources, albums in this case
        """
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new resource, album in this case
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """
        Retrieve a single resource, album in this case
        """
        album = get_object_or_404(Ablum, pk=pk)
        serializer = self.serializer_class(album)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update the resource, album in this case
        """
        album = get_object_or_404(Album, pk=pk)
        serializer = self.serializer_class(album, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """
        Partially update the resource, album in this case
        """
        album = get_object_or_404(Album, pk=pk)
        serializer = self.serializer_class(album, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Delete the resource, album in this case
        """
        album = get_object_or_404(Album, pk=pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer