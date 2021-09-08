from rest_framework import serializers


class BookSerializer(serializers.Serializer):
# 根据模型类来定义
# 序列化返回数据
    btitle = serializers.CharField()
    bread = serializers.IntegerField()
    bpub_date = serializers.DateField()


