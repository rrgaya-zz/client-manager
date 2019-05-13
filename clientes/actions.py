def nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)

nfe_emitida.short_description = "Emitir NFE"