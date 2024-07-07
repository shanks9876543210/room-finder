from django.urls import path
from .views import register, register_success, login_view, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('register/success/', register_success, name='register_success'),
    path('login/', login_view, name='login'),
    # path('staff/login/', staff_login_view, name='staff_login'),
    path('logout/', logout_view, name='logout'),
]
