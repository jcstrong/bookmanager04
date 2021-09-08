import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from books.models import BookInfo
from rest_framework.generics import \
    ListAPIView,CreateAPIView, UpdateAPIView, \
    RetrieveAPIView, DestroyAPIView

class BookView(View):
    #     获取所有图书、保存
    def get(self, request):
        # 查询并返回所有图书对象，
        books = BookInfo.objects.all()
        book_list = []
        for book in books:
            book_list.append(
                {
                    'id': book.id,
                    'btitle': book.btitle,
                    'bread': book.bread,
                    'bcomment': book.bcomment,
                    'bpub_date': book.bpub_date,
                }
            )
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)  # 转换成字典形式
        # 2、验证数据
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')
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


class BookView(View):
    #     获取单一、更新、删除

    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'id错误'}, status=400)
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'bpub_date': book.bpub_date,
            }
        )

    def put(self, request, pk):  # 更新和保存的逻辑相似
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)  # 转换成字典形式
        # 2、验证数据
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')
        # 3、更新数据
        if bpub_date is None or bpub_date is None:
            return JsonResponse({'error': '无数据'}, status=400)
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'id错误'}, status=400)
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
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

    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'id错误'}, status=400)
        book.is_delete = True
        book.save()
        return JsonResponse({})


# class BookCView(CreateAPIView):
