from rest_framework.serializers import ModelSerializer

from movie.models import Movie, Comment, Genre, Actor, Director, Saved, Transaction


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class SavedSerializer(ModelSerializer):
    class Meta:
        model = Saved
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
