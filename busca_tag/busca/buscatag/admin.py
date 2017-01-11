from django.contrib import admin
from .models import Pessoa, Tag, PessoaTag, Projetolist


class TagAdmin(admin.ModelAdmin):
    pass


class PessoaTagAdmin(admin.ModelAdmin):
    pass

class PessoaTagInline(admin.TabularInline):
    model = PessoaTag
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    inlines = [PessoaTagInline]

#class ProjetolistInLine(admin.TabularInline):
#    model = Projetolist

class ProjetolistAdmin(admin.ModelAdmin):
    #inlines = [ProjetolistInLine]
    pass




admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PessoaTag, PessoaTagAdmin)
admin.site.register(Projetolist,ProjetolistAdmin)
