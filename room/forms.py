from django import forms
from .models import Room, Category, Location

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description', 'location', 'category', 'price_per_month', 'availability']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description']
