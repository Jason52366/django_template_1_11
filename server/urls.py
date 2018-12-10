from django.conf.urls import url, include
from django.views.static import serve
from server import settings

urlpatterns = [
    # url(r'^appname/', include('appname.urls')),
    url(r'^sample_app/', include('sample_app.urls')),
]

# Static Url Setting
if not settings.DEBUG:
    urlpatterns += [url(r'^static/(?P<path>.*)$',
                    serve,
                    {'document_root': settings.STATIC_ROOT})]
