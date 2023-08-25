from django.contrib import admin
from .models import Automobilio_modelis, Automobilis, Uzsakymas, UzsakymoEilute, Paslauga
class UzsakymoEilutesInline(admin.TabularInline):
    model = UzsakymoEilute

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('automobilis_id', 'klientas_id', 'data', 'status', 'suma')
    inlines = [UzsakymoEilutesInline]


@admin.register(Automobilis)
class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('savininkas', 'automobilio_modelis_id', 'valstybinis_numeris', 'vin_kodas')
    list_editable = ('valstybinis_numeris', 'vin_kodas')
    list_filter = ('savininkas', 'automobilio_modelis_id')
    search_fields = ('valstybinis_numeris', 'vin_kodas')
    list_display_links = ('savininkas',)



@admin.register(Paslauga)
class Paslaugos(admin.ModelAdmin):
    list_display = ('name', 'kaina')


admin.site.register(Automobilio_modelis)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute)