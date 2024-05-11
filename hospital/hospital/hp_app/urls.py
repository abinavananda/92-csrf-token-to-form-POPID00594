
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('abot/',views.about,name='about'),
   path('booking/',views.booking,name='booking'),
   path('contact/',views.contact,name='contact'),
   path('department/',views.department,name='department'),
   path('doctor/',views.doctor,name='doctor')
]
