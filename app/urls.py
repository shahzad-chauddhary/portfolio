from . import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [

    # path('',views.Image,name=''),
    path('index',views.Home.as_view(),name='index'),
    path('about', views.About.as_view(), name='about'),
    path('portfolio-work', views.Portfolio_work.as_view(), name='portfolio_work'),
    path('work_details', views.Work_details.as_view(), name='work_details'),
    path('services', views.Services.as_view(), name='services'),
    path('elements', views.Elements.as_view(), name='elements'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('blog',views.Blog.as_view(),name='blog'),
    path('single_blog',views.Single_blog.as_view(),name='single_blog'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)