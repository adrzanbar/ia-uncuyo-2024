import random

class Environment:
    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        """
        Inicializa el entorno con las dimensiones dadas, posición inicial del agente y tasa de suciedad.
        """
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.agent_posX = init_posX
        self.agent_posY = init_posY
        self.dirt_rate = dirt_rate
        self.grid = self.initialize_grid()
        self.clean_cells = set()  # Set de celdas que han sido limpiadas
        self.action_count = 0

    def initialize_grid(self):
        """
        Inicializa la cuadrícula con suciedad según la tasa de suciedad.
        """
        grid = [[0 for _ in range(self.sizeX)] for _ in range(self.sizeY)]
        num_dirty_cells = int(self.sizeX * self.sizeY * self.dirt_rate)
        dirty_cells = random.sample([(x, y) for x in range(self.sizeX) for y in range(self.sizeY)], num_dirty_cells)
        for (x, y) in dirty_cells:
            grid[y][x] = 1
        return grid

    def accept_action(self, action):
        """
        Acepta una acción del agente y actualiza el entorno en consecuencia.
        """
        if self.action_count >= 1000:
            return

        if action == 'Arriba':
            if self.agent_posY > 0:
                self.agent_posY -= 1
        elif action == 'Abajo':
            if self.agent_posY < self.sizeY - 1:
                self.agent_posY += 1
        elif action == 'Izquierda':
            if self.agent_posX > 0:
                self.agent_posX -= 1
        elif action == 'Derecha':
            if self.agent_posX < self.sizeX - 1:
                self.agent_posX += 1
        elif action == 'Limpiar':
            if self.is_dirty():
                self.clean_cells.add((self.agent_posX, self.agent_posY))
                # Mark the cell as cleaned in the grid
                self.grid[self.agent_posY][self.agent_posX] = 0
        elif action == 'NoHacerNada':
            pass
        else:
            raise ValueError("Acción no válida")

        self.action_count += 1

    def is_dirty(self):
        """
        Verifica si la celda actual contiene suciedad.
        """
        return self.grid[self.agent_posY][self.agent_posX] == 1

    def get_performance(self):
        """
        Devuelve la medida de rendimiento del agente.
        """
        return len(self.clean_cells)

    def print_environment(self):
        """
        Imprime la cuadrícula del entorno con el agente y las celdas limpias.
        """
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                if (x, y) == (self.agent_posX, self.agent_posY):
                    print('A', end=' ')
                elif (x, y) in self.clean_cells:
                    print('.', end=' ')
                else:
                    print('D' if self.grid[y][x] == 1 else '-', end=' ')
            print()
        print()
