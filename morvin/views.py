from django.shortcuts import render
from django.views.generic import  View 
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MyPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    success_url = reverse_lazy("dashboards:dashboard")


class MyPasswordSetView(LoginRequiredMixin,PasswordSetView):
    success_url = reverse_lazy("dashboards:dashboard")

class DashboardView(LoginRequiredMixin, View):
    pass

dashboard_view = DashboardView.as_view( _name = "index.html")
calendar_view = DashboardView.as_view( _name = "calendar.html")
chat_view = DashboardView.as_view( _name = "chat.html")
        