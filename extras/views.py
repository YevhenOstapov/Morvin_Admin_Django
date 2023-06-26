from django.shortcuts import render
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ExtrasView(LoginRequiredMixin, View):
    pass
 
# layouts
    # vertical 
vertical_dark_sidebar = ExtrasView.as_view( _name="extras/layouts/vertical/layouts-dark-sidebar.html")
vertical_compact_sidebar = ExtrasView.as_view( _name="extras/layouts/vertical/layouts-compact-sidebar.html")
vertical_icon_sidebar = ExtrasView.as_view( _name="extras/layouts/vertical/layouts-icon-sidebar.html")
vertical_boxed_layout = ExtrasView.as_view( _name="extras/layouts/vertical/layouts-boxed.html")
vertical_preloader = ExtrasView.as_view( _name="extras/layouts/vertical/layouts-preloader.html")

    # horizontal
horizontal_layout = ExtrasView.as_view( _name="extras/layouts/horizontal/layouts-horizontal.html")
horizontal_light_topbar = ExtrasView.as_view( _name="extras/layouts/horizontal/layouts-hori-topbar-light.html")
horizontal_hori_boxed_width = ExtrasView.as_view( _name="extras/layouts/horizontal/layouts-hori-boxed-width.html")
horizontal_hori_preloader = ExtrasView.as_view( _name="extras/layouts/horizontal/layouts-hori-preloader.html")
horizontal_hori_colored_header = ExtrasView.as_view( _name="extras/layouts/horizontal/layouts-hori-colored-header.html")
    

# authentications
auth_login = ExtrasView.as_view( _name="extras/authentications/auth-login.html")
auth_register = ExtrasView.as_view( _name="extras/authentications/auth-register.html")
auth_recover_password = ExtrasView.as_view( _name="extras/authentications/auth-recoverpw.html")
auth_lock_screen = ExtrasView.as_view( _name="extras/authentications/auth-lock-screen.html")

# pages
pages_timeline = ExtrasView.as_view( _name="extras/pages/pages-timeline.html")
pages_invoice = ExtrasView.as_view( _name="extras/pages/pages-invoice.html")
pages_blank_page = ExtrasView.as_view( _name="extras/pages/pages-blank.html")
pages_error404 = ExtrasView.as_view( _name="extras/pages/pages-404.html")
pages_error500 = ExtrasView.as_view( _name="extras/pages/pages-500.html")
pages_pricing = ExtrasView.as_view( _name="extras/pages/pages-pricing.html")
pages_maintenance = ExtrasView.as_view( _name="extras/pages/pages-maintenance.html")
pages_comingsoon = ExtrasView.as_view( _name="extras/pages/pages-comingsoon.html")
pages_faqs = ExtrasView.as_view( _name="extras/pages/pages-faq.html")
