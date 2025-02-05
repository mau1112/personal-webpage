from django.shortcuts import render
from chuzos.models import ChuzoReview

# Create your views here.

def chuzos_list_view(request):
    chuzos = ChuzoReview.objects.all()
    pass

def chuzos_detail_view(request, chuzo_id):
    chuzo = ChuzoReview.objects.get(id=chuzo_id)
    pass