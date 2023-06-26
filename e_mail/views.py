from django.shortcuts import render
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class EmailView(LoginRequiredMixin, View):
    pass

email_inbox_view = EmailView.as_view( _name = "e_mail/email-inbox.html")
email_read_view = EmailView.as_view( _name = "e_mail/email-read.html")
email_compose_view = EmailView.as_view( _name = "e_mail/email-compose.html")

