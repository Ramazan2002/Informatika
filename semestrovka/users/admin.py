from django.contrib import admin
from .models import CustomUser, UserProfile, Group
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in obj._meta.fields if not f.editable]

admin.site.register(UserProfile, MyModelAdmin)
admin.site.register(CustomUser, MyModelAdmin)
admin.site.register(Group)