# ATIVIDADE: braço robótico com grafo de cena.
# Leia ATIVIDADE.md e complete os trechos marcados com TODO.
# ESC fecha. P salva capturas/resultado.png para a entrega.
import argparse

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.object3D import Object3D
from formas import caixa

CINZA = [0.6, 0.62, 0.66]
LARANJA = [0.98, 0.45, 0.2]
AZUL = [0.25, 0.5, 0.95]
VELOCIDADE = 1.5  # radianos por segundo


class Braco(Base):

    def initialize(self):
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=960 / 640)
        self.camera.setPosition([0, 1.9, 4.2])
        self.camera.rotateX(-0.2)

        chao = caixa(6, 0.1, 6, [0.8, 0.82, 0.85])
        chao.setPosition([0, -0.05, 0])
        self.scene.add(chao)

        # base: caixa de altura 0.4, apoiada no chão
        self.base = caixa(1.0, 0.4, 1.0, CINZA)
        self.base.setPosition([0, 0.2, 0])
        self.scene.add(self.base)

        # TODO 1: crie self.ombro = Object3D(), filho da base, no TOPO da base.
        self.ombro = Object3D()
        self.base.add(self.ombro)
        # A base tem altura 0.4 e centro no 0, então o topo local é 0.2 no Y
        self.ombro.setPosition([0, 0.2, 0])

        # Crie o braço: filho do ombro, posicionado para que a ponta de BAIXO fique no ombro.
        braco = caixa(0.3, 1.2, 0.3, LARANJA)
        self.ombro.add(braco)
        # O braço tem altura 1.2, subimos a metade (0.6) para a base dele ficar no pivô
        braco.setPosition([0, 0.6, 0])

        # TODO 2: crie self.cotovelo = Object3D(), filho do ombro, na ponta de CIMA do braço.
        self.cotovelo = Object3D()
        self.ombro.add(self.cotovelo)
        # A ponta de cima do braço está a 1.2 de distância do ombro
        self.cotovelo.setPosition([0, 1.2, 0])

        # Crie o antebraço: filho do cotovelo, com a ponta de baixo no cotovelo.
        antebraco = caixa(0.25, 1.0, 0.25, AZUL)
        self.cotovelo.add(antebraco)
        # O antebraço tem altura 1.0, subimos a metade (0.5)
        antebraco.setPosition([0, 0.5, 0])

        # TODO 3: crie a garra: na ponta do antebraço.
        garra = caixa(0.5, 0.15, 0.5, CINZA)
        self.cotovelo.add(garra)
        # A garra fica na ponta do antebraço (altura 1.0) + metade da própria altura (0.075)
        garra.setPosition([0, 1.075, 0])

    def update(self):
        angulo = VELOCIDADE * self.deltaTime

        # TODO 4: A e D giram a base em torno do eixo Y.
        if self.isKeyPressed("a"):
            self.base.rotateY(angulo)
        if self.isKeyPressed("d"):
            self.base.rotateY(-angulo)

        # TODO 5: W e S giram o ombro e I e K giram o cotovelo, ambos em torno do eixo Z.
        if self.isKeyPressed("w"):
            self.ombro.rotateZ(angulo)
        if self.isKeyPressed("s"):
            self.ombro.rotateZ(-angulo)

        if self.isKeyPressed("i"):
            self.cotovelo.rotateZ(angulo)
        if self.isKeyPressed("k"):
            self.cotovelo.rotateZ(-angulo)

        self.renderer.render(self.scene, self.camera)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int)
    parser.add_argument('--screenshot')
    args = parser.parse_args()
    Braco(title='Atividade: braço robótico').run(args.frames, args.screenshot)
