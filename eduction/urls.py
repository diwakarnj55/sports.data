from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("classes",views.classes,name="classes"),
    path("contact",views.contact,name="contact"),
    path("404",views.html,name="404"),
    path("appointment",views.appointment,name="appointment"),
    path("call-to-action",views.calltoaction,name="call-to-action"),
    path("facility",views.facility,name="facility"),
    path("team",views.team,name="team"),
    path("testimonial",views.testimonial,name="testimonial"),
]

