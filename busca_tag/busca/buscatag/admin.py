from django.contrib import admin
from .models import Pessoa, Tag, PessoaTag




class TagAdmin(admin.ModelAdmin):
    pass


class PessoaTagAdmin(admin.ModelAdmin):
    pass

class PessoaTagInline(admin.TabularInline):
    model = PessoaTag
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    inlines = [PessoaTagInline]



admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PessoaTag, PessoaTagAdmin)
