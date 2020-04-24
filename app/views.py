from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import MobileApp,WorkDetail,Service,AboutService


class Home(TemplateView):
	template_name = 'app/index.html'




class About(TemplateView):
	template_name = 'app/about.html'



class Portfolio_work(ListView):
    template_name = 'app/portfolio-work.html'
    queryset = MobileApp.objects.all()
    context_object_name = 'album'

class Work_details(ListView):
    template_name = 'app/work_details.html'
    queryset = WorkDetail.objects.all()
    context_object_name = 'obj'


class Services(ListView):
    template_name = 'app/services.html'
    queryset = Service.objects.all()
    def get_context_data(self, **kwargs):
        context = super(Services,self).get_context_data(**kwargs)
        context['service'] = Service.objects.all()
        context['about'] = AboutService.objects.all()

        return context




class Elements(TemplateView):
    template_name = 'app/elements.html'


class Contact(TemplateView):
    template_name = 'app/contact.html'

class Blog(TemplateView):
    template_name = 'app/blog.html'

class Single_blog(TemplateView):
    template_name = 'app/single-blog.html'
