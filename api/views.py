from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions 
from rest_framework.views import APIView

class APIData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def getData(request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
        
    @api_view(['POST'])
    def addItem(request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)