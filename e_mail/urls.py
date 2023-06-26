from django.urls import path
from e_mail.views import (
    
    email_inbox_view,
    email_read_view,
    email_compose_view,
    
)

app_name = 'e_mail'

urlpatterns = [
    
    path('email_inbox',view=email_inbox_view,name='email_inbox'),
    path('email_read',view=email_read_view,name='email_read'),
    path('email_compose',view=email_compose_view,name='email_compose'),
]
