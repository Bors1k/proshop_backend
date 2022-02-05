from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status

from base.models import UserProfile
from base.serializer import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = UserProfile.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = UserProfile.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserById(request, pk):
    user = UserProfile.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)

    data = request.data

    user.first_name = data['name']
    user.name = data['name']
    user.email = data['email']

    user.is_staff = data['is_staff']

    # if data['password'] != '':
    #     user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    delUser = UserProfile.objects.get(id=pk)
    delUser.delete()

    return Response('User was deleted')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = UserProfile.objects.create(
            name=data['name'],
            email=data['email'],
            password=make_password(password=data['password'])
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)

    data = request.data

    user.first_name = data['name']
    user.name = data['name']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)
