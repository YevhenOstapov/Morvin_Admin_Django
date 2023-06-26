from django.shortcuts import render
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ComponentsView(LoginRequiredMixin, View):
    pass

# base-ui

ui_elements_alerts_view = ComponentsView.as_view( _name = "components/ui-elements/ui-alerts.html")
ui_elements_buttons_view = ComponentsView.as_view( _name = "components/ui-elements/ui-buttons.html")
ui_elements_colors_view = ComponentsView.as_view( _name = "components/ui-elements/ui-colors.html")
ui_elements_cards_view = ComponentsView.as_view( _name = "components/ui-elements/ui-cards.html")
ui_elements_carousel_view = ComponentsView.as_view( _name = "components/ui-elements/ui-carousel.html")
ui_elements_dropdowns_view = ComponentsView.as_view( _name = "components/ui-elements/ui-dropdowns.html")
ui_elements_grid_view = ComponentsView.as_view( _name = "components/ui-elements/ui-grid.html")
ui_elements_lightbox_view = ComponentsView.as_view( _name = "components/ui-elements/ui-lightbox.html")
ui_elements_images_view = ComponentsView.as_view( _name = "components/ui-elements/ui-images.html")
ui_elements_tabs_view = ComponentsView.as_view( _name = "components/ui-elements/ui-tabs.html")
ui_elements_modals_view = ComponentsView.as_view( _name = "components/ui-elements/ui-modals.html")
ui_elements_progressbars_view = ComponentsView.as_view( _name = "components/ui-elements/ui-progressbars.html")
ui_elements_range_slider_view = ComponentsView.as_view( _name = "components/ui-elements/ui-rangeslider.html")
ui_elements_session_timeout_view = ComponentsView.as_view( _name = "components/ui-elements/ui-session-timeout.html")
ui_elements_sweet_alerts_view = ComponentsView.as_view( _name = "components/ui-elements/ui-sweet-alert.html")
ui_elements_tab_accordions_view = ComponentsView.as_view( _name = "components/ui-elements/ui-tabs-accordions.html")
ui_elements_video_view = ComponentsView.as_view( _name = "components/ui-elements/ui-video.html")
ui_elements_typography_view = ComponentsView.as_view( _name = "components/ui-elements/ui-typography.html")
ui_elements_general_view = ComponentsView.as_view( _name = "components/ui-elements/ui-general.html")
ui_elements_rating_view = ComponentsView.as_view( _name = "components/ui-elements/ui-rating.html")


# forms
forms_elements_view = ComponentsView.as_view( _name = "components/forms/form-elements.html")
forms_masks_view = ComponentsView.as_view( _name = "components/forms/form-mask.html")
forms_advanced_view = ComponentsView.as_view( _name = "components/forms/form-advanced.html")
forms_validation_view = ComponentsView.as_view( _name = "components/forms/form-validation.html")
forms_wizard_view = ComponentsView.as_view( _name = "components/forms/form-wizard.html")
forms_editors_view = ComponentsView.as_view( _name = "components/forms/form-editors.html")
forms_uploads_view = ComponentsView.as_view( _name = "components/forms/form-uploads.html")
forms_xeditable_view = ComponentsView.as_view( _name = "components/forms/form-xeditable.html")


# charts
charts_apex_view = ComponentsView.as_view( _name = "components/charts/charts-apex.html")
charts_chartist_view = ComponentsView.as_view( _name = "components/charts/charts-chartist.html")
charts_chartjs_view = ComponentsView.as_view( _name = "components/charts/charts-chartjs.html")
charts_flot_view = ComponentsView.as_view( _name = "components/charts/charts-flot.html")
charts_knob_view = ComponentsView.as_view( _name = "components/charts/charts-knob.html")
charts_sparkline_view = ComponentsView.as_view( _name = "components/charts/charts-sparkline.html")

# tables
tables_basic_view = ComponentsView.as_view( _name = "components/tables/tables-basic.html")
tables_datatables_view = ComponentsView.as_view( _name = "components/tables/tables-datatable.html")
tables_editable_view = ComponentsView.as_view( _name = "components/tables/tables-editable.html")
tables_responsive_view = ComponentsView.as_view( _name = "components/tables/tables-responsive.html")

# icons
icons_materialdesign_view = ComponentsView.as_view( _name = "components/icons/icons-materialdesign.html")
icons_dripicons_view = ComponentsView.as_view( _name = "components/icons/icons-dripicons.html")
icons_fontawesome_view = ComponentsView.as_view( _name = "components/icons/icons-fontawesome.html")
icons_themify_view = ComponentsView.as_view( _name = "components/icons/icons-themify.html")


# maps
maps_google_view = ComponentsView.as_view( _name = "components/maps/maps-google.html")
maps_vector_view = ComponentsView.as_view( _name = "components/maps/maps-vector.html")

