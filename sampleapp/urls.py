from django.urls import path
# from django.urls import path
from .views import uploadView,like_image, dislike_image

urlpatterns = [
    path('', uploadView, name='upload_image'),
    # path('upload/',  image_upload, name='upload_image'),
    path('like/<int:id>', like_image, name='like_image'),
    path('dislike/<int:id>', dislike_image, name='dislike_image'),
]
