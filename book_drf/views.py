import json

from django.http import JsonResponse
from django.views import View
from books.models import BookInfo
from book_drf.my_serializer import BookSerializer


# from django.core import serializers


class Books(View):

    def get(self, request):
        # books = serializers.serialize("json", BookInfo.objects.all())
        books = BookInfo.objects.all()
        ser = BookSerializer(books, many=True)
        # 序列化做的事👇
        # book_list = []
        # for book in books:
        #     book_list.append(
        #         {
        #             'id': book.id,
        #             'btitle': book.btitle,
        #             'bread': book.bread,
        #             'bcomment': book.bcomment,
        #             'bpub_date': book.bpub_date,
        #         }
        #     )
        return JsonResponse(ser.data, safe=False)

    def put(self, request, pk):  # 更新和保存的逻辑相似
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)  # 转换成字典形式
        # 2、验证数据
        # btitle = data_dict.get('btitle')
        # bpub_date = data_dict.get('bpub_date')
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'wrongwrong'})
        # 3、更新数据
        # book.btitle = btitle
        # book.bpub_date = bpub_date
        # book.save()
        ser = BookSerializer(book, data=data_dict)
        ser.is_valid()
        ser.save()
        # 4、返回结果
        return JsonResponse(ser.data)

    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)  # 转换成字典形式
        # 2、验证数据
        ser = BookSerializer(data=data_dict)
        # 3、保存数据
        if bpub_date is None or bpub_date is None:
            return JsonResponse({'error': '无数据'}, status=400)
        book = BookInfo.objects.create(btitle=btitle, bpub_date=bpub_date)
        # 4、返回结果
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'bpub_date': book.bpub_date,
            }
        )
