from django.template import loader
from django.http import HttpResponse

def homePage(request):
    template = loader.get_template('homePageTemplate.html')
    return HttpResponse(template.render())
