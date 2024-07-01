from django.contrib import admin
from .models import MandatoAporte
# Register your models here.


class MandatoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_inicio", )

admin.site.register(MandatoAporte, MandatoAdmin)