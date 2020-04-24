from django.contrib import admin

from .models import MobileApp,WorkDetail,Service,AboutService

admin.site.register(MobileApp)
admin.site.register(WorkDetail)
admin.site.register(Service)
admin.site.register(AboutService)