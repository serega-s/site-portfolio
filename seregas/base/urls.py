from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('', views.home, name='account'),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('send_email/', views.send_email, name="send_email"),
    path('create_post/', views.create_post, name="create_post"),
    path('update_post/<slug:slug>/', views.update_post, name="update_post"),
    path('delete_post/<slug:slug>/', views.delete_post, name="delete_post"),

    path('account/', views.user_account, name="account"),
    path('update_profile/', views.update_profile, name="update_profile"),

    # Auth
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
