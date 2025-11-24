# test_seguranca_pedidos.py
import pytest
from sistema_pedidos import buscar_detalhes_pedido

def test_usuario_nao_pode_acessar_pedido_de_outro_usuario(id_pedido: int, id_usuario_atacante: int):

    resultado = buscar_detalhes_pedido(id_pedido, id_usuario_atacante)

    assert resultado == {}, (
        "Falha de segurança: usuário 2 conseguiu acessar dados "
        "do pedido que pertence ao usuário 1!"
    )

test_usuario_nao_pode_acessar_pedido_de_outro_usuario(101, 2)
