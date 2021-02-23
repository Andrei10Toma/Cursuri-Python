from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Motherboard)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(MemoryRAM)
admin.site.register(Storage)
admin.site.register(Computer)
