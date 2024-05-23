from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def classes(request):
    return  render(request,"classes.html")
def contact(request):
    return  render(request,"contact.html")
def html(request):
    return  render(request,"404.html")
def appointment(request):
    return  render(request,"appointment.html")
def calltoaction(request):
    return  render(request,"call-to-action.html")
def facility(request):
    return  render(request,"facility.html")
def team(request):
    return  render(request,"team.html")
def testimonial(request):
    return  render(request,"testimonial.html")



