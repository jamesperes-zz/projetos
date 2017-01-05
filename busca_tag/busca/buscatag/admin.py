from django.contrib import admin
from .models import Pessoa, Tag, PessoaTag

class PessoaAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class PessoaTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PessoaTag, PessoaTagAdmin)
