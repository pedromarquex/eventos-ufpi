from django.urls import path
from .views import Login, Logout, index

app_name = 'core'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('', index, name='index'),
    path('logout', Logout.as_view(), name='logout'),
]
