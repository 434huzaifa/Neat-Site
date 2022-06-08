from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

# Register your models here.


# admin.site.register(models.client)
# admin.site.register(models.salon)
@admin.register(models.client)
class clientView(admin.ModelAdmin):
    list_display = ('cl_name',)


@admin.register(models.salon)
class salonVeiw(admin.ModelAdmin):
    list_display = ('sal_name', 'sal_adr')

@admin.register(models.services)
class serviceView(admin.ModelAdmin):
    list_display=('s_name','s_price','s_salon')
    

@admin.register(models.apointment)
class appointmentView(admin.ModelAdmin):
    list_display=('id','a_salon','a_client')

@admin.register(models.cart)
class cartView(admin.ModelAdmin):
    list_display=('id','c_salon','c_client')