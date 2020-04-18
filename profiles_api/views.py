from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
