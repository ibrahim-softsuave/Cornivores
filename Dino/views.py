from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

def signin(request):
    return HttpResponse ('Signin Successfully')
@csrf_exempt
def register(request):
        if request.method == "POST":
            if not request.data.username:
                 return HttpResponse('Username is missing')
            else:
                if request.data.password != request.data.confirm_password:
                        return HttpResponse('password is mis matching')
                else:
                    user=CustomUser()
                    user.objects.create_user(username=request.data.username,phone_number=request.data.phone_number,email=request.data.email)
                    user.set_password(request.data.password)
                    user.save()
                    return HttpResponse ('User Craete Successfully')
        return HttpResponse('nousername')