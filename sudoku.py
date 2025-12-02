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
        quit_rect = pygame.Rect(screenW // 2 - 100,
                                screenH // 2 + 50,
                                200, 60)

        def handle_move_result():
            nonlocal lives, board_valid, in_progress, game_over, win
            new_valid=board.check_board()
            sel_r,sel_c=board.selectR, board.selectC
            if not new_valid:
                if 0 <= sel_r < board.size and 0 <= sel_c < board.size and not board.cells[sel_r][sel_c].wrong:
                    lives -= 1

                print(f"Wrong move! Lives remaining: {lives}")
                if 0<=sel_r<board.size and 0<=sel_c<board.size:
                    board.cells[sel_r][sel_c].set_wrong(True)
                if lives<=0:
                    in_progress=False
                    game_over=True
                    win=False
                    return
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
                if board.is_full() and board_valid:
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
                pygame.draw.rect(screen, "red", quit_rect)
                quit_text = button_font.render("Quit", True, (255, 255, 255))
                screen.blit(
                    quit_text,
                    (quit_rect.x + (quit_rect.width - quit_text.get_width()) // 2,
                     quit_rect.y + (quit_rect.height - quit_text.get_height()) // 2)
                )

            #EVENTS
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                elif in_progress:
                    try:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            board.unselect()
                            digit = 0
                            board.select(
                                board.click(event.pos[0],event.pos[1])[0],
                                board.click(event.pos[0],event.pos[1])[1]
                            )
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                new_selectedR, new_selectedC = board.selectR - 1, board.selectC
                                if new_selectedR == -1:
                                    new_selectedR = 8
                                board.unselect()
                                board.select(new_selectedR, new_selectedC)
                            elif event.key == pygame.K_DOWN:
                                new_selectedR, new_selectedC = board.selectR + 1, board.selectC
                                if new_selectedR == 9:
                                    new_selectedR = 0
                                board.unselect()
                                board.select(new_selectedR, new_selectedC)
                            elif event.key == pygame.K_LEFT:
                                new_selectedR, new_selectedC = board.selectR, board.selectC - 1
                                if new_selectedC == -1:
                                    new_selectedC = 8
                                board.unselect()
                                board.select(new_selectedR, new_selectedC)
                            elif event.key == pygame.K_RIGHT:
                                new_selectedR, new_selectedC = board.selectR, board.selectC + 1
                                if new_selectedC == 9:
                                    new_selectedC = 0
                                board.unselect()
                                board.select(new_selectedR, new_selectedC)
                            elif chr(event.key).isdigit() and int(event.key)!=48:
                                digit = int(chr(event.key))
                                board.sketch(digit)
                                board.cells[board.selectR][board.selectC].set_wrong(False)

                                print(f"Number pressed: {digit}")
                            elif event.key == pygame.K_RETURN:
                                if digit != 0:
                                    board.place_number(digit)
                                    handle_move_result()
                                    board.unselect()
                                    digit=0
                                    print("Enter")
                            elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                                print("Delete")
                                board.clear()
                                sel_r,sel_c=board.selectR,board.selectC
                                if 0<=sel_r<board.size and 0<=sel_c<board.size:
                                    board.cells[sel_r][sel_c].set_wrong(False)
                                digit=0
                    except Exception as e:
                        print(f"Invalid Key: {e}")
                elif game_over:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if play_again_rect.collidepoint(event.pos):
                            return "restart"
                        if quit_rect.collidepoint(event.pos):
                            return "quit"
            pygame.display.flip()
            continue
    finally:
        pass


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screenW, screenH))
    font = pygame.font.SysFont('Corbel', 50)
    titlefont = pygame.font.SysFont('Corbel', 80)
    ez_text = font.render('Easy', True, (255, 255, 255))
    mid_text = font.render('Medium', True, (255, 255, 255))
    hrd_text = font.render('Hard', True, (255, 255, 255))
    title_text = titlefont.render('SUDOKU', True, (255, 255, 255))

    # Difficulty menu function
    def difficulty_menu():
        while True:
            screen.fill("light blue")
            mouse = pygame.mouse.get_pos()

            ez_button = pygame.Rect(220, 140, 200, 80)
            mid_button = pygame.Rect(220, 284, 200, 80)
            hrd_button = pygame.Rect(220, 428, 200, 80)

            # EASY
            if ez_button.collidepoint(mouse):
                pygame.draw.rect(screen, "light green", ez_button)
            else:
                pygame.draw.rect(screen, "green", ez_button)

            # MEDIUM
            if mid_button.collidepoint(mouse):
                pygame.draw.rect(screen, "light yellow", mid_button)
            else:
                pygame.draw.rect(screen, "orange", mid_button)

            # HARD
            if hrd_button.collidepoint(mouse):
                pygame.draw.rect(screen, "pink", hrd_button)
            else:
                pygame.draw.rect(screen, "red", hrd_button)

            screen.blit(ez_text, (ez_button.x + 60, ez_button.y + 25))
            screen.blit(mid_text, (mid_button.x + 25, mid_button.y + 25))
            screen.blit(hrd_text, (hrd_button.x + 60, hrd_button.y + 25))
            screen.blit(title_text, (screenW/3.25, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ez_button.collidepoint(event.pos):
                        return "easy"
                    if mid_button.collidepoint(event.pos):
                        return "medium"
                    if hrd_button.collidepoint(event.pos):
                        return "hard"

            pygame.display.update()

    # MAIN LOOP (clean & correct)
    while True:
        difficulty = difficulty_menu()
        result = main(difficulty)
        if result == "quit":
            pygame.quit()
            quit()
