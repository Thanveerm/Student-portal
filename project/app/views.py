from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import Registration

from app.serializers import RegistrationSerializer
from django.views.decorators.csrf import csrf_exempt

class RegistrationCRUDCBV(ModelViewSet):
    student=Registration.objects.all()
    serializrer_class=RegistrationSerializer


from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Registration

@csrf_exempt
def register_api(request):
    print("helloooo")
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_password = data['password']
        data_email = data['email_id']
        print("data_password::::",str(data_password))
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.create_user(data_email, data_email, data_password)
            update_reg = Registration.objects.filter(id=serializer.data['id']).update(author=user)




            return JsonResponse(serializer.data, status=201)


from django.contrib.auth import authenticate, login
from django.contrib.auth import login as authlogin

def login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        passwrd = request.POST.get("passwrd")
        user = authenticate(request, username=uname, password=passwrd)
        if user is not None:
            authlogin(request, user)
            # Redirect to a success page.
            # return redirect('')
            data = Registration.objects.get(author=request.user)
            return render(request,'home.html',{'data':data})

    return render(request,'login.html')