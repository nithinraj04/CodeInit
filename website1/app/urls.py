
from django.urls import path,include
from app import views
urlpatterns = [
   path('',views.home,name='home'),path('working',views.work,name='working'),path('signupboiler',views.signup,name='signup')
]
