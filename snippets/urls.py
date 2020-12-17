from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('snippets/', views.SnippetList.as_view(), name='snippets-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
