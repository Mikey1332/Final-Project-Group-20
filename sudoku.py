import pygame

screenW = 640
screenH = 512

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((screenW, screenH))
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill("light green")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     grid_pos = convert_screen_to_grid(event.pos[0], event.pos[1])
            # screen.blit(mole_image, mole_image.get_rect(topleft=convert_grid_to_screen(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()