from django.contrib import admin

from congratulation.models import Customer, Details

class DetailsInLine(admin.TabularInline):
    model = Details
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    fields = ['last_name', 'first_name', 'mobile', 'user_id']
    inlines = [DetailsInLine]
    list_filter = ['last_name']
    search_fields = ['=first_name', '=last_name'] 
    list_per_page = 50
    show_full_result_count = False

admin.site.register(Customer, CustomerAdmin)