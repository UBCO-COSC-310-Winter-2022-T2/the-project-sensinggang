# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader


# Create your views here.
# def graphsDisplay(request):
#     template = loader.get_template('base.html')
#     return HttpResponse(template.render())

# views.py
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from .models import SensorData

def sensor_data(request):
    # Get the temperature data from the database
    temperature_data = SensorData.objects.values_list('timestamp', 'temperature')
    
    # Generate a simple line graph of the temperature data using matplotlib
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plot([t[0] for t in temperature_data], [t[1] for t in temperature_data])
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    
    # Embed the graph in the HTML template
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
