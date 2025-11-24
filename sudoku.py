import pygame

from board import Board

screenW = 640
screenH = 512

def main(difficulty):
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
                board = Board(screenW, screenH, screen, difficulty)
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
    pygame.init()
    DARK_BLUE = (0, 0, 139)
    WHITE = (255, 255, 255)
    LIGHT_BLUE = (173, 216, 230)
    font = pygame.font.SysFont('Corbel', 50)
    titlefont = pygame.font.SysFont('Corbel', 80)
    title_text = titlefont.render('SUDOKU', True, WHITE)
    ez_text = font.render('Easy', True, WHITE)
    mid_text = font.render('Medium', True, WHITE)
    hrd_text = font.render('Hard', True, WHITE)
    screen = pygame.display.set_mode((screenW, screenH))
    running = True
    difficulty = "easy"

    while running:
        screen.fill("light blue")
        mouse = pygame.mouse.get_pos()

        # Button dimensions
        ez_button_x, ez_button_y = 220, 140
        ez_button_width, ez_button_height = 200, 80

        mid_button_x, mid_button_y = 220, 284
        mid_button_width, mid_button_height = 200, 80

        hrd_button_x, hrd_button_y = 220, 428
        hrd_button_width, hrd_button_height = 200, 80

        # Check if mouse is over the button
        if ez_button_x <= mouse[0] <= ez_button_x + ez_button_width and ez_button_y <= mouse[1] <= ez_button_y + ez_button_height:
            pygame.draw.rect(screen, "light green", [ez_button_x, ez_button_y, ez_button_width, ez_button_height])
            if pygame.mouse.get_pressed()[0]:
                difficulty = "easy"
                break
        else:
            pygame.draw.rect(screen, "green", [ez_button_x, ez_button_y, mid_button_width, mid_button_height])
        if mid_button_x <= mouse[0] <= mid_button_x + mid_button_width and mid_button_y <= mouse[1] <= mid_button_y + mid_button_height:
            pygame.draw.rect(screen, "light yellow", [mid_button_x, mid_button_y, mid_button_width, mid_button_height])
            if pygame.mouse.get_pressed()[0]:
                difficulty = "medium"
                break
        else:
            pygame.draw.rect(screen, "orange", [mid_button_x, mid_button_y, mid_button_width, mid_button_height])

        if hrd_button_x <= mouse[0] <= hrd_button_x + hrd_button_width and hrd_button_y <= mouse[1] <= hrd_button_y + hrd_button_height:
            pygame.draw.rect(screen, "pink", [hrd_button_x, hrd_button_y, hrd_button_width, hrd_button_height])
            if pygame.mouse.get_pressed()[0]:  # Left mouse click
                difficulty = "hard"
                break
        else:
            pygame.draw.rect(screen, "red", [hrd_button_x, hrd_button_y, hrd_button_width, hrd_button_height])


        # Render text on the button
        screen.blit(ez_text, (ez_button_x + 50, ez_button_y + 15))
        screen.blit(mid_text, (mid_button_x + 15, mid_button_y + 15))
        screen.blit(hrd_text, (hrd_button_x + 50, hrd_button_y + 15))
        screen.blit(title_text, (170, 10))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    if running:
        main(difficulty)