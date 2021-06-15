from rest_framework import serializers
from web.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title','description','image')