from django.urls import path
from extras.views import (
    
    # layouts
        # vertical
    vertical_dark_sidebar,
    vertical_compact_sidebar,
    vertical_icon_sidebar,
    vertical_boxed_layout,
    vertical_preloader,
    
        # horizontal
    horizontal_layout,
    horizontal_light_topbar,
    horizontal_hori_boxed_width,
    horizontal_hori_preloader,
    horizontal_hori_colored_header,
    
    
    # authentication
    auth_login,
    auth_register,
    auth_recover_password,
    auth_lock_screen,
    
    # pages
    pages_timeline,
    pages_invoice,
    pages_blank_page,
    pages_error404,
    pages_error500,
    pages_pricing,
    pages_maintenance,
    pages_comingsoon,
    pages_faqs,
)

app_name = 'extras'

urlpatterns = [
    
    # layouts
        # vertical
    path('layouts/vertical/dark_sidebar',view=vertical_dark_sidebar,name='layouts.vertical.dark_sidebar'),
    path('layouts/vertical/compact_sidebar',view=vertical_compact_sidebar,name='layouts.vertical.compact_sidebar'),
    path('layouts/vertical/icon_sidebar',view=vertical_icon_sidebar,name='layouts.vertical.icon_sidebar'),
    path('layouts/vertical/boxed_layout',view=vertical_boxed_layout,name='layouts.vertical.boxed_layout'),
    path('layouts/vertical/preloader',view=vertical_preloader,name='layouts.vertical.preloader'),
    
        # horizontal
    path('layouts/horizontal/horizontal_layout',view=horizontal_layout,name='layouts.horizontal.horizontal_layout'),
    path('layouts/horizontal/light_topbar',view=horizontal_light_topbar,name='layouts.horizontal.light_topbar'),
    path('layouts/horizontal/hori_boxed_width',view=horizontal_hori_boxed_width,name='layouts.horizontal.hori_boxed_width'),
    path('layouts/horizontal/hori_preloader',view=horizontal_hori_preloader,name='layouts.horizontal.hori_preloader'),
    path('layouts/horizontal/hori_colored_header',view=horizontal_hori_colored_header,name='layouts.horizontal.hori_colored_header'),
    
    
    
    # authentications
    path('authentications/login',view=auth_login,name='authentications.login'),
    path('authentications/register',view=auth_register,name='authentications.register'),
    path('authentications/recover_password',view=auth_recover_password,name='authentications.recover_password'),
    path('authentications/lock_screen',view=auth_lock_screen,name='authentications.lock_screen'),
    
    # pages
    path('pages/timeline',view=pages_timeline,name='pages.timeline'),
    path('pages/invoice',view=pages_invoice,name='pages.invoice'),
    path('pages/blank_page',view=pages_blank_page,name='pages.blank_page'),
    path('pages/error404',view=pages_error404,name='pages.error404'),
    path('pages/error500',view=pages_error500,name='pages.error500'),
    path('pages/pricing',view=pages_pricing,name='pages.pricing'),
    path('pages/maintenance',view=pages_maintenance,name='pages.maintenance'),
    path('pages/comingsoon',view=pages_comingsoon,name='pages.comingsoon'),
    path('pages/faqs',view=pages_faqs,name='pages.faqs'),
    
    
]
