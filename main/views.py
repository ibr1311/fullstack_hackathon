from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions, AllowAny
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from main.models import Type, Product, Comment, ProductLikes
from main.serializers import TypeSerializer, ProductSerializer, CommentSerializer, LikeSerializer
from rest_framework.response import Response
from django_filters import rest_framework as  filters

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         return [IsAdminUser]
    #     return []


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
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]

        return super(self.__class__, self).get_permissions()


    def get_serializer_context(self):
        return {'request': self.request}


@api_view(['POST', 'GET', 'DELETE'])
def comment_product_api(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        comments = Comment.objects.filter(product=product)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST', 'GET'])
def like_product_api(request, pk):
    try:
        likeproduct = get_object_or_404(Product, pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        likes = ProductLikes.objects.filter(likeproduct=likeproduct)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = LikeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)