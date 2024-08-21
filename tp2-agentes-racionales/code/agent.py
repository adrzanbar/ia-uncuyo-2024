import random

class Agent:
    def __init__(self, env):
        """
        Inicializa el agente con el entorno dado.
        """
        self.env = env

    def up(self):
        """
        Mueve el agente hacia arriba.
        """
        self.env.accept_action('Arriba')

    def down(self):
        """
        Mueve el agente hacia abajo.
        """
        self.env.accept_action('Abajo')

    def left(self):
        """
        Mueve el agente hacia la izquierda.
        """
        self.env.accept_action('Izquierda')

    def right(self):
        """
        Mueve el agente hacia la derecha.
        """
        self.env.accept_action('Derecha')

    def suck(self):
        """
        Limpia la celda actual.
        """
        self.env.accept_action('Limpiar')

    def idle(self):
        """
        No hace nada.
        """
        self.env.accept_action('NoHacerNada')

    def perspective(self):
        """
        Sensar el entorno actual del agente.
        """
        return self.env.is_dirty()

    def think(self):
        """
        Implementa la lógica de decisiones del agente.
        """
        if self.perspective():
            self.suck()
        else:
            # Mueve aleatoriamente si no hay suciedad
            action = random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha'])
            if action == 'Arriba':
                self.up()
            elif action == 'Abajo':
                self.down()
            elif action == 'Izquierda':
                self.left()
            elif action == 'Derecha':
                self.right()
