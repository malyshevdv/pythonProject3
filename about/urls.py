from django.urls import path
from .views import showAnswer, AboutClass, MyProfile
#from . import views

urlpatterns = [
    #path('', showAnswer, name = 'about'),
    path('', AboutClass.as_view(), name='about'),
    path('profile/', MyProfile.as_view(), name='profile'),

    #views.homePageView()
]