import pygame

from board import Board

screenW = 640
screenH = 512

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((screenW, screenH))
        clock = pygame.time.Clock()
        running = True
        game_start = True
        in_progress = False
        game_over = False
        win = False
        digit = 0
        while running:
            screen.fill("light blue")
            if game_start:
                # draw menu
                board = Board(screenW, screenH, screen, -1)
                in_progress = True
                game_start = False
            elif in_progress:
                board.draw()
                if board.is_full():
                    print("checking board")
                    if board.check_board():
                        win = True
                    game_over = True
                    in_progress = False
            elif game_over:
                if win:
                    print("YOU WIN")
                else:
                    print("YOU LOSE")
                print("PLAY AGAIN?")

            #EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif in_progress:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if digit != 0:
                            board.place_number(digit)
                        board.unselect()
                        digit = 0
                        board.select(board.click(event.pos[0], event.pos[1])[0], board.click(event.pos[0], event.pos[1])[1])
                    elif event.type == pygame.KEYDOWN:
                        if chr(event.key).isdigit() and int(event.key)!=48:
                            digit = int(chr(event.key))
                            board.sketch(digit)
                            print(f"Number pressed: {digit}")
                        elif event.key == pygame.K_RETURN:
                            board.place_number(digit)
                            board.unselect()
                            print("Enter")
                        elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                            print("Delete")
                            board.clear()
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()