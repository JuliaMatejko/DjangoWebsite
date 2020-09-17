from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import BasicInfoCard

def index(request):
    latest_added_infocards = BasicInfoCard.objects.order_by('-date_of_registration')[:5]
    context = {'latest_added_infocards': latest_added_infocards}
    return render(request, 'info_cards/index.html', context)

def detail(request, infocard_id):
    try:
        infocard = BasicInfoCard.objects.get(pk=infocard_id)
    except BasicInfoCard.DoesNotExist:
        raise Http404("Infocard with this id does not exist")
    return render(request, 'info_cards/index.html', {'infocard': infocard_id})