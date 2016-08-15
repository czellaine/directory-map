from django.contrib import admin

from .models import *

admin.site.register(Author)
admin.site.register(CallNumber)
admin.site.register(Title)
admin.site.register(Book)
admin.site.register(Location)
admin.site.register(Item)