import pygame
from telas.tela import Tela
from dados.api import FaseService

class CriarFase(Tela):
    def __init__(self):
        super().__init__()
        self.fonte = pygame.font.SysFont("Arial", 24)

        self.nome = ""
        self.enunciado = ""
        self.opcoes = []

        self.campo_ativo = "nome"
        self.btn_nova_opcao = pygame.Rect(50, 295, 160, 40)
        self.btn_salvar = pygame.Rect(50, 600, 200, 50)

        self.mensagem = ""
        self.cor_mensagem = (255, 255, 255)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.btn_nova_opcao.collidepoint(event.pos):
                from telas.criar_opcao import CriarOpcao
                return CriarOpcao(self)

            if self.btn_salvar.collidepoint(event.pos):
                self.enviar_para_backend()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.campo_ativo = "enunciado" if self.campo_ativo == "nome" else "nome"

            elif event.key == pygame.K_BACKSPACE:
                if self.campo_ativo == "nome":
                    self.nome = self.nome[:-1]
                else:
                    self.enunciado = self.enunciado[:-1]

            else:
                if event.unicode.isprintable():
                    if self.campo_ativo == "nome":
                        self.nome += event.unicode
                    elif self.campo_ativo == "enunciado":
                        self.enunciado += event.unicode

        return None

    def enviar_para_backend(self):
        if not self.nome.strip():
            self.mensagem = "Informe o nome da fase."
            self.cor_mensagem = (255, 80, 80)
            return

        if not self.enunciado.strip():
            self.mensagem = "Informe o enunciado."
            self.cor_mensagem = (255, 80, 80)
            return

        payload = {
            "ordem": 1,  # depois você pode calcular dinamicamente
            "nome": self.nome,
            "enunciado": self.enunciado,
            "opcoes": self.opcoes,
            "totalEstrelas": 3,
            "estrelasParaAvancar": 1
        }

        resultado = FaseService.criar_fase(payload)

        if resultado is not None:
            self.mensagem = "Fase salva com sucesso!"
            self.cor_mensagem = (80, 220, 120)

            self.nome = ""
            self.enunciado = ""
            self.opcoes = []
        else:
            self.mensagem = "Erro ao salvar fase."
            self.cor_mensagem = (255, 80, 80)

    def desenhar(self, screen):
        screen.fill("#2C2448")

        titulo = self.fonte.render("Configuração da Fase", True, (255, 255, 255))
        screen.blit(titulo, (50, 30))

        label_nome = self.fonte.render("Nome do Desafio", True, (200, 200, 200))
        screen.blit(label_nome, (50, 95))
        pygame.draw.rect(screen, "#2F3356", (50, 125, 600, 40), border_radius=5)
        txt_n = self.fonte.render(
            self.nome + ("|" if self.campo_ativo == "nome" else ""),
            True,
            (255, 255, 255)
        )
        screen.blit(txt_n, (60, 130))

        label_enun = self.fonte.render("Pergunta (Enunciado)", True, (200, 200, 200))
        screen.blit(label_enun, (50, 185))
        pygame.draw.rect(screen, "#2F3356", (50, 215, 600, 40), border_radius=5)
        txt_e = self.fonte.render(
            self.enunciado + ("|" if self.campo_ativo == "enunciado" else ""),
            True,
            (255, 255, 255)
        )
        screen.blit(txt_e, (60, 220))

        label_opt = self.fonte.render("Alternativas", True, (200, 200, 200))
        screen.blit(label_opt, (50, 295))

        pygame.draw.rect(screen, "#4CAF50", self.btn_nova_opcao, border_radius=8)
        txt_novo = self.fonte.render("+ Adicionar", True, (255, 255, 255))
        screen.blit(txt_novo, (self.btn_nova_opcao.x + 10, self.btn_nova_opcao.y + 5))

        for i, opt in enumerate(self.opcoes):
            cor = "#4CAF50" if opt.get("correta") else (255, 255, 255)
            prefixo = "[CORRETA] " if opt.get("correta") else f"{i+1}. "
            texto = opt.get("texto", "")
            txt_surface = self.fonte.render(f"{prefixo}{texto}", True, cor)
            screen.blit(txt_surface, (60, 350 + (i * 40)))

        pygame.draw.rect(screen, "#5D4DA0", self.btn_salvar, border_radius=8)
        txt_save = self.fonte.render("SALVAR", True, (255, 255, 255))
        screen.blit(txt_save, (self.btn_salvar.x + 20, self.btn_salvar.y + 10))

        if self.mensagem:
            txt_msg = self.fonte.render(self.mensagem, True, self.cor_mensagem)
            screen.blit(txt_msg, (50, 560))