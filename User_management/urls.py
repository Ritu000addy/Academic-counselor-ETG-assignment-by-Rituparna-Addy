from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.home, name= 'Users'),
    path('register', views.register, name= 'Users Register'),
    path('loggin', views.loggin, name= 'Users Login'),
    path('loggout', views.loggout, name= 'Users Logout'),
]