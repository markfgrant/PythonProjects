import pygame

width = 1000
height = 1000
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

def redrawWindow(win,player):
    win.fill((255,255,255))
    player.draw()
    pygame.display.update()


def main():
    run = True
    p=[]
    NumOfPlayers = 3
    player1 = Player(players / width, 50, 100, 100, (0, 255, 0))
    player2 = Player(players / width, 50, 100, 100, (0, 255, 0))
    player3 = Player(players / width, 50, 100, 100, (0, 255, 0))
    player4 = Player(players / width, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        redrawWindow(win,p)

main()