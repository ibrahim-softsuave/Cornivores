from django.urls import path
from . import views
# from .views import signinAPI,registerAPI
from . import views

urlpatterns=[
    # path('signin/',signinAPI.as_view()),
    # path('register/',registerAPI.as_view()),
    path('register/',views.register),
    path('signin/',views.signin),

]