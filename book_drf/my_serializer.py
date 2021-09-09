from django.db.transaction import atomic
from rest_framework import serializers

from books.models import BookInfo


class BookSerializer(serializers.Serializer):
# 根据模型类来定义
# 序列化返回数据
    btitle = serializers.CharField()
    bread = serializers.IntegerField()
    bpub_date = serializers.DateField()

    def create(self, validated_data):
        # book = BookInfo.objects.create(btitle=validated_data['btitle'])
        # 字典拆包处理。等价👆
        book = BookInfo.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        instance.btitle = validated_data['btitle']
        instance.save() # 不是同一个save
        return instance

