from django.shortcuts import redirect, render
from .models import Pessoa
from .forms import PessoaForm

def list_pessoa(request):
    pessoa=Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas':pessoa})

def create_pessoa(request):
    form=PessoaForm(request.POST or None)
    context = {'form':form}
    pessoa=Pessoa.objects.all()
    if form.is_valid():
        cep=request.POST.get('cep', None)
        ende=request.POST.get('ende', None)
        numero=request.POST.get('numero', None)
        complemento=request.POST.get('complemento', None)
        bairro=request.POST.get('bairro', None)
        cidade=request.POST.get('cidade', None)
        uf=request.POST.get('uf', None)
        descricao=request.POST.get('descricao', None)
        b=Pessoa(cep=cep, ende=ende+", "+numero+", "+bairro+", "+cidade+", "+uf, numero=numero, complemento=complemento, bairro=bairro, cidade=cidade, uf=uf, descricao=descricao)
        try: 
            pessoa=Pessoa.objects.get(cep=cep)
            pessoa.ende=ende+", "+numero+", "+bairro+", "+cidade
            pessoa.numero=numero
            pessoa.complemento=complemento
            pessoa.bairro=bairro
            pessoa.cidade=cidade
            pessoa.uf=uf
            pessoa.descricao=descricao
            pessoa.save()
        except:
            b.save()
        return redirect('list_pessoas')
    return render(request, 'pessoa-form.html', context=context)

    
# Create your views here.
