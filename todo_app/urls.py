from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('check/<int:id>',views.is_done.as_view(),name='check'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='login.html'),name='logout'),
    path('signup/',views.signup.as_view(),name='signup'),
    path('delete/<int:id>/',views.delete.as_view(),name='del'),
    path('edit/<int:id>/',views.edit.as_view(),name='edit')
]