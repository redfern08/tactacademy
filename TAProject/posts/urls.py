from django.urls import path 
from . import views 

app_name = 'posts'

urlpatterns = [ 
    path('', views.HomeView.as_view(), name="home"),
    path('posts/', views.PostListView.as_view(), name="stories"),
    path('create/', views.CreateStoryView.as_view(), name="create"),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name="detail"),
    path('update/<int:pk>/', views.UpdateStoryView.as_view(), name="update"),
    path('delete/<int:pk>/', views.DeleteStoryView.as_view(), name="delete"),
]