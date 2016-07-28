from django.conf.urls import url

from .views import UrlView, UrlRequestView, UrlCreateView


urlpatterns = [
    url(r'^(?P<id>\w+)$', UrlRequestView.as_view(), name='short'),
    url(r'^create/$', UrlCreateView.as_view(), name='create'),
]
