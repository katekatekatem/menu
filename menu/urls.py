from django.urls import path

from .views import menu_page


urlpatterns = [
    path('menu_page/', menu_page, name='menu_page'),
]
