from . import views
from django.urls import path, include, re_path
from allauth.account.views import ConfirmEmailView, confirm_email, PasswordResetView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as jwt_views

urlpatterns = [

    re_path('rest-auth/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='confirm_email'),
    path('', views.PostList.as_view()),
    path('catlist/',views.CatList.as_view()),
    path('taglist/', views.TagList.as_view()),
    path('comlist/', views.CommentList.as_view()),
    path('shortpost/', views.PostShortList.as_view()),
    #path('rest-auth/password/reset/', PasswordResetView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('create_post/', views.CreatePost.as_view()),
    path('delete/<id>', views.DeletePost.as_view()),
    path('update_post/<id>', views.UpdatePost.as_view()),
    path('testview/', views.PostsView.as_view()),
    path('testview/?id=<id>', views.PostsView.as_view()),
    path('testpost/<id>', views.Testposts.as_view()),
    path('token-auth/', jwt_views.obtain_auth_token),
]
