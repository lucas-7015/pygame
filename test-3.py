#!/usr/bin/python3
from math import pi

import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform
from core.matrix import Matrix


class Example(Base):
    """
    Move a triangle around the screen: global and local transformations.
    Use keys WASDZXQE and IJKLUO respectively.
    """

    def initialize(self):
        print('Initializing program...')
        ### Initialize program ###
        vs_code = """
            in vec3 position;
            uniform mat4 projectionMatrix;
            uniform mat4 modelMatrix;
            void main()
            {
                gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
            }
        """
        fs_code = """
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(1.0, 1.0, 0.0, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        ### Render settings ###
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        ### Set up vertex array object ###
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        ### Set up vertex attribute: three points of triangle ###
        position_data = [[0.0, 0.2, 0.0], [0.1, -0.2, 0.0], [-0.1, -0.2, 0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)

        # Correção aplicada aqui
        position_attribute.associateVariable(self.program_ref, 'position')

        ### Set up uniforms ###
        m_matrix = Matrix.make_translation(0, 0, -1)
        self.model_matrix = Uniform('mat4', m_matrix)

        # Correção aplicada aqui
        self.model_matrix.locateVariable(self.program_ref, 'modelMatrix')

        p_matrix = Matrix.make_perspective()
        self.projection_matrix = Uniform('mat4', p_matrix)

        # Correção aplicada aqui
        self.projection_matrix.locateVariable(self.program_ref, 'projectionMatrix')

        # movement speed, units per second
        self.move_speed = 0.5
        # rotation speed, radians per second
        self.turn_speed = 90 * (pi / 180)

    def update(self):
        """ Update data """
        move_amount = self.move_speed * self.deltaTime
        turn_amount = self.turn_speed * self.deltaTime
        # global translation
        if self.input.isKeyPressed('w'):
            m = Matrix.make_translation(0, move_amount, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.isKeyPressed('s'):
            m = Matrix.make_translation(0, -move_amount, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.isKeyPressed('a'):
            m = Matrix.make_translation(-move_amount, 0, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.isKeyPressed('d'):
            m = Matrix.make_translation(move_amount, 0, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.isKeyPressed('z'):
            m = Matrix.make_translation(0, 0, move_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.isKeyPressed('x'):
            m = Matrix.make_translation(0, 0, -move_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        # global rotation (around the origin)
        if self.input.isKeyPressed('q'):
            m = Matrix.make_rotation_z(turn_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.isKeyPressed('e'):
            m = Matrix.make_rotation_z(-turn_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        # local translation
        if self.input.isKeyPressed('i'):
            m = Matrix.make_translation(0, move_amount, 0)
            self.model_matrix.data = self.model_matrix.data @ m
        if self.input.isKeyPressed('k'):
            m = Matrix.make_translation(0, -move_amount, 0)
            self.model_matrix.data = self.model_matrix.data @ m
        if self.input.isKeyPressed('j'):
            m = Matrix.make_translation(-move_amount, 0, 0)
            self.model_matrix.data = self.model_matrix.data @ m
        if self.input.isKeyPressed('l'):
            m = Matrix.make_translation(move_amount, 0, 0)
            self.model_matrix.data = self.model_matrix.data @ m
        # local rotation (around object center)
        if self.input.isKeyPressed('u'):
            m = Matrix.make_rotation_z(turn_amount)
            self.model_matrix.data = self.model_matrix.data @ m
        if self.input.isKeyPressed('o'):
            m = Matrix.make_rotation_z(-turn_amount)
            self.model_matrix.data = self.model_matrix.data @ m
        ### Render scene ###
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)

        # Correções aplicadas aqui
        self.projection_matrix.uploadData()
        self.model_matrix.uploadData()

        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)


# Instantiate this class and run the program
Example().run()