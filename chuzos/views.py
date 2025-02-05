import json

from django.shortcuts import render, get_object_or_404


from chuzos.models import ChuzoReview

# Create your views here.

def chuzos_list_view(request):
    chuzos = ChuzoReview.objects.all().values()
    chuzos = json.dumps(chuzos, default=str)
    context = {'chuzos': chuzos}
    return render(request, "chuzos/chuzos_list.html", context)

def chuzos_detail_view(request, chuzo_id):
    chuzo = get_object_or_404(ChuzoReview, id=chuzo_id)
    pass