from django.urls import path
from Userdata.apis.views import *

app_name = 'UserData APIs'

urlpatterns = [
   path('signUp/', user_auth_api.as_view()),
   path('content/',content_view_api.as_view()),
   path('wallet/',wallet_view_api.as_view()),
   path('wallet/<id>',wallet_view_api.as_view()),
]
