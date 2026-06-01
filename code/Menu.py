import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from Const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_RED, COLOR_YELLOW

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (800, 600))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option: int = 0
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Rise", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(50, "of the", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2), 120))
            self.menu_text(50, "Fallen", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2), 170))
            self.menu_text(16, "COMO JOGAR", COLOR_BLACK, (720, 50))
            self.menu_text(12, "SETAS - MOVIMENTO", COLOR_BLACK, (720, 75))
            self.menu_text(12, "NUMPAD 1 - ATAQUE 1", COLOR_BLACK, (720, 95))
            self.menu_text(12, "NUMPAD 2 - ATAQUE 2", COLOR_BLACK, (720, 115))
            self.menu_text(12, "NUMPAD 0 - DEFESA", COLOR_BLACK, (720, 135))
            self.menu_text(12, "ENTER - SELECIONAR", COLOR_BLACK, (720, 155))
            self.menu_text(12, "ESC - SAI DA TELA SCORE", COLOR_BLACK, (720, 175))
            self.menu_text(
                14,
                "Desenvolvedor: Douglas H. Milech",
                text_color=COLOR_BLACK,
                text_center_pos=(120, 580)
            )
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], text_color=COLOR_YELLOW,
                                   text_center_pos=((WIN_WIDTH / 2), 500 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], text_color=COLOR_RED,
                                   text_center_pos=((WIN_WIDTH / 2), 500 + 30 * i))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)