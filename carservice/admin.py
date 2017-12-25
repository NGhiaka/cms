from django.contrib import admin

# Register your models here.
from .models import User, Schedule, Cost, Album, Photo

admin.site.register(User)
admin.site.register(Schedule)
admin.site.register(Cost)
admin.site.register(Album)
admin.site.register(Photo)
