from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'IdCardNo','balance', 'first_name']
    list_editable = ['balance']
    
    search_fields = ['balance', ]
    def first_name(self, x):
        return (x.user.first_name + " " + x.user.last_name)
    
    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)
# Register your models here.
