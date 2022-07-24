from django.urls import path
from .views import homePageView
#from . import views

urlpatterns = [
    path('', homePageView, name = 'home'),
    #views.homePageView()
]