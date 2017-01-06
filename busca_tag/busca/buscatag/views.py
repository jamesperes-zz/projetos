from django.shortcuts import render
from django.template.loader import render_to_string


from .models import PessoaTag, Pessoa, Tag

def tag_lista(request):
    tags_localizados = PessoaTag.objects.all()
    return render(request, 'busca/lista.html', {'tags': tags_localizados})
