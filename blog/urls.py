from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.blog, name='all_blogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
    ]
