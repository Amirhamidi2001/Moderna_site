from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('newsletter', newsletter_view, name='newsletter'),
    path('portfolio', portfolio_view, name='portfolio'),
    path('details', details, name='details'),
    path('services', services_view, name='services'),
    path('team', team_view, name='team'),
]
