import pygame

from board import Board

barH = 30
screenW = 640
screenH = 512 + barH

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
        lives=3
        board_valid=True
        end_font=pygame.font.SysFont('Corbel',72)
        button_font=pygame.font.SysFont('Corbel',40)
        play_again_rect=pygame.Rect(screenW//2-100,
                                    screenH//2-30,
                                    200,60)
        def handle_move_result():
            nonlocal lives, board_valid, in_progress, game_over, win
            new_valid=board.check_board()
            sel_r,sel_c=board.selectR, board.selectC
            if not new_valid:
                lives=lives-1
                print(f"Wrong move! Lives remaining: {lives}")
                if 0<=sel_r<board.size and 0<=sel_c<board.size:
                    board.cells[sel_r][sel_c].set_wrong(True)
                if lives<=0:
                    in_progress=False
                    game_over=True
                    win=False
            else:
                if 0<=sel_r<board.size and 0<=sel_c<board.size:
                    board.cells[sel_r][sel_c].set_wrong(False)
            board_valid=new_valid
        while running:
            screen.fill("light blue")
            if game_start:
                # draw menu
                board = Board(screenW, screenH-barH, screen, difficulty)
                in_progress = True
                game_start = False
                board_valid=board.check_board()
            elif in_progress:
                board.draw()
                font = pygame.font.Font(None, 30)
                text_surface = font.render("Lives:", True, pygame.Color("black"))
                screen.blit(text_surface,(5, screenH - barH*3/4))
                for n in range(lives):
                    pygame.draw.circle(screen, pygame.Color("dark blue"), (85+n*30, screenH - barH/2), 10, 15)
                if board.is_full():
                    print("checking board")
                    if board.check_board():
                        win = True
                    game_over = True
                    in_progress = False
            elif game_over:
                msg = "You Win!" if win else "You Lose"
                text_surface = end_font.render(msg, True, (0, 0, 0))
                # Draw "You Win" / "You Lose" text
                screen.blit(
                    text_surface,
                    (screenW // 2 - text_surface.get_width() // 2,
                     screenH // 2 - 120),
                )
                pygame.draw.rect(screen, "green", play_again_rect)
                button_text = button_font.render("Play Again?", True, (255, 255, 255))
                screen.blit(
                    button_text,
                    (play_again_rect.x + (play_again_rect.width - button_text.get_width()) // 2,
                     play_again_rect.y + (play_again_rect.height - button_text.get_height()) // 2),
                )

            #EVENTS
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                elif in_progress:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if digit != 0:
                            #NEEDS TO CHECK FOR IF ENTErED OR NOT
                            board.clear()
                        board.unselect()
                        digit = 0
                        board.select(
                            board.click(event.pos[0],event.pos[1])[0],
                            board.click(event.pos[0],event.pos[1])[1]
                        )
                    elif event.type == pygame.KEYDOWN:
                        if chr(event.key).isdigit() and int(event.key)!=48:
                            digit = int(chr(event.key))
                            board.sketch(digit)
                            print(f"Number pressed: {digit}")
                        elif event.key == pygame.K_RETURN:
                            if digit != 0:
                                board.place_number(digit)
                                handle_move_result()
                                board.unselect()
                                print("Enter")
                        elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                            print("Delete")
                            board.clear()
                            sel_r,sel_c=board.selectR,board.selectC
                            if 0<=sel_r<board.size and 0<=sel_c<board.size:
                                board.cells[sel_r][sel_c].set_wrong(False)
                            digit=0
                elif game_over:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if play_again_rect.collidepoint(event.pos):
                            running=False
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
                main(difficulty)
                pygame.init()
                screen=pygame.display.set_mode((screenW, screenH))
        else:
            pygame.draw.rect(screen, "green", [ez_button_x, ez_button_y, mid_button_width, mid_button_height])
        if mid_button_x <= mouse[0] <= mid_button_x + mid_button_width and mid_button_y <= mouse[1] <= mid_button_y + mid_button_height:
            pygame.draw.rect(screen, "light yellow", [mid_button_x, mid_button_y, mid_button_width, mid_button_height])
            if pygame.mouse.get_pressed()[0]:
                difficulty = "medium"
                main(difficulty)
                pygame.init()
                screen=pygame.display.set_mode((screenW, screenH))
        else:
            pygame.draw.rect(screen, "orange", [mid_button_x, mid_button_y, mid_button_width, mid_button_height])

        if hrd_button_x <= mouse[0] <= hrd_button_x + hrd_button_width and hrd_button_y <= mouse[1] <= hrd_button_y + hrd_button_height:
            pygame.draw.rect(screen, "pink", [hrd_button_x, hrd_button_y, hrd_button_width, hrd_button_height])
            if pygame.mouse.get_pressed()[0]:  # Left mouse click
                difficulty = "hard"
                main(difficulty)
                pygame.init()
                screen=pygame.display.set_mode((screenW, screenH))
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
