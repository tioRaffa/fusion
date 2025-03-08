from django.urls import path
from .views import IndexView, NotFoundView

app_name = 'fusion'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('not_found/404', NotFoundView.as_view(), name='not_found')
]
