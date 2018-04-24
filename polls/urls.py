#from django.conf.urls import url

#from . import views

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#]

# howdy/urls.py
from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
