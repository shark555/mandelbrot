import ctypes
from sdl2 import *


class Drawer:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.window = ""
        self.renderer = ""

    def init_screen(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = SDL_CreateWindow(self.title, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, self.width,
                                       self.height, SDL_WINDOW_SHOWN)
        self.renderer = SDL_CreateRenderer(self.window, 0, 0)

    def wait(self):
        running = True
        event = SDL_Event()
        while running:
            while SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == SDL_QUIT:
                    running = False
                    break
        SDL_DestroyWindow(self.window)
        SDL_Quit()

    def draw_point(self, x, y, r=255, g=255, b=255):
        SDL_SetRenderDrawColor(self.renderer, r, g, b, 255)
        (x, y) = self.convert_coords(x, y)
        SDL_RenderDrawPoint(self.renderer, x, y)

    def refresh(self):
        SDL_RenderPresent(self.renderer)

    def clear(self):
        SDL_SetRenderDrawColor(self.renderer, 0, 0, 0, 255)
        SDL_RenderFillRect(self.renderer, SDL_Rect(0, 0, self.width, self.height))

    def convert_coords(self, x, y):
        return round(self.width / 2 + x * 300), round(self.height / 2 - y * 300)
