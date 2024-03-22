from django.contrib import admin

# Register your models here.

from .models import Pet , Adoption_status , user 

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age', 'adoption_status')

class Adoption_statusAdmin(admin.ModelAdmin):
    list_display = ('status', 'adopted_by', 'adoption_date', 'notes')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'work', 'phone_number', 'email')

class volunteer(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'free_hours_a_week', 'exprtise')


admin.site.register(Pet, PetAdmin)
admin.site.register(Adoption_status, Adoption_statusAdmin)
admin.site.register(user, UserAdmin)
