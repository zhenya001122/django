from rest_framework import serializers

from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = ('title', 'content', 'cat', 'author')
