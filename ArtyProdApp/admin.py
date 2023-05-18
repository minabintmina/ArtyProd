from django.contrib import admin
from .models import SignUp, Services, Personnel, Team, Project, Contact


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('label', 'get_services', 'description', 'start_date', 'end_date', 'status', 'team')

    def get_services(self, obj):
        return ", ".join([service.TypeS for service in obj.service.all()])

    get_services.short_description = 'Services'


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('TypeS', 'description')


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_services', 'experience', 'linkedln_link')

    def get_services(self, obj):
        return ", ".join([service.TypeS for service in obj.service.all()])


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('get_personnel',)

    def get_personnel(self, obj):
        return ", ".join([personnel.name for personnel in obj.personnel.all()])


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
