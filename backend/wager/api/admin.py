from django.contrib import admin
from .models import User,Tag,Bed,Game,BedWay

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,PostAdmin)
admin.site.register(Tag,PostAdmin)
admin.site.register(Bed,PostAdmin)
admin.site.register(Game,PostAdmin)
admin.site.register(BedWay,PostAdmin)