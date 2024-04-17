from flask import Blueprint, render_template
from database.cliente import clientes
cliente_route = Blueprint('clientes',__name__)

"""
Rota clientes

    - /clientes/ - listar clientes {GET}
    - /clientes/ - inserir cliente no servidor {POST}
    - /clientes/new - novo cliente {GET}
    - /clientes/<id> - obter dados do cliente {GET}
    - /clientes/<id>/edit - editar cliente {GET}
    - /clientes/<id>/update - atualizar dados do cliente {PUT}
    - /clientes/<id>/delete - apagar cliente {DELETE}
"""

@cliente_route.route('/')
def lista_clientes(): # Listar clientes
    return render_template('lista_clientes.html', clientes=clientes)

@cliente_route.route('/',methods=['POST'])
def inserir_cliente(): # Inserir cliente no banco de dados
    pass

@cliente_route.route('/new')
def form_cliente(): # Fomulario de criação de cliente
    return render_template('form_criar_clientes.html')    

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id): # Fomulario de edição de cliente
    return render_template('form_edit_clientes.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id): # Atualizar dados do cliente
    pass

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id): # Exibir detalhes do cliente
    render_template('detalhe_clientes.html')

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def del_cliente(cliente_id): # Deletar cliente
    pass