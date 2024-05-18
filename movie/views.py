from rest_framework.viewsets import ViewSet

from movie.models import Movie


class MovieViewSet(ViewSet):
    def get_all(self, request):
        pass

    def get_one(self, request):
        pass

    def get_by_genre(self, request):
        pass

    def get_by_director(self, request):
        pass

    def get_by_actor(self, request):
        pass

    def save_movie(self, request):
        pass

    def delete_movie(self, request):
        pass


class CommentViewSet(ViewSet):
    def create(self, request):
        pass

    def update(self, request):
        pass

    def delete(self, request):
        pass
