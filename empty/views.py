from multiprocessing import context
from select import select
from ssl import AlertDescription
from empty.models import Emptys, Review
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def reviews(request):
    reviews = Review.objects.all() 
    if len(reviews)>11: 
        reviews = reviews[len(reviews):len(reviews)-10:-1]
    return render(request, "reviews.html", context = {'reviews': reviews})

@csrf_exempt
def create(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    service = request.POST.get("select-service", "")
    time = request.POST.get("select-time", "")
    msg = request.POST.get("message", "")
    if not name or not email:
        return redirect("index")
    obj = Emptys(name = name, email = email, service = service, time = time, msg = msg)
    obj.save()
    return redirect("index")

@csrf_exempt
def createreviews(request):
    name_r = request.POST.get("name_reviews", "")
    email_r = request.POST.get("email_reviews", "")
    msg_r = request.POST.get("message_reviews", "")
    if not name_r or not email_r or not msg_r:
        return redirect("reviews")
    obj = Review(name_reviews = name_r, email_reviews = email_r, msg_reviews = msg_r)
    obj.save()
    return redirect("reviews")


class List(generic.ListView):
    model = Emptys
    paginate_by = 5
    template_name = "list.html"


