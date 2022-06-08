
from django.contrib import admin
from django.urls import path
from one import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls,name='a'),
    path('',views.home,name='home'),
    path('logout/',views.logoutUser,name='logout'),
    path('salons/',views.salons,name='salons'),
    path('salonReg/',views.salonReg,name='salonReg'),
    path('clientReg/',views.clientReg,name='clientReg'),
    path('salon/<str:id>/',views.sinlgeSalonView,name='salon'),
    path('salonowner/',views.salonOwner,name='SalonOwner'),
    path('service/',views.service,name='service'),
    path('delete_appoint_service',views.deleteAppointmentServices,name='appoint_service_delete'),
    path('update_status',views.update_status,name='update_status'),
    path('delete_service',views.delete_service,name='delete_service'),
    path('search/',views.search_salon,name='search'),
    path('reset_search/',views.reset_search,name='reset_search'),
    path('service_cart/',views.service_cart,name='service_cart'),
    path('make_appoint/',views.make_appoint,name='make_appoint'),
    path('t/',views.t,name='t'),
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
    
]