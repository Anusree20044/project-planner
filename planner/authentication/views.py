from django.shortcuts import render

from django.contrib.auth import authenticate

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import ProfileSerializer

from .models import Profile

from planner.utils import generate_password

# Create your views here.

class LoginView(APIView):

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')

        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user :

            refresh_token = RefreshToken.for_user(user)

            access_token = refresh_token.access_token

            data = {'refresh': str(refresh_token), 'access': str(access_token)}

            return Response(data, status=200)

        data = {'msg': 'invalid username or password'}

        return Response(data, status=400)

class UserRegistrationView(APIView):
    
    serializer_class = ProfileSerializer   

    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            username = serializer.validated_data.get('username') 
                
            profile = serializer.save()  

            profile.email = username

            password =  generate_password()

            profile.set_password(password)

            profile.save()

            data = {

                    "message": "User registered successfully"
                }
            
            return Response(data, status=201)

        return Response(serializer.errors, status=400)


        




         

        