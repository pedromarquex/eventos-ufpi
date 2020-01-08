from django.urls import path
from .views import Login

app_name = 'core'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
]
