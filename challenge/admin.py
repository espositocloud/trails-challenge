from django.contrib import admin
from .models import Group, Patrol, Technique, Test


#@admin.register()
#class MyAdminSite(admin.AdminSite):
#    site_header = 'Trails Challenge administration'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    list_display = ('name',)


@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'staff',
        'person_name',
        'radio_id',
        'phone',
        'note',
        'check_condition',
    )
    list_filter = [
        'check_condition',
    ]


@admin.register(Patrol)
class PatrolAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'group',
        'hour_condition',
    )
    list_filter = [
        'hour_condition',
        'group',
    ]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):

    fields = (
        'patrol',
        'technique',
        'technique_score',
        'style_score',
    )
    list_display = (
        'patrol',
        'technique',
        'technique_score',
        'style_score',
        'created_date_hms',
        'modified_date_hms',
        'user',
    )
    list_filter = [
        'patrol',
        'technique',
        'technique_score',
        'style_score',
        'created_date',
        'modified_date',
        'user',
    ]
    radio_fields = {
        'patrol': admin.HORIZONTAL,
        'technique': admin.VERTICAL,
    }

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user.username
        obj.save()
