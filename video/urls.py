from django.urls import path, include
from .views import newsfeed,singleVideo,saveComment,uploadVideo,saveVideo


urlpatterns = [
    path('', newsfeed, name='newsfeed'),
    path('video/<pk>/<str:title>/', singleVideo, name='video-reading'),
    path('save-comment/<pk>/', saveComment, name='save-comment'),
    path('save-video/', saveVideo, name='save-video'),
    path('upload-video/', uploadVideo, name='upload-video'),

]
