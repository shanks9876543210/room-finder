from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Room, Category, Location, RoomImage
from .forms import RoomForm, CategoryForm, LocationForm

def room_list(request):
    rooms = Room.objects.filter(availability=True)
    locations = Location.objects.all()

    context = {
        'rooms': rooms,
        'locations': locations,
    }
    return render(request, 'room_list.html', context)

class RoomsByCategoryView(ListView):
    model = Room
    template_name = 'rooms_by_category.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Room.objects.filter(category_id=category_id, availability=True)

class RoomsByLocationView(ListView):
    model = Room
    template_name = 'rooms_by_location.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Room.objects.filter(location_id=location_id, availability=True)

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'

@user_passes_test(lambda u: u.is_staff)
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            for image in request.FILES.getlist('images'):
                RoomImage.objects.create(room=room, image=image)
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = LocationForm()
    return render(request, 'add_location.html', {'form': form})

@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.user.is_staff:
        room.delete()
    return redirect('room_list')

def contact_view(request):
    return render(request, 'contact.html')

def navbar(request):
    return render(request, 'navbar.html')

def locations_list(request):
    locations = Location.objects.all()
    return render(request, 'locations_list.html', {'locations': locations})

class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'room_form.html'
    success_url = '/'

    def form_valid(self, form):
        room = form.save()
        for image in self.request.FILES.getlist('images'):
            RoomImage.objects.create(room=room, image=image)
        return super().form_valid(form)
