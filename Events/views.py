from django.shortcuts import render
from .models import User
from .models import Event


# Create your views here.
def home(request):
    all_place = Event.objects.all()
    return render(request, 'home.html',{
        'tour':all_place
    })
    
def participants(request):
    all_attendees = User.objects.all()
    return render(request, 'participants.html',{
        'out':all_attendees
    })