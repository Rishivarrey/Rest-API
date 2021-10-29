"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from myapp import views

urlpatterns = [
            path('admin/advisor', views.advisor_list),

            path('user/register', views.user_register),

            path('user/login', views.user_login),
            path('user/<int:user_id>/advisor', views.useradvisor_list),

            path('user/<int:user_id>/advisor/<int:advisor_id>', views.bookingtime),
            path('user/<int:user_id>/advisor/booking', views.getallbookedadivsorlist)
]



