# Computação Gráfica – Atividades Práticas

**Disciplina:** Computação Gráfica
**Integrantes:** Lucas Eduardo; Lucas Nogueira

---

## Atividade 1 – Mini Sistema Solar
**Pasta:** `Aula_Transformacoes/alunos/` · **Arquivo:** `atividade_sistema_solar.py` · **Captura:** `Aula_Transformacoes/alunos/capturas/resultado.png`

**Descrição:** O Sol gira no próprio centro. O planeta orbita o Sol (raio 0.6) e gira no próprio eixo com velocidade diferente da órbita. A Lua orbita o planeta (raio 0.2) e o acompanha. As teclas ↑ e ↓ aumentam e diminuem a velocidade da órbita, que nunca fica negativa. Usa apenas `make_translation`, `make_rotation_z` e `make_scale`, combinadas com `@`.

**Resposta da questão:** A rotação própria fica à direita da translação porque as matrizes são lidas da direita para a esquerda: o planeta ainda está na origem quando gira, então gira em torno do próprio eixo. A órbita é `R @ T` porque a translação empurra o planeta para x = 0.6 e, em seguida, a rotação em torno da origem o arrasta junto, formando um círculo.

---

## Atividade 2 – Braço Robótico
**Pasta:** `Aula_GrafoCena/alunos/` · **Arquivo:** `atividade_braco.py` · **Captura:** `Aula_GrafoCena/alunos/capturas/resultado.png`

**Descrição:** Grafo de cena com base, pivô do ombro, braço laranja, pivô do cotovelo, antebraço azul e garra cinza. A/D giram a base em Y; W/S giram o ombro em Z; I/K giram o cotovelo em Z.

**Resposta da questão:** Cada caixa gira em torno do próprio centro, então girá-la diretamente a faria rodar como uma hélice. Os pivôs funcionam como dobradiças nas extremidades: a caixa é filha do pivô e deslocada, e a rotação acontece a partir da ponta. A hierarquia também faz as partes abaixo (antebraço, garra) acompanharem o movimento do ombro.

---

## Atividade 3 – Cubo com Satélite Texturizado
**Pasta:** `Aula_Texturas/alunos/` · **Arquivo:** `atividade_cubo.py` · **Captura:** `Aula_Texturas/alunos/capturas/resultado.png`

**Descrição:** O cubo principal usa `mosaico.png`. O satélite usa `grade_uv.png` com `repeatUV = [2,2]`, é filho do cubo, fica a 1.3 do centro, com escala 0.4, e gira no próprio eixo X. ↑ e ↓ alteram a velocidade de rotação do cubo principal.

**Resposta da questão:** As coordenadas UV indicam como a textura 2D é mapeada sobre os vértices e as faces do modelo 3D. Com `repeatUV = [2,2]`, as coordenadas são multiplicadas por 2. Valores acima de 1.0 fazem a imagem recomeçar, e ela aparece repetida 2 vezes na horizontal e 2 na vertical em cada face.


