
from django.urls import path
from components.views import (
    
    # bootstrap-ui
    ui_elements_alerts_view,
    ui_elements_buttons_view,
    ui_elements_colors_view,
    ui_elements_cards_view,
    ui_elements_carousel_view,
    ui_elements_dropdowns_view,
    ui_elements_grid_view,
    ui_elements_images_view,
    ui_elements_lightbox_view,
    ui_elements_tabs_view,
    ui_elements_modals_view,
    ui_elements_range_slider_view,
    ui_elements_session_timeout_view,
    ui_elements_progressbars_view,
    ui_elements_tab_accordions_view,
    ui_elements_sweet_alerts_view,
    ui_elements_typography_view,
    ui_elements_video_view,
    ui_elements_general_view,
    ui_elements_rating_view,
    
    # forms
    forms_elements_view,
    forms_masks_view,
    forms_advanced_view,
    forms_validation_view,
    forms_wizard_view,
    forms_editors_view,
    forms_uploads_view,
    forms_xeditable_view,

    # charts
    charts_apex_view,
    charts_chartist_view,
    charts_chartjs_view,
    charts_flot_view,
    charts_knob_view,
    charts_sparkline_view,
    
    # table
    tables_basic_view,
    tables_datatables_view,
    tables_editable_view,
    tables_responsive_view,
    
    # icons
    icons_materialdesign_view,
    icons_dripicons_view,
    icons_fontawesome_view,
    icons_themify_view,

    # maps
    maps_google_view,
    maps_vector_view,
   
)

app_name ='components'

urlpatterns = [
    
    # bootstrap-ui
    path('ui-elements/alerts',view=ui_elements_alerts_view,name="ui-elements.alerts"),
    path('ui-elements/buttons',view=ui_elements_buttons_view,name="ui-elements.buttons"),
    path('ui-elements/colors',view=ui_elements_colors_view,name="ui-elements.colors"),
    path('ui-elements/cards',view=ui_elements_cards_view,name="ui-elements.cards"),
    path('ui-elements/carousel',view=ui_elements_carousel_view,name="ui-elements.carousel"),
    path('ui-elements/dropdowns',view=ui_elements_dropdowns_view,name="ui-elements.dropdowns"),
    path('ui-elements/grid',view=ui_elements_grid_view,name="ui-elements.grid"),
    path('ui-elements/images',view=ui_elements_images_view,name="ui-elements.images"),
    path('ui-elements/lightbox',view=ui_elements_lightbox_view,name="ui-elements.lightbox"),
    path('ui-elements/tabs',view=ui_elements_tabs_view,name="ui-elements.tabs"),
    path('ui-elements/modals',view=ui_elements_modals_view,name="ui-elements.modals"),
    path('ui-elements/range_slider',view=ui_elements_range_slider_view,name="ui-elements.range_slider"),
    path('ui-elements/session_timeout',view=ui_elements_session_timeout_view,name="ui-elements.session_timeout"),
    path('ui-elements/progress',view=ui_elements_progressbars_view,name="ui-elements.progressbars"),
    path('ui-elements/sweet_alert',view=ui_elements_sweet_alerts_view,name="ui-elements.sweet_alert"),
    path('ui-elements/accordions',view=ui_elements_tab_accordions_view,name="ui-elements.tabs_accordions"),
    path('ui-elements/typography',view=ui_elements_typography_view,name="ui-elements.typography"),
    path('ui-elements/video',view=ui_elements_video_view,name="ui-elements.video"),
    path('ui-elements/general',view=ui_elements_general_view,name="ui-elements.general"),
    path('ui-elements/rating',view=ui_elements_rating_view,name="ui-elements.rating"),
  
    # forms
    path('forms/elements',view=forms_elements_view,name="forms.elements"),
    path('forms/masks',view=forms_masks_view,name="forms.masks"),
    path('forms/advanced',view=forms_advanced_view,name="forms.advanced"),
    path('forms/validation',view=forms_validation_view,name="forms.validation"),
    path('forms/wizard',view=forms_wizard_view,name="forms.wizard"),
    path('forms/editors',view=forms_editors_view,name="forms.editors"),
    path('forms/uploads',view=forms_uploads_view,name="forms.uploads"),
    path('forms/xeditable',view=forms_xeditable_view,name="forms.xeditable"),

    #  charts
    path('charts/apex',view=charts_apex_view,name="charts.apex"),
    path('charts/chartist',view=charts_chartist_view,name="charts.chartist"),
    path('charts/chartjs',view=charts_chartjs_view,name="charts.chartjs"),
    path('charts/flot',view=charts_flot_view,name="charts.flot"),
    path('charts/knob',view=charts_knob_view,name="charts.knob"),
    path('charts/sparkline',view=charts_sparkline_view,name="charts.sparkline"),

    # tables
    path('tables/basic',view=tables_basic_view,name="tables.basic"),
    path('tables/datatables',view=tables_datatables_view,name="tables.datatables"),
    path('tables/editable',view=tables_editable_view,name="tables.editable"),
    path('tables/responsive',view=tables_responsive_view,name="tables.responsive"),
    
    # icons
    path('icons/materialdesign',view=icons_materialdesign_view,name="icons.materialdesign"),
    path('icons/dripicons',view=icons_dripicons_view,name="icons.dripicons"),
    path('icons/fontawesome',view=icons_fontawesome_view,name="icons.fontawesome"),
    path('icons/themify',view=icons_themify_view,name="icons.themify"),
    
    # maps
    path('maps/google',view=maps_google_view,name="maps.google"),
    path('maps/vector',view=maps_vector_view,name="maps.vector"),

    
]