# Importamos a função index() definida no arquivo views.py
from django.urls import path
from website.views import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioCreateView, FuncionarioDeleteView

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # Get /
    path('', IndexTemplateView.as_view(), name='index'),

    # Get /funcionario/cadastrar
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name="cadastra_funcionario"),

    # Get /funcionario
    path('funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),

    # Get/Post /funcionario/{pk}
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),

    # Get/Post /funcionarios/excluir/{pk}
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),
]