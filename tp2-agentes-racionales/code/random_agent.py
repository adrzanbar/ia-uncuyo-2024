import random
from agent import Agent

class RandomAgent(Agent):
    def __init__(self, env):
        """
        Inicializa el agente aleatorio con el entorno dado.
        """
        super().__init__(env)

    def think(self):
        """
        Implementa la lógica de decisiones del agente de manera aleatoria.
        """
        action = random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha', 'Limpiar', 'NoHacerNada'])
        if action == 'Arriba':
            self.up()
        elif action == 'Abajo':
            self.down()
        elif action == 'Izquierda':
            self.left()
        elif action == 'Derecha':
            self.right()
        elif action == 'Limpiar':
            self.suck()
        elif action == 'NoHacerNada':
            self.idle()
        else:
            raise ValueError("Acción no válida")
