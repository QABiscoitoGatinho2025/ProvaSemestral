# test_seguranca_pedidos.py
import pytest
from sistema_pedidos import buscar_detalhes_pedido

def test_usuario_nao_pode_acessar_pedido_de_outro_usuario():

    id_pedido = 101
    id_usuario_atacante = 2
    resultado = buscar_detalhes_pedido(id_pedido, id_usuario_atacante)

    assert resultado == {}, (
        "Falha de segurança: usuário 2 conseguiu acessar dados "
        "do pedido que pertence ao usuário 1!"
    )


