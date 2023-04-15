from django.urls import path
from . import views
from .views import signinAPI,registerAPI

urlpatterns=[
    path('signin/',signinAPI.as_view()),
    path('register/',registerAPI.as_view()),
    # path('register/',views.register)
]