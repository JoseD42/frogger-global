import OpenGL.GL as gl
import glfw
import numpy as np
from Fondo import *
from Shader import *
from Modelo import *
from Carros import *
from Rana import *
from Triangulo import Triangulo

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

modelo = None
fondo = None
rana = None
carros = None
window = None

carros = {}

posiciones_carros = [
     [0.3,-0.85, 0.0],
     [0.8, -0.75, 0.0],
     [-0.4, -0.65, 0.0],
     [0.2, -0.55, 0.0],
     [0.7, -0.45, 0.0],
     [-0.1, -0.55, 0.0],
     [-0.3, -0.25, 0.0],
     [-0.6, -0.15, 0.0],
     [-0.2, -0.05, 0.0],
     [0.5, 0.05, 0.0],
     [0.3, 0.15, 0.0],
     [0.7, 0.25, 0.0],
     [0.9, 0.75, 0.0],
     [0.2, 0.45, 0.0],
     [-0.4, 0.55, 0.0],
     [-0.2, 0.65, 0.0],
     [0.5, 0.75, 0.0],
     [0.2, 0.85, 0.0],
     [0.5,-0.85, 0.0],
     [0.5, -0.75, 0.0],
     [-0.9, -0.65, 0.0],
     [0.8, -0.55, 0.0],
     [0.9, -0.45, 0.0],
     [-0.8, -0.85, 0.0],
     [-0.7, -0.25, 0.0],
     [-0.2, -0.15, 0.0],
     [-0.5, -0.05, 0.0],
     [0.9, 0.05, 0.0],
     [0.7, 0.15, 0.0],
     [0.2, 0.25, 0.0],
     [0.7, 0.65, 0.0],
     [0.5, 0.45, 0.0]
 ]

velocidades_carros=[0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.9, 0.5]
direcciones_carros=[2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def inicializar_carros(shader,
            posicion_id, color_id, transformaciones_id):
    for i in range(30):
        posicion_x=posiciones_carros[i][0]
        posicion_y=posiciones_carros[i][1]
        posicion_z=posiciones_carros[i][2]
        velocidad=velocidades_carros[i]
        direccion=direcciones_carros[i]
        carros.append(Carros(shader,
            posicion_id, color_id, transformaciones_id, posicion_x, posicion_y, posicion_z, velocidad, direccion))

def actualizar():
    global window

def dibujar():
    global modelo
    global fondo
    global rana
    global carros
    fondo.dibujar()
    for carro in carros:
        carro.dibujar()
    rana.dibujar()
    #modelo.dibujar()

def main():
    global modelo
    global fondo
    global rana
    global carros
    global window
    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

   
    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")
    color_id = gl.glGetAttribLocation(shader.shader_program, "color")
    
    transformaciones_id = gl.glGetUniformLocation(
            shader.shader_program, "transformations")
    
    modelo = Triangulo(shader, 
            posicion_id, color_id, transformaciones_id)

    fondo = Fondo(shader, 
            posicion_id, color_id, transformaciones_id)

    rana = Rana(shader,
            posicion_id, color_id, transformaciones_id)

    #carros = Carros(shader,
            #posicion_id, color_id, transformaciones_id)

    inicializar_carros(shader,
            posicion_id, color_id, transformaciones_id)

    glfw.set_key_callback(window, rana.actualizar)

    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(0.3,0.3,0.3,1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        dibujar()
        actualizar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar memoria
    modelo.borrar()
    fondo.borrar()
    rana.borrar()
    carros.borrar()
    shader.borrar()

    

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()

