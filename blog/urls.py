from django.urls import path
from blog import views

urlpatterns = [

    path('', views.showblog, name='showblog'),
    path('<int:post_id>/', views.specific_post, name='specific_post'),
]
