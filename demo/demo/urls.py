from django.conf.urls import url,include
from django.conf import settings
from django.views import static

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATICFILES_DIRS}, name='static'),
    url(r'^',include('poll.urls'))
]
