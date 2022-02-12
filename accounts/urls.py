from django.urls import path
from . import views
urlpatterns=[
    path('Registration',views.register,name='Registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
