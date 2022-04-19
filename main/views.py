from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions, AllowAny
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from main.models import Type, Product, Comment
from main.serializers import TypeSerializer, ProductSerializer, CommentSerializer

from django_filters import rest_framework as  filters

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         return [IsAdminUser]
    #     return []



class ProductViewPagination(LimitOffsetPagination):
    default_limit = 6



class ProductFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price',
                                      lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price',
                                    lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['type']


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, )
    search_fields = ('model', 'titles')
    pagination_class = ProductViewPagination
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(self.__class__, self).get_permissions()


    def get_serializer_context(self):
        return {'request': self.request}


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super(self.__class__, self).get_permissions()

