from django.shortcuts import render, get_object_or_404
from .models import Belt, Technique

def belt_list(request):
    belts = Belt.objects.all().order_by('id')
    return render(request, 'belts/belt_list.html', {'belts': belts})

def technique_list(request, belt_id):
    belt = get_object_or_404(Belt, id=belt_id)
    techniques = belt.techniques.all()  # uses related_name='techniques'
    return render(request, 'belts/technique_list.html', {
        'belt': belt,
        'techniques': techniques,
    })
def home(request):
    belts = Belt.objects.all().order_by('id')
    return render(request, 'belts/home.html', {'belts': belts})

def day1_view(request):
    # Get White Belt (pk=1 or filter by name='White')
    white_belt = Belt.objects.get(name='White')
    # In real usage, you might also filter by day=1 if you introduced that field
    techniques = Technique.objects.filter(belt=white_belt)
    return render(request, 'belts/day1_white.html', {
        'belt': white_belt,
        'techniques': techniques,
    })