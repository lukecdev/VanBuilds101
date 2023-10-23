from . import views
from django.urls import path
from .views import PostCreateView


urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/', PostCreateView.as_view(), name='add_post'),

]
