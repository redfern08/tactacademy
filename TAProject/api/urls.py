from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('app_user', views.UsersViewset, basename='app_user')
router.register('post', views.PostViewset, basename='post')

urlpatterns = router.urls