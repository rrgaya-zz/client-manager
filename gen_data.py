import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestao_clientes.settings")
django.setup()

import string
import time
from random import random, randint, choice
from produtos.models import Produto


class Utils:
    """metodos genericos"""

    @staticmethod
    def gen_digitis(max_length):
        return str("".join(choice(string.digits) for i in range(max_length)))


class ProductClass:
    """Criar produtos ficticios para o model"""

    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                descricao=Utils.gen_digitis(3) + " - " + produto,
                preco=random() * randint(750, 4500),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    "Notebook",
    "Monitor",
    "Desktop",
    "Mouse",
    "Teclado",
    "Baterias de Notebook",
    "Carregador",
)

t0 = time.time()

ProductClass.criar_produtos(produtos)

resposta = time.time() - t0

print(resposta)
