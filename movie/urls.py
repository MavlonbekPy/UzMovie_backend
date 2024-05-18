from django.urls import path
from .views import MovieViewSet, CommentViewSet

urlpatterns = [
    # MOVIE
    path('movie/get-all/', MovieViewSet.as_view({'get': 'get_all'})),
    path('movie/get-one/', MovieViewSet.as_view({'get': 'get_one'})),
    path('movie/by-genre/', MovieViewSet.as_view({'get': 'get_by_genre'})),
    path('movie/by-director/', MovieViewSet.as_view({'get': 'get_by_director'})),
    path('movie/by-actor/', MovieViewSet.as_view({'get': 'get_by_actor'})),
    # SAVED
    path('movie/save/', MovieViewSet.as_view({'post': 'save_movie'})),
    path('movie/delete/', MovieViewSet.as_view({'delete': 'delete_movie'})),

    # COMMENT
    path('comment/create/', CommentViewSet.as_view({'post': 'create'})),
    path('comment/update/', CommentViewSet.as_view({'patch': 'update'})),
    path('comment/delete/', CommentViewSet.as_view({'delete': 'delete'})),

]
