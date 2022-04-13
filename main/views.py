from rest_framework import generics, filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from main.models import Type, Product, ProductImage
from main.serializers import TypeSerializer, ProductSerializer, ProductImageSerializer


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ProductViewPagination(LimitOffsetPagination):
    default_limit = 2


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('model', 'title')
    ordering_fields = ('type')
    pagination_class = ProductViewPagination


class ProductImageView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}