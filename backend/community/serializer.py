from attr import field
from rest_framework import serializers

from community.models import PostImage, Post


class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PostImage
        fields = ['image']


class CommunitySerializer(serializers.ModelSerializer):
    images = PostImageSerializer(source='postimage_posts', many=True)

    class Meta:
        model = Post
        fields = ['title', 'article', 'music_code', 'images']

    def get_user_email(self, obj):
        return obj.writer.email

    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            PostImage.objects.create(post=instance, image=image_data)
        return instance


class CommunityUpdateSerializer(serializers.ModelSerializer):
    writer = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'article', 'music_code', 'writer']
