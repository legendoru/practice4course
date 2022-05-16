from select import select
from empty.models import Emptys
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")


@csrf_exempt
def create(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    service = request.POST.get("select-service", "")
    time = request.POST.get("select-time", "")
    msg = request.POST.get("message", "")
    obj = Emptys(name = name, email = email, service = service, time = time, msg = msg)
    obj.save()
    return redirect("index")


class List(generic.ListView):
    model = Emptys
    paginate_by = 5
    template_name = "list.html"


