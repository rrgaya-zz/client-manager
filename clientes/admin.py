from django.contrib import admin
from .models import Person, Documento, Venda, Produto
from .actions import nfe_emitida, nfe_nao_emitida


class PersonAdmin(admin.ModelAdmin):
    model = Person
    fieldsets = (
        ('Dados Pessoais', {'fields': ('first_name', 'last_name')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'bio', 'photo', 'doc')})
    )
    # fields = (('first_name', 'last_name'), ('age', 'salary'), 'bio', ('doc', 'photo'))
    # exclude = ('bio', )
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto', 'doc')
    list_filter = ('age', 'salary', )
    search_fields = ['first_name', 'last_name', 'age',]

    def tem_foto(self, obj):
        if obj.photo:
            return "Sim"
        else:
            return "Não"


class VendaAdmin(admin.ModelAdmin):
    fields = ('numero', 'desconto', 'impostos', 'pessoa', 'produtos', 'valor', 'nfe_emitida')
    readonly_fields =  ('valor',)
    raw_id_fields = ('pessoa',)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('numero', 'id', 'valor', 'get_total', 'nfe_emitida')
    search_fields = ['id', 'pessoa__first_name', 'pessoa__doc__num_doc']
    actions = [nfe_emitida, nfe_nao_emitida]
    # filter_vertical = ('produtos',)
    filter_horizontal = ('produtos',)

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')



admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)