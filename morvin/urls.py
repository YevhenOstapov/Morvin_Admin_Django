"""
URL configuration for morvin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from morvin.views import (
    dashboard_view,
    calendar_view,
    chat_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',view=dashboard_view,name='dashboard'),
    path('calendar/',view=calendar_view,name='calendar'),
    path('chat/',view=chat_view,name='chat'),
    
    # ecommerce
    path('ecommerce/',include('ecommerce.urls')),
    
    # e_mail
    path('e_mail/',include('e_mail.urls')),
    
    # components
    path('components/',include('components.urls')),
    
    # extras
    path('extras/',include('extras.urls')),
    
    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
    # All Auth 
    path('account/', include('allauth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
