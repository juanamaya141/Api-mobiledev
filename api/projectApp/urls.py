from django.urls import path, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("*")

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("*")

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ("*")



# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BrandList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['brands']
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
class StoreList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['stores']
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
class DealList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['deals']
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('brands/', BrandList.as_view()),
    path('stores/', StoreList.as_view()),
    path('deals/', DealList.as_view()),
]