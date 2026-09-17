# Métodos Numéricos - Problema 3 (Escoamento de Água)

Projeto da disciplina INF1920 - Métodos Numéricos, 1º GQ.

## Descrição

Implementação de 5 métodos numéricos (sem uso de funções prontas) para
encontrar a raiz da equação não linear que modela a altura de água
necessária para atingir uma velocidade de escoamento desejada.

## Instalação

Clone o repositório e instale o pacote com pip:

\`\`\`bash
git clone <link-do-repositorio>
cd projeto-metodos-numericos
pip install -e .
\`\`\`

## Uso

Abra o arquivo `notebook_analise.ipynb` e execute as células. O notebook
importa as funções do pacote `metodos_numericos` e aplica os métodos ao
problema do escoamento de água.

\`\`\`python
from metodos_numericos import bisseccao, posicao_falsa, ponto_fixo, newton_raphson, secante
\`\`\`

## Métodos implementados

- Bisseção
- Posição Falsa
- Ponto Fixo (Método Iterativo Linear)
- Newton-Raphson
- Secante

## Integrantes

- (nomes do grupo)
