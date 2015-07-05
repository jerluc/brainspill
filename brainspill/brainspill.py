from game import *

def main():

    #-- SHITTY Make some kind of display/screen/device object
    import pygame
    pygame.init()
    display = pygame.display.Info()
    screen_size = (display.current_w, display.current_h)
    screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
    import pygame.mouse
    pygame.mouse.set_visible(False)
    #-/ SHITTY

    assets = AssetsCache()
    assets.load('hank', '../assets/hank.bmp')

    # TODO Create "drawable" objects that receive the game state
    # and current scene?
    class hankTest(object):
        def draw(self, game_state):
            game_state.screen.blit(assets.get('hank'), (400, 500))

    game_obj = GameLoop()

    # TODO Create a "transition" method or something to purge/revive scenes?
    game_obj.scene = Scene({
        'hank': hankTest()
    })

    game_obj.do_loop()

if __name__ == '__main__':
    main()
