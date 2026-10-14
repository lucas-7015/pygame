from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *


# anima um retângulo formado por dois triângulos
class Test(Base):

    def initialize(self):

        print("Initializing program...")

        ### código do vertex shader ###
        vsCode = """
        in vec3 position;
        uniform vec3 translation;

        void main()
        {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """

        ### código do fragment shader ###
        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;

        void main()
        {
            fragColor = vec4(
                baseColor.r,
                baseColor.g,
                baseColor.b,
                1.0
            );
        }
        """

        ### cria o programa da GPU ###
        self.programRef = OpenGLUtils.initializeProgram(
            vsCode,
            fsCode
        )

        ### define a cor usada ao limpar a tela ###
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### configura o vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### seis vértices formando dois triângulos ###
        positionData = [

            # Primeiro triângulo
            [-0.3,  0.2, 0.0],
            [ 0.3,  0.2, 0.0],
            [ 0.3, -0.2, 0.0],

            # Segundo triângulo
            [-0.3,  0.2, 0.0],
            [ 0.3, -0.2, 0.0],
            [-0.3, -0.2, 0.0]
        ]

        # quantidade total de vértices: 6
        self.vertexCount = len(positionData)

        ### configura o atributo de posição ###
        positionAttribute = Attribute(
            "vec3",
            positionData
        )

        positionAttribute.associateVariable(
            self.programRef,
            "position"
        )

        ### configura a uniform de translação ###
        self.translation = Uniform(
            "vec3",
            [-1.3, 0.0, 0.0]
        )

        self.translation.locateVariable(
            self.programRef,
            "translation"
        )

        ### configura a uniform de cor ###
        # Altere estes valores para escolher outra cor
        # Vermelho: [1.0, 0.0, 0.0]
        # Verde:    [0.0, 1.0, 0.0]
        # Azul:     [0.0, 0.0, 1.0]
        self.baseColor = Uniform(
            "vec3",
            [0.2, 0.6, 1.0]
        )

        self.baseColor.locateVariable(
            self.programRef,
            "baseColor"
        )

    def update(self):

        ### movimenta o retângulo horizontalmente ###
        self.translation.data[0] += 0.01

        ### reaparece no lado esquerdo ###
        if self.translation.data[0] > 1.3:
            self.translation.data[0] = -1.3

        ### limpa o color buffer ###
        glClear(GL_COLOR_BUFFER_BIT)

        ### utiliza o programa da GPU ###
        glUseProgram(self.programRef)

        ### envia as uniforms para a GPU ###
        self.translation.uploadData()
        self.baseColor.uploadData()

        ### desenha os seis vértices como dois triângulos ###
        glDrawArrays(
            GL_TRIANGLES,
            0,
            self.vertexCount
        )


# instancia a classe e executa o programa
Test().run()