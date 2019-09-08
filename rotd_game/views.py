from django.shortcuts import render
from boot.models import Boot

def home(request):
    all_boots = Boot.objects.order_by("bt_name").reverse()
    return render(request, "index.html", {"all_boots": all_boots})
