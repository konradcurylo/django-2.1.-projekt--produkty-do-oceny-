from django.urls import path,include
from . import views


urlpatterns = [
      path('stworz', views.stworz , name='stworz'),
      path('<int:towar_id>', views.detail , name='detail'),
      path('<int:towar_id>/upvote', views.upvote , name='upvote'),

      ]
