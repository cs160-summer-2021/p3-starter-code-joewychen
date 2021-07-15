from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.interaction, name='new_interaction'),
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('new_interaction_trig', views.interaction_trig, name='new_interaction_trig')
]
