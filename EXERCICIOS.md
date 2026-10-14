# Exercícios da disciplina

Atividades em **dupla**, feitas ao final de cada aula. Cada uma tem um arquivo inicial com trechos
marcados com `TODO`: altere apenas esses trechos. O enunciado completo está no `ATIVIDADE.md` da
pasta `alunos/` de cada aula.

## Como começar

1. Abra o terminal na pasta `alunos` da aula.
2. Crie o ambiente e instale as dependências (só na primeira vez):
   - Windows: `py -3 -m venv .venv` e `.venv\Scripts\python.exe -m pip install -r requirements.txt`
   - macOS/Linux: `python3 -m venv .venv` e `.venv/bin/python -m pip install -r requirements.txt`
3. Rode as demonstrações da aula e depois o arquivo da atividade.

No PyCharm, abra a pasta `alunos` da aula como projeto e use **Run**.

## Entrega (todas as atividades)

- O arquivo da atividade alterado.
- Uma captura do resultado, salva pela tecla indicada abaixo durante a execução (vai para
  `capturas/resultado.png`).
- Os nomes dos dois integrantes.
- Um parágrafo respondendo à pergunta de explicação da atividade.

Cada atividade vale **10 pontos**. A tabela de critérios está no `ATIVIDADE.md` correspondente.

---

## 1. Mini sistema solar (Transformações)

📁 `Aula_Transformacoes/alunos/` · arquivo `atividade_sistema_solar.py` · 25 min · captura: **P**

Use apenas `make_translation`, `make_rotation_z` e `make_scale`, combinadas com `@`.

1. O sol gira em torno do próprio centro.
2. O planeta orbita o sol (raio 0.6).
3. O planeta gira em torno do próprio eixo, com velocidade diferente da órbita.
4. A lua orbita o planeta (raio 0.2) e o acompanha.
5. As setas ↑ e ↓ mudam a velocidade da órbita, que nunca fica negativa.

**Explique:** por que a órbita usa `R @ T` e a rotação própria fica à direita da translação?

[Enunciado completo](Aula_Transformacoes/alunos/ATIVIDADE.md)

## 2. Braço robótico (Grafo de cena)

📁 `Aula_GrafoCena/alunos/` · arquivo `atividade_braco.py` · 25 min · captura: **P**

1. Um pivô (`Object3D`) no topo da base, com o braço laranja preso a ele pela ponta de baixo.
2. Um pivô na ponta do braço (cotovelo), com o antebraço azul preso a ele.
3. Uma garra cinza na ponta do antebraço.
4. A e D giram a base (e todo o braço) em torno do eixo Y.
5. W e S giram o ombro; I e K giram o cotovelo, em torno do eixo Z.

**Explique:** por que foi preciso usar pivôs em vez de girar as caixas diretamente?

[Enunciado completo](Aula_GrafoCena/alunos/ATIVIDADE.md)

## 3. Cubo com satélite texturizado (Texturas)

📁 `Aula_Texturas/alunos/` · arquivo `atividade_cubo.py` · 20 min · captura: **S**

1. O cubo principal usa a textura `mosaico.png`.
2. Um segundo cubo (satélite) usa `grade_uv.png` repetida 2x2 (`repeatUV = [2,2]`).
3. O satélite é filho do cubo principal: fica a 1.3 do centro, com escala 0.4, e orbita junto.
4. As setas ↑ e ↓ mudam a velocidade de rotação do cubo principal.
5. O satélite gira em torno do próprio eixo X.

**Explique:** qual é o papel das coordenadas UV e qual o efeito de `repeatUV = [2,2]`?

[Enunciado completo](Aula_Texturas/alunos/ATIVIDADE.md)

---

## Dicas gerais

- Velocidades são **por segundo**: multiplique sempre por `self.deltaTime`.
- Em `A @ B @ ponto`, a matriz mais à direita é aplicada primeiro.
- Posicione antes de escalar, senão a distância também encolhe.
- Erros de importação (`ModuleNotFoundError: core`): execute a partir da pasta `alunos` da aula.
