
from controle_tabuleiro import ControleTabuleiro
from controle_player import ControlePlayer
from telas.tela_central import TelaCentral


class ControleCentral:
    def __init__(self):
        self.__controle_player = ControlePlayer(self)
        self.__controle_tabuleiro = ControleTabuleiro(self)
        self.__tela_central = TelaCentral()

    def chama_controlador_player(self):
        self.__controle_player.abre_tela_player()

    def chama_controlador_tabuleiro(self):
        self.__controle_tabuleiro.abre_tela_jogo()

    def inicia_programa(self):
        while True:
            opcao_escolhida = self.__tela_central.mostrar_opcoes()
            if opcao_escolhida == 1:
                self.chama_controlador_player()
                break
            elif opcao_escolhida == 2:
                self.chama_controlador_tabuleiro()
                break
            else:
                print("digite a opcao correta!")

            

