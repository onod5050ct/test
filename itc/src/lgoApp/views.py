from django.shortcuts import render

def mainView(request):
    template_name="lgoApp/main.html"
    return render(request, template_name)

def menuView(request):
    template_name="lgoApp/menu.html"
    return render(request, template_name)

def bousaiView(request):
    template_name="lgoApp/bousai.html"
    return render(request, template_name)

def garbageView(request):
    template_name="lgoApp/garbage.html"
    return render(request, template_name)

def iventView(request):
    template_name="lgoApp/ivent.html"
    return render(request, template_name)

def kouhouView(request):
    template_name="lgoApp/kouhou.html"
    return render(request, template_name)

def consulReserveView(request):
    template_name="lgoApp/consulReserve.html"
    return render(request, template_name)

def consulReserveDayView(request):
    template_name="lgoApp/consulReserveDay.html"
    return render(request, template_name)

def reserveView(request):
    template_name="lgoApp/reserve.html"
    return render(request, template_name)

