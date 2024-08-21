from django.contrib import admin
from django.urls import path
from app02 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', views.salom),
    path('bitta_muallif/<int:son>/', views.bitta_muallif),
    path('kitob/', views.kitob),
    path('muallif/', views.muallif),
    path('record/', views.record),
    path('muallif_true/', views.muallif_true),
    path('Muallif/', views.Muallif),
    path('Muallif_ochir/<int:son>', views.ochir),
    path('Todo/', views.todo),

]
