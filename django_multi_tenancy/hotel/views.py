from rest_framework.viewsets import ModelViewSet
from .serializers import HotelSerializer
from .models import Hotel
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

tenant_header = openapi.Parameter(
    'Tenant-Header',  # Name of the header
    openapi.IN_HEADER,  # Specify that it's a header
    description="A unique string value indentifying the tenant",  # Description
    type=openapi.TYPE_STRING,  # Type of the header value (string in this case)
    required=True  # Set it to True to make it a required header
)
class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @swagger_auto_schema(manual_parameters=[tenant_header])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(manual_parameters=[tenant_header])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(manual_parameters=[tenant_header])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(manual_parameters=[tenant_header])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(manual_parameters=[tenant_header])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(manual_parameters=[tenant_header])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)