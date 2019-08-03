from django.contrib import admin
from .models import Person, Documento


class PersonAdmin(admin.ModelAdmin):
    model = Person
    fieldsets = (
        ('Dados Pessoais', {'fields': ('first_name', 'last_name', 'telefone')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'bio', 'photo', 'doc', 'user',)})
    )
    # fields = (('first_name', 'last_name'), ('age', 'salary'), 'bio', ('doc', 'photo'))
    # exclude = ('bio', )
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto', 'doc', 'telefone', 'user',)
    list_filter = ('age', 'salary', )
    search_fields = ['id', 'first_name', 'last_name', 'age',]
    autocomplete_fields = ["doc"]

    def tem_foto(self, obj):
        if obj.photo:
            return "Sim"
        else:
            return "Não"



class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ["num_doc"]



admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
