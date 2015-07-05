import pygame
import pygame.display
import pygame.key
import pygame.image
import pygame.mouse
import pygame.time

from pygame.locals import QUIT, USEREVENT

from collections import namedtuple

Mouse = namedtuple('Mouse', ['pressed', 'pos'])
Keys = namedtuple('Keys', ['pressed'])
Scene = namedtuple('Scene', ['elements'])

class GameState(object):
    def __init__(self):
        self.display = pygame.display.Info()
        self.screen = pygame.display.set_mode(
            (self.display.current_w, self.display.current_h), 
            pygame.FULLSCREEN)
        # TODO Meh
        self.mouse = None
        self.keys = None
        self.player = None
        self.clock = pygame.time.Clock()

    def update(self):
        self.mouse = Mouse(pygame.mouse.get_pressed(), pygame.mouse.get_pos())
        self.keys = Keys(pygame.key.get_pressed())


class GameLoop(object):
    def __init__(self):
        # TODO Meh
        self.game_state = GameState()
        self.scene = Scene({})


    def do_loop(self):
        while True:
            self.game_state.clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == USEREVENT:
                    # TODO: Handle user-events
                    pass


            self.game_state.update()

            # TODO: Put this logic elsewhere
            if self.game_state.keys.pressed[pygame.K_ESCAPE]:
                return

            for el in self.scene.elements.itervalues():
                el.draw(self.game_state)

            pygame.display.flip()


class AssetsCache(object):
    def __init__(self):
        self._assets = {}
        self._cache = {}

    def load(self, name, path):
        self._assets[name] = path
        self._cache[name] = pygame.image.load(path).convert()

    def get(self, name, reload=False):
        assert name in self._assets, 'No such asset [%s]' % name

        if reload:
            path = self._assets[name]
            self.load(name, path)

        return self._cache[name]
