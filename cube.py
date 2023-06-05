import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

button_clicked = 0
window_width = 800
window_height = 600
rotation_angle = 0.0

def load_texture(image_path):
    texture_surface = pygame.image.load(image_path)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()
    
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    
    return texture
    
def draw_cube(texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    glRotatef(rotation_angle, 0.0, 1.0, 0.0)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glEnd()
    glDisable(GL_TEXTURE_2D)

def draw_button():
    glBegin(GL_QUADS)
    if button_clicked == 1:
        glColor3f(0.0, 0.0, 1.0)
    elif button_clicked == 2:
        glColor3f(0.0, 1.0, 0.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
    glEnd()

def display_callback():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)
    background_image = load_texture("data/img/texture.jpg")
    draw_cube(background_image)

    glLoadIdentity()
    glTranslate(0.0, 0.0, -1.0)
    draw_button()

    pygame.display.flip()

def main():
    pygame.init()
    pygame.display.set_mode((window_width, window_height), DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (window_width / window_height), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    global button_clicked
                    button_clicked = (button_clicked + 1) % 3

        global rotation_angle
        rotation_angle += 1.0

        display_callback()

        clock.tick(60)

if __name__ == '__main__':
    main()