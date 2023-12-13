# projects/admin.py

from django.contrib import admin
from projects.models import Project
from personal_portfolio.admin import *

class database(admin.ModelAdmin):
    using = "default"
    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)
    def delete_model(self, request, obj):
        obj.delete(using=self.using)
    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )

class localdb(database):
    using = "localhost"

class RDSdb(database):
    using = "RDS"

class otherRDSdb(database):
    using = "otherRDS"

admin.site.register(Project, database)
localadmin.register(Project, localdb)
RDSadmin.register(Project, RDSdb)
otherRDSadmin.register(Project, otherRDSdb)