import math
from Modelo import *
import glm

class Fondo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(0.0,0.0,0.0)
        self.vertices = np.array(
            [
                #Fondo
                -1.0,2.0,0.0,1.0,    30/255, 69/255, 34/255,1.0,  #izquierda arriba
                -1.0,-2.0,0.0,1.0,   30/255, 69/255, 34/255,1.0,  #izquierda abajo
                1.0,2.0,0.0,1.0,     30/255, 69/255, 34/255,1.0, #derecha arriba
                1.0,-2.0,0.0,1.0,    30/255, 69/255, 34/255,1.0, # derecha abajo

                #Calle
                -1.0,0.9,0.0,1.0,    92/255,92/255,92/255,1.0,  #izquierda arriba
                -1.0,-0.9,0.0,1.0,   92/255,92/255,92/255,1.0,  #izquierda abajo
                1.0,0.9,0.0,1.0,     92/255,92/255,92/255,1.0, #derecha arriba
                1.0,-0.9,0.0,1.0,    92/255,92/255,92/255,1.0, # derecha abajo

                #Banqueta
                -1.0,-0.30,0.0,1.0,   184/255, 186/255, 186/255,1.0,  #izquierda arriba
                -1.0,-0.40,0.0,1.0,   184/255, 186/255, 186/255,1.0,  #izquierda abajo
                1.0,-0.30,0.0,1.0,    184/255, 186/255, 186/255,1.0, #derecha arriba
                1.0,-0.40,0.0,1.0,    184/255, 186/255, 186/255,1.0, # derecha abajo

                -1.0,0.30,0.0,1.0,    184/255, 186/255, 186/255,1.0,  #izquierda arriba
                -1.0,0.40,0.0,1.0,    184/255, 186/255, 186/255,1.0,  #izquierda abajo
                1.0,0.30,0.0,1.0,     184/255, 186/255, 186/255,1.0, #derecha arriba
                1.0,0.40,0.0,1.0,     184/255, 186/255, 186/255,1.0, # derecha abajo

                #Lineas calle
                -1.0,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                -1.0,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                -0.8,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                -0.8,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                -0.5,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                -0.5,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                -0.3,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                -0.3,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                0.0,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                0.0,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                0.2,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                0.2,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                0.5,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                0.5,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                0.7,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                0.7,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                0.5,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0,  #izquierda arriba
                0.5,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0,  #izquierda abajo
                0.7,0.025,0.0,1.0,   255/255, 227/255, 11/255,1.0, #derecha arriba
                0.7,-0.025,0.0,1.0,  255/255, 227/255, 11/255,1.0, # derecha abajo

                #Lineas calle abajo
                -1.0 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -0.5 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -0.5 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.3 +.1, 0.025 -.67 ,0.0,1.0,  255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.3 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                0.0 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                0.0 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                0.2 +.1, 0.025 -.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                0.2 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                0.5 +.1, 0.025 -.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                0.5 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                0.7 +.1, 0.025 -.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                0.7 +.1, -0.025 -.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                #Lineas calle arriba
                -1.0 +.1, 0.025 +.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8 +.1, 0.025 +.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -0.5 +.1, 0.025 +.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -0.5 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.3 +.1, 0.025 +.67 ,0.0,1.0,  255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.3 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                0.0 +.1, 0.025 +.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                0.0 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                0.2 +.1, 0.025 +.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                0.2 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                0.5 +.1, 0.025 +.67,0.0,1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                0.5 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                0.7 +.1, 0.025 +.67 ,0.0,1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                0.7 +.1, -0.025 +.67,0.0,1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                #Lineas peatonales arriba
                -1.0, 0.085, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, 0.070, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, 0.085, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, 0.070, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, 0.14, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, 0.12, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, 0.14, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, 0.12, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, 0.20, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, 0.18, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, 0.20, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, 0.18, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, 0.26, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, 0.24, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, 0.26, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, 0.24, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                #Lineas peatonales abajo
                -1.0, -0.085, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, -0.070, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, -0.085, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, -0.070, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, -0.14, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, -0.12, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, -0.14, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, -0.12, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, -0.20, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, -0.18, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, -0.20, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, -0.18, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo

                -1.0, -0.26, 0.0, 1.0,   255/255, 255/255, 255/255,1.0,  #izquierda arriba
                -1.0, -0.24, 0.0, 1.0,  255/255, 255/255, 255/255,1.0,  #izquierda abajo
                -0.8, -0.26, 0.0, 1.0,   255/255, 255/255, 255/255,1.0, #derecha arriba
                -0.8, -0.24, 0.0, 1.0,  255/255, 255/255, 255/255,1.0, # derecha abajo


                
            ], dtype="float32"

        )
        for angulo in range(0, 359, 5):
            componente_x = 0.1 * math.cos(angulo * math.pi / 180) +.3
            componente_y = 0.065 * math.sin(angulo * math.pi / 180) -.08 +.42 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            66/255, 193/255, 42/255, 1.0 ], dtype="float32"))


        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, direccion):
        
        if direccion == self.ARRIBA:
           self.posicion.y  = self.posicion.y + 0.001
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - 0.001

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 52, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 56, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 60, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 64, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 68, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 72, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 76, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 80, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 84, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 88, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 92, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 96, 4)
        #gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        #gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 48, 72)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()