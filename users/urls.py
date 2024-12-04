from django.urls import path,include


from . import views


urlpatterns=[
    path ('',views.home, name="home"),
    path("signup/",views.signup, name="signup"),
    path("logout/",views.logout_user, name="logout"),
     path('accounts/',include('allauth.urls')),

]