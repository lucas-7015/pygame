# Material da aula de Transformações Geométricas
A apresentação tem 26 slides, com notas do professor, para uma aula de 90 minutos (65 min de exposição e demonstrações + 25 min de atividade).

- `Aula_Transformacoes_OpenGL_26_Slides.pptx`: slides com notas e roteiro das demonstrações.
- `alunos/`: framework didático, 3 demonstrações, arquivo inicial da atividade, enunciado e instruções para Windows/macOS. **Entregue apenas esta pasta à turma.**
- `professor/`: solução de referência, captura esperada e rubrica.

A aula continua o checkpoint `test-3.py` do repositório: as mesmas classes (`Base`, `Input`, `Utils`, `Attribute`, `Uniform`, `Matrix`) e a mesma convenção de multiplicação (global à esquerda, local à direita).

Diferença importante em relação ao `core/` da raiz do repositório: o `alunos/core/uniform.py` suporta o tipo `mat4`, que o `test-3.py` precisa. O `alunos/core/base.py` também pede OpenGL 3.3 core e trata ESC, captura (tecla P) e execução por N quadros.

As classes e convenções seguem o livro *Developing Graphics Frameworks with Python and OpenGL*, de Lee Stemkoski e Michael Pascale (CRC Press, 2022), capítulo 3.

Próxima aula: `Aula_GrafoCena` (capítulo 4), que transforma as matrizes desta aula em uma árvore de objetos, e depois `Aula_Texturas` (capítulo 5).
