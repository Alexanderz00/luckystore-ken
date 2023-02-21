from django.contrib import admin
from .models import Contact
from .models import *
# Register your models here.


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id','name','email','contact_date')
  list_display_links = ('id','name')
  search_fields = ('name','title',)
  list_per_page = 25


admin.site.register(Contact, ContactAdmin)
