from django.shortcuts import render
from django.template.loader import render_to_string


from .models import PessoaTag, Pessoa, Tag, Projetolist

def tags_ratings(request, tag_id):

    tags_localizados = PessoaTag.objects.filter(
        tag__id=tag_id).order_by('-rating')
    return render(request,
                  'busca/tags_ratings.html',
                  {'tags': tags_localizados})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'busca/tags_list.html', {'tags': tags})

def pessoa(request, pessoa_id):

    pessoa = Pessoa.objects.get(id=pessoa_id)
    pessoa_tags = PessoaTag.objects.filter(pessoa__id=pessoa_id).order_by('-rating')
    return render(request, 'busca/pessoa.html', {'pessoa': pessoa,
                                                 'pessoa_tags': pessoa_tags})

def dev_list(request):
    dev = Pessoa.objects.all()
    return render(request, 'busca/dev_list.html', {'devs': dev})

def pro_list(request):
    projetos = Projetolist.objects.all()
    #for projeto in projetos:
    #devs = projeto.devs.all()
    #tags = projeto.tag.all()
    return render (request, 'busca/pro_list.html', {'projetos': projetos})
