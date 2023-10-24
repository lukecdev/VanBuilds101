from . import views
from django.urls import path
from .views import PostCreateView
from .views import UpdatePostView


urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('update_post/<slug:slug>', UpdatePostView.as_view(), name='update_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    # path('post/', PostCreateView.as_view(), name='add_post'),
  

]
