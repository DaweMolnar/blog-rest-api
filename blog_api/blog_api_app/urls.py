from django.urls import path
from . import views

urlpatterns = [
    path('api/post/', views.PostCreate.as_view()),
    path('api/author/', views.AuthorCreate.as_view()),
    path('api/label/', views.LabelCreate.as_view()),
    path('api/comment/', views.CommentCreate.as_view()),
    path('api/comment/filter/<post_id>', views.CommentView.as_view()),
    path('api/comment/delete/<pk>', views.CommentDelete.as_view()),
]