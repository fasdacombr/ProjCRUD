from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from helloworld.models import Funcionario
from website.forms import InsereFuncionarioForm

# Página Principal.
# -------------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# Lista de Funcionários
# -------------------------------------------------

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

# Cadastramento de Funcionarios
# -------------------------------------------------

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")

# Atualização de Funcionários
# -------------------------------------------------

class FuncionarioUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = "__all__"
    context_object_name = "funcionarios"
    success_url = reverse_lazy("website:lista_funcionarios")

# Exclusão de Funcionários
# -------------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = "funcionarios"
    success_url = reverse_lazy("website:lista_funcionarios")
