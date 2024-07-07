from django.contrib import admin
from .models import Location, Category, Room, RoomImage

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage)
