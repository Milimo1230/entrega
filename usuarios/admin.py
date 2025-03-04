from django.contrib import admin
from usuarios.models import Municipio, Departamento, Categoria, Artesano
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'Administrador - ASOARTE STORE'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Administrador - ASOARTE STORE'

class AdminMunicipios(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    class Meta:
        model = Municipio

class AdminDepartamento(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["nombre_departamento", "cod_depto"]
    search_fields = ["nombre_departamento", "cod_depto"]
    class Meta:
        model = Departamento


class AdminCategoria(admin.ModelAdmin):
	list_display = ["nombre"]
	search_fields = ["nombre"]
	class Meta:
		model = Categoria

class AdminArtesano(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["nombre"]    
    class Meta:
        model = Artesano

admin.site.register(Artesano, AdminArtesano)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Municipio, AdminMunicipios)
admin.site.register(Departamento, AdminDepartamento)