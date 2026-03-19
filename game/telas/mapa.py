import pygame
from telas.tela import Tela
from componentes.sidebar import Sidebar
from dados.api import FaseService
from telas.criar_fase import CriarFase

class Mapa(Tela):
    def __init__(self):
        super().__init__()

        self.sidebar = Sidebar(320, 720)
        self.fonte_titulo = pygame.font.SysFont("Arial", 28, bold=True)
        self.fonte_texto = pygame.font.SysFont("Arial", 22)

        self.casinha = pygame.image.load("assets/casinha.png").convert_alpha()
        self.casinha = pygame.transform.scale(self.casinha, (180, 180))
        self.casinha_pos = (500, 110)

        self.botao_proxima_fase = pygame.image.load("assets/botao_proxima_fase.png").convert_alpha()
        self.botao_proxima_fase = pygame.transform.scale(self.botao_proxima_fase, (80, 80))
        self.botao_proxima_fase_pos = (500, 400)
        self.rect_botao = self.botao_proxima_fase.get_rect(topleft=self.botao_proxima_fase_pos)

        self.fases = []
        self.cards_fases = []
        self.mensagem = ""

        self.carregar_fases()

    def carregar_fases(self):
        self.fases = FaseService.buscar_todas_fases() or []
        self.fases.sort(key=lambda f: f.get("ordem", 0))

        self.cards_fases = []
        x = 760
        y = 110
        largura = 430
        altura = 60
        espacamento = 15

        for fase in self.fases:
            rect = pygame.Rect(x, y, largura, altura)
            self.cards_fases.append({
                "rect": rect,
                "fase": fase
            })
            y += altura + espacamento

        if not self.fases:
            self.mensagem = "Nenhuma fase cadastrada."
        else:
            self.mensagem = f"{len(self.fases)} fase(s) carregada(s)."

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # botão da sidebar -> criar fase
            if self.sidebar.handle_event(event):
                return CriarFase()

            # botão visual do mapa -> abre a primeira fase cadastrada
            if self.rect_botao.collidepoint(mouse_pos):
                if len(self.fases) > 0:
                    fase_id = self.fases[0].get("faseId")
                    dados_da_api = FaseService.buscar_detalhes_fase(fase_id)

                    if dados_da_api:
                        from telas.fase import Fase
                        return Fase(dados_da_api)

            # clique em uma fase listada
            for item in self.cards_fases:
                if item["rect"].collidepoint(mouse_pos):
                    fase_id = item["fase"].get("faseId")
                    dados_da_api = FaseService.buscar_detalhes_fase(fase_id)

                    if dados_da_api:
                        from telas.fase import Fase
                        return Fase(dados_da_api)

        return None

    def update(self):
        pass

    def desenhar(self, screen):
        screen.fill("#3D3267")

        self.sidebar.desenhar(screen)
        screen.blit(self.casinha, self.casinha_pos)
        screen.blit(self.botao_proxima_fase, self.botao_proxima_fase_pos)

        titulo = self.fonte_titulo.render("Mapa de Fases", True, (255, 255, 255))
        screen.blit(titulo, (760, 40))

        subtitulo = self.fonte_texto.render(self.mensagem, True, (220, 220, 220))
        screen.blit(subtitulo, (760, 75))

        if not self.fases:
            aviso = self.fonte_texto.render("Crie uma fase pela sidebar.", True, (255, 220, 120))
            screen.blit(aviso, (760, 120))
            return

        for item in self.cards_fases:
            rect = item["rect"]
            fase = item["fase"]

            pygame.draw.rect(screen, "#2F3356", rect, border_radius=10)
            pygame.draw.rect(screen, "#5D4DA0", rect, width=2, border_radius=10)

            ordem = fase.get("ordem", 0)
            nome = fase.get("nome", "Sem nome")
            estrelas = fase.get("totalEstrelas", 0)

            texto_principal = self.fonte_texto.render(
                f"{ordem}. {nome}",
                True,
                (255, 255, 255)
            )
            texto_secundario = self.fonte_texto.render(
                f"⭐ {estrelas}",
                True,
                (200, 200, 200)
            )

            screen.blit(texto_principal, (rect.x + 15, rect.y + 10))
            screen.blit(texto_secundario, (rect.x + 15, rect.y + 32))