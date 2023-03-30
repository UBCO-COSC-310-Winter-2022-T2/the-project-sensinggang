from django.template import loader
from django.http import HttpResponse

def sensingGang(request):
    template = loader.get_template('masterTemplate.html')
    return HttpResponse(template.render())
