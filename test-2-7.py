from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *


# anima um triângulo a mover-se pelo ecrã
class Test(Base):

    def initialize(self):

        print("Initializing program...")

        ### inicializa o programa ###
        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main()
        {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(
                baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(
            vsCode, fsCode)

        ### definições de renderização (opcional) ###
        # especifica a cor usada ao limpar o ecrã
        glClearColor(0.0, 0.0, 0.0, 1.0)

         ### configura o vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

         ### configura o atributo de vértice ###
        positionData = [[0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]]
        self.vertexCount = len(positionData)

        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(
            self.programRef, "position")

        ### configura as uniforms ###
        self.translation = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation.locateVariable(
            self.programRef, "translation")

        self.baseColor = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor.locateVariable(
            self.programRef, "baseColor")

    def update(self):

        ### atualiza os dados ###

        # aumenta a coordenada x da translação
        self.translation.data[0] += 0.01
        # se o triângulo sair do ecrã pela direita,
        #  altera a translação para que reapareça pela esquerda
        if self.translation.data[0] > 1.2:
            self.translation.data[0] = -1.2

        ### renderiza a cena ###
        # repõe o buffer de cor com a cor especificada
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.programRef)
        self.translation.uploadData()
        self.baseColor.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# instancia esta classe e executa o programa
Test().run()
