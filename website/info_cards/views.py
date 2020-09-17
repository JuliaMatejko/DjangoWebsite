from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import BasicInfoCard, DetailInfoCard

def index(request):
    latest_added_infocards = BasicInfoCard.objects.order_by('-date_of_registration')[:5]
    context = {'latest_added_infocards': latest_added_infocards}
    return render(request, 'info_cards/index.html', context)

def detail(request, basicinfocard_id):
    detail_info_card = get_object_or_404(DetailInfoCard, basic_info_card_id=basicinfocard_id)
    return render(request, 'info_cards/detail.html', {'detail_info_card': detail_info_card})