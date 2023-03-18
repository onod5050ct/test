from django.urls import path
from .views import mainView, menuView, bousaiView, garbageView, iventView, kouhouView, consulReserveView, consulReserveDayView, reserveView
 
urlpatterns = [
  path("main/", mainView),
  path("menu/", menuView),
  path("bousai/", bousaiView),
  path("garbage/", garbageView),
  path("ivent/", iventView),
  path("kouhou/", kouhouView),
  path("consulReserve/", consulReserveView),
  path("consulReserveDay/", consulReserveDayView),
  path("reserve/", reserveView),
]