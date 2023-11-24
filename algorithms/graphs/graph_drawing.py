import pygame
import random
import sys


pygame.init()

fps = 60

window_size = (800, 500)

font_family = 'Arial'
font_size = 30

radius = 30
round_radius = 10
border_width = 3
edge_width = 3
side1 = 20
side2 = 10
padding_x = 10
padding_y = 5

background_color = (255, 255, 255)
fill_color = (220, 220, 220)
border_color = (0, 0, 0)
edge_color = (0, 0, 0)
font_color = (0, 0, 0)
cmd_background_color = (220, 220, 220)

save_names = ('1', 's', 'save')
load_names = ('2', 'l', 'load')
exit_names = ('e', 'exit')
random_names = ('r', 'random')

path = '\\data\\'

temp = pygame.font.SysFont(font_family, font_size)
temp = temp.render('a', True, font_color)
temp = temp.get_rect()
temp = temp.h
print(temp)

cmd_size = (window_size[0] * 0.6, temp + 2 * padding_y)
cmd_coords = ((window_size[0] - cmd_size[0]) // 2, 5)


arr = [
    [],
    [5],
    [9],
    [1],
    [2, 9],
    [3],
    [8, 11],
    [4, 5],
    [9, 10, 11],
    [5, 7],
    [2, 6],
    [3],
]


window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()


def line(x1, y1, x2, y2):
    k = None
    b = None

    if x1 == x2:
        k = -1
        b = x1
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1

    return k, b


def step(x1, y1, x2, y2, k, side):
    kx = None
    ky = None
    if x2 > x1:
        kx = -1
        ky = -1
    else:
        kx = 1
        ky = 1

    x0 = x2 + kx * side / (1 + k ** 2) ** .5
    y0 = y2 + ky * k * side / (1 + k ** 2) ** .5

    if x1 == x2:
        x0 = x2
        if y2 > y1:
            y0 = y2 - side
        else:
            y0 = y2 + side

    return x0, y0


def is_oriented(arr=arr):
    temp = []
    for i in range(len(arr)):
        for j in arr[i]:
            for l in range(len(temp)):
                if temp[l] == [j, i]:
                    temp.pop(l)
                    break
            else:
                temp.append([i, j])

    if len(temp) > 0:
        return True
    return False


def save(name):
    verts = []
    for vertex in vertices:
        verts.append([vertex.coords, vertex._text])

    with open(f'{sys.path[0]}{path}{name}.json', 'w', encoding='utf-8') as file:
        file.write(str([verts, arr]))


def load(name):
    with open(f'{sys.path[0]}{path}{name}.json', 'r', encoding='utf-8') as file:
        data = file.read()
        if data != '':
            global vertices
            global arr
            global oriented

            data = eval(data)
            [verts, arr] = data

            vertices = []
            for [coords, text] in verts:
                vertices.append(Vertex(text))
                vertices[-1].coords = coords

            oriented = is_oriented()


class CommandLine:
    def __init__(self,
                 window,
                 size=cmd_size,
                 coords=cmd_coords,
                 background_color=cmd_background_color,
                 radius=round_radius,
                 font_family=font_family,
                 font_size=font_size,
                 padding_x=padding_x,
                 padding_y=padding_y):

        self.window = window
        self.background_color = background_color
        self.radius = radius
        self.rect = pygame.Rect(*coords, *size)
        self.show = False
        self.font_family = font_family
        self.font_size = font_size
        self.font_color = font_color
        self.padding_x = padding_x
        self.padding_y = padding_y

    def draw(self, text):
        pygame.draw.rect(self.window, self.background_color, self.rect, border_radius=self.radius)
        self.draw_text(text)

    def draw_text(self, text):
        font = pygame.font.SysFont(self.font_family, self.font_size)

        text_surface = font.render(text, True, self.font_color)

        self.window.blit(text_surface, (self.rect.x + self.padding_x, self.rect.y + self.padding_y))


class Vertex(pygame.sprite.Sprite):
    def __init__(self,
                 text='',
                 window=window,
                 window_size=window_size,
                 radius=radius,
                 border_width=border_width,
                 font_family=font_family,
                 fill_color=fill_color,
                 border_color=border_color,
                 font_color=font_color,
                 font_size=font_size
                 ):
        pygame.sprite.Sprite.__init__(self)

        self.text = text

        self.window = window

        self.radius = radius
        self.border_width = border_width
        self.font_family = font_family
        self.font_size = font_size

        self.fill_color = fill_color
        self.border_color = border_color
        self.font_color = font_color

        self.coords = [
            random.randint(self.radius + self.border_width, window_size[0] - self.radius - self.border_width),
            random.randint(self.radius + self.border_width, window_size[1] - self.radius - self.border_width)
        ]

    def draw(self, text=None):
        pygame.draw.circle(self.window, self.fill_color, self.coords, self.radius)
        pygame.draw.circle(self.window, self.border_color, self.coords, self.radius + self.border_width, self.border_width)
        self.draw_text(text)

    def draw_text(self, text=None):
        if text != None:
            self.text = text

        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.text_surface = self.font.render(self.text, True, self.font_color)
        rect = self.text_surface.get_rect()
        self.text_size = (rect.w, rect.h)

        window.blit(self.text_surface, (int(self.coords[0] - self.text_size[0] / 2), int(self.coords[1] - self.text_size[1] / 2)))

    def collidepoint(self, pos):
        r0 = (pos[0] - self.coords[0]) ** 2 + (pos[1] - self.coords[1]) ** 2
        if r0 <= self.radius ** 2:
            return True
        return False


oriented = is_oriented()

vertices = []
for i in range(len(arr)):
    vertices.append(Vertex(str(i)))

clicked_vertex = None

command_line = CommandLine(window)
command = ''

while True:

    window.fill(background_color)

    for i in range(len(arr)):
        for j in arr[i]:
            pygame.draw.line(window, edge_color, vertices[i].coords, vertices[j].coords, edge_width)
            if oriented:
                [x1, y1] = vertices[i].coords
                [x2, y2] = vertices[j].coords

                coords = []

                k1, b1 = line(x1, y1, x2, y2)

                x0, y0 = step(x1, y1, x2, y2, k1, radius)

                coords.append([int(x0), int(y0)])

                x0, y0 = step(x1, y1, x0, y0, k1, side1)

                if k1 == 0:
                    coords.append([int(x0), int(y0 - side2)])
                    coords.append([int(x0), int(y0 + side2)])

                else:
                    k2 = -1 / k1
                    if k1 == -1:
                        k2 = 0
                    b2 = y0 - k2 * x0

                    x1 = x0 + side2 / (1 + k2 ** 2) ** .5
                    y1 = k2 * x1 + b2
                    coords.append([int(x1), int(y1)])

                    x1 = x0 - side2 / (1 + k2 ** 2) ** .5
                    y1 = k2 * x1 + b2

                    coords.append([int(x1), int(y1)])

                pygame.draw.polygon(window, edge_color, coords)

    for vertex in vertices:
        vertex.draw()

    if command_line.show:
        command_line.draw(command)

    if clicked_vertex != None:
        mouse_pos = pygame.mouse.get_pos()
        clicked_vertex.coords = mouse_pos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for vertex in vertices:
                if vertex.collidepoint(mouse_pos):
                    clicked_vertex = vertex

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicked_vertex = None

        if command_line.show and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                command_line.show = False
                command = command.split()
                if command[0] in exit_names:
                    sys.exit()

                elif command[0] in random_names:
                    vertices = []
                    for i in range(len(arr)):
                        vertices.append(Vertex(str(i)))

                elif command[0] in save_names:
                    save(command[1])

                elif command[0] in load_names:
                    load(command[1])

                else:
                    command = ' '.join(command)
                    if 'self' in command:
                        command = command.replace('self', 'vertex')
                        for vertex in vertices:
                            mouse_pos = pygame.mouse.get_pos()
                            if vertex.collidepoint(mouse_pos):
                                exec(command)

                    elif 'all' in command:
                        command = command.replace('all', 'vertex')
                        for vertex in vertices:
                            exec(command)

                    else:
                        exec(command)

                command = ''

            elif event.key == pygame.K_BACKSPACE:
                command = command[:-1]

            elif event.key == pygame.K_ESCAPE:
                command_line.show = False
                command = ''

            else:
                command += event.unicode

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            command_line.show = True

    pygame.display.update()
    clock.tick(fps)
