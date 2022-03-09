from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView

from tubeapp.models import Mijoz, Video, Comment, Playlist

from tubeapp.serializers import VideoSerializer, MijozSerializer, CommentSerializer, PlaylistSerializer


class MijozLC(ListCreateAPIView):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["ism"]

    def get_queryset(self):
        mijoz = Mijoz.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            mijoz = Mijoz.objects.annotate(
                similarity=TrigramSimilarity("ism", soz)
            ).filter(similarity__gte=0.4).order_by("-similarity")
        return mijoz

class MijozRUD(RetrieveUpdateDestroyAPIView):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer



class PlaylistLC(ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        playlist = Playlist.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            playlist = Playlist.objects.annotate(
                similarity=TrigramSimilarity("nom", soz)
            ).filter(similarity__gte=0.4).order_by("-similarity")
        return playlist

class PlaylistRUD(RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class VideoLC(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        video = Video.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            video = Playlist.objects.annotate(
                similarity=TrigramSimilarity("nomi", soz)
            ).filter(similarity__gte=0.4).order_by("-similarity")
        return video

class VideoD(DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class CommentLC(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentD(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer