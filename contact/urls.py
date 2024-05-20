from django.urls import path

from contact.views import ContactViewSet

urlpatterns = [
    path('contact/', ContactViewSet.as_view({'post': 'contact'}), name='contact')
]
