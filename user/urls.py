from django.urls import path
from.views import *


urlpatterns=[
    path('items/',item_list),
    path('user/',user_auth),
]