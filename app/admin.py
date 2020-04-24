from django.contrib import admin

from .models import MobileApp,WorkDetail,Service,ServiceB

admin.site.register(MobileApp)
admin.site.register(WorkDetail)
admin.site.register(Service)
admin.site.register(ServiceB)