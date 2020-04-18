from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer#this should be serializer_class not other name

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Gives us the most control over our applications',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """"Creates a hello message with our name"""
        serializerss= self.serializer_class(data=request.data)

        if serializerss.is_valid():
            name = serializerss.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializerss.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handles updating an object"""
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """Handles a partial update of object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Deletes an object"""
        return Response({'method':'DELETE'})

class HelloViewSets(viewsets.ViewSet):
    """Test API Viewsets"""
    def list(self, request):
        """Return a hello message"""
        a_viewsets=[
            'Uses actions (list,create,retrieve,update,partial_update)',
            'Automaticaly maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewsets':a_viewsets})

    def retrieve(self,request,pk=None):
        """Handles Getting Object by its ID"""
        return Response({'http_method':"GET"})

    def update(self,request,pk=None):
        """Handles Updating an object"""
        return Response({'HTTP_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles updating a part of object"""
        return Response({'http_method':'Patch'})
    def destroy(self,request,pk=None):
        """Handles destroying an object"""
        return Response({"Http_method":"DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiels"""
    serializer_class = serializers.UserProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields=('name','email',)
    queryset = models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
