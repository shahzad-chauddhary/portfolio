from django.contrib import admin

from .models import MobileApp,WorkDetail,Service,AboutService,About,AboutTestimonial

admin.site.register(MobileApp)
admin.site.register(WorkDetail)
admin.site.register(Service)
admin.site.register(AboutService)
admin.site.register(About)
admin.site.register(AboutTestimonial)