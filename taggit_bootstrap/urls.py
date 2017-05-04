from django.conf.urls import url
from .views import *

urlpatterns = [
    url(
        regex=r'^$',
        view=TaggitBootstrapView.as_view(),
        name='taggit-bootstrap'
    )
]

