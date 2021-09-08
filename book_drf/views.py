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
