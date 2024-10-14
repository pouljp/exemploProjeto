import os
import django
import random

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exemploProjeto.settings')
django.setup()

from loja.models import Produto

# Lista de exemplos
nomes_produtos = ['Camiseta', 'Calça', 'Tênis', 'Casaco', 'Relógio', 'Bolsa', 'Óculos', 'Chapéu']
categorias = ['Vestuário', 'Acessórios', 'Eletrônicos', 'Calçados']
precos = [49.99, 89.90, 199.99, 299.99, 159.99, 99.99, 129.90, 79.99]
estoque = [10, 20, 50, 15, 30, 60, 80, 100]

# Criar produtos fictícios
for _ in range(20):
    produto = Produto(
        nome=random.choice(nomes_produtos),
        categoria=random.choice(categorias),
        preco=random.choice(precos),
        quantidade_em_estoque=random.choice(estoque)
    )
    produto.save()

print("Banco de dados populado com produtos de teste.")
