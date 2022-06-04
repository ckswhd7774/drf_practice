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
        fields = ['title', 'article', 'music_code', 'images', 'category']

    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            PostImage.objects.create(post=instance, image=image_data)
        return instance


class CommunityUpdateSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(source='postimage_posts', many=True)
    writer = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'article', 'music_code', 'writer', 'images', 'category']

    def update(self, instance, validated_data):
        instance = Post.objects.update(**validated_data)
        post_images = PostImage.objects.all(post=instance)

        instance.title = validated_data.get('title', instance.title)
        instance.article = validated_data.get('article', instance.article)
        instance.music_code = validated_data.get('music_code', instance.music_code)
        instance.save()

        post_images.image = instance.get('image', PostImage.image)
        post_images.save()

        return instance
