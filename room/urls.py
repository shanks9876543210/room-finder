from django.urls import path
from .views import (
    room_list,
    RoomsByCategoryView,
    RoomsByLocationView,
    RoomDetailView,
    add_room,
    add_category,
    add_location,
    contact_view,
    delete_room,
    RoomUpdateView,
    locations_list
)


urlpatterns = [
    path('list/', room_list, name='room_list'),
    path('category/<int:category_id>/', RoomsByCategoryView.as_view(), name='rooms_by_category'),
    path('location/<int:location_id>/', RoomsByLocationView.as_view(), name='rooms_by_location'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('add_room/', add_room, name='add_room'),
    path('add_category/', add_category, name='add_category'),
    path('add_location/', add_location, name='add_location'),
    path('contact/', contact_view, name='contact'),
    path('delete_room/<int:room_id>/', delete_room, name='delete_room'),
     path('<int:pk>/edit/', RoomUpdateView.as_view(), name='room_edit'),
    path('locations/', locations_list, name='locations_list'),
    
]
