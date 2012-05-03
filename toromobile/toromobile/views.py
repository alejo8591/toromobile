from django.template import Context
from django.template.loader import get_template
from django.http import Http404, HttpResponse
import datetime
       
def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('index.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
