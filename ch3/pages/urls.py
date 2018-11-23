from django.urls import path

from .views import AboutPageView, HomePageView, MojaStronka

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('strona/', MojaStronka.as_view(), name='strona')
]
