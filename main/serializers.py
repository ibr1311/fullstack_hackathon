from rest_framework import serializers
from main.models import Type, Product, Comment


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'product', 'name', 'text', 'date_added')

class ProductSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'type', 'model', 'charac', 'titles', 'desc', 'price', 'image', 'comment')

        def _get_image_url(self, obj):
            if obj.image:
                url = obj.image.url
                request = self.context.get('request')
                if request is not None:
                    url = request.build_absolute_uri(url)
            else:
                url = ''
            return url

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['image'] = self._get_image_url(instance)
            return representation


