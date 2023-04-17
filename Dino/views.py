from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate
from django.views import View



# class signinAPI(View):
#     def post(self,request):
#         data=json.loads(request.body)
#         user=authenticate(request, username=data.get('username'), password=data.get('password'))
#         if user:
#             return HttpResponse ('Signin Successfully')
#         else:
#             username=CustomUser.objects.filter(username=data.get('username')).first()
#             if username is None:
#                  return HttpResponse ('Username is doesnot exist')
#             else:
#                  return HttpResponse ('Password is mismatched')
# class registerAPI(View):
#     def post(self,request):
#             data=json.loads(request.body)
#             if not data.get('username'):
#                  return HttpResponse('Username is missing')
#             else:
#                 if data.get('password') != data.get('confirm_password'):
#                         return HttpResponse('password is mis matching')
#                 else:
#                     user=CustomUser.objects.create_user(username=data.get('username'),email=data.get('email'),password=data.get('password'),phone_number=data.get('phone_number'))
#                     if user:
#                         return HttpResponse ('User Craete Successfully')
#                     else:
#                           return HttpResponse ('User Craete Failed')
          

@csrf_exempt
def signin(request):
    if request.method == "POST":
        data=json.loads(request.body)
        user=authenticate(request, username=data.get('username'), password=data.get('password'))
        if user:
            return HttpResponse ('Signin Successfully',200)
        else:
            username=CustomUser.objects.filter(username=data.get('username')).first()
            if username is None:
                 return HttpResponse ('Username is doesnot exist')
            else:
                 return HttpResponse ('Password is mismatched')
    else:
         return HttpResponse('other method')
@csrf_exempt
def register(request):
        if request.method == "POST":
            data=json.loads(request.body)
            if not data.get('username'):
                 return HttpResponse('Username is missing')
            else:
                if data.get('password') != data.get('confirm_password'):
                        return HttpResponse('password is mis matching')
                else:
                    user=CustomUser.objects.create_user(username=data.get('username'),email=data.get('email'),password=data.get('password'),phone_number=data.get('phone_number'))
                    if user:
                        return HttpResponse ('User Craete Successfully')
                    else:
                          return HttpResponse ('User Craete Failed')
        return HttpResponse('nousername')