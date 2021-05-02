import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getKey(key_name):
    ans = False
    for eve in pygame.event.get(): pass
    key_input = pygame.key.get_pressed()
    my_key = getattr(pygame, 'K_{}'.format(key_name))

    if key_input[my_key]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getKey('LEFT'):
        print('LEFT key pressed')
    if getKey('RIGHT'):
        print('RIGHT is pressed')


if __name__ == '__main__':
    init()
    while True:
        main()
