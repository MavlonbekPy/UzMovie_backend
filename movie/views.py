from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from movie.serializers import MovieSerializer, SavedSerializer

from movie.models import Movie, Genre, Actor, Director, Saved, Comment, Transaction


class MovieViewSet(ViewSet):
    def get_all(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_one(self, request):
        data = request.data
        movie = Movie.objects.get(id=data['id'])
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_by_genre(self, request):
        data = request.data
        movies = Movie.objects.filter(genre=data['genre'])
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_by_director(self, request):
        data = request.data
        movies = Movie.objects.filter(directors=data['director'])
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_by_actor(self, request):
        data = request.data
        movies = Movie.objects.filter(actors=data['actor'])
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def save_movie(self, request):
        data = request.data
        saved = Saved.objects.create(user=data['user'], movie=data['movie'])
        serializer = SavedSerializer(saved, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_movie(self, request):
        pass


class CommentViewSet(ViewSet):
    def create(self, request):
        pass

    def update(self, request):
        pass

    def delete(self, request):
        pass
