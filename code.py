import pygame
import numpy as np
import pickle

class GameOfLife:
    def __init__(self, width, height, n_cells_x, n_cells_y):
        pygame.init()

        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((width, height))

        self.n_cells_x, self.n_cells_y = n_cells_x, n_cells_y
        self.cell_width, self.cell_height = width // n_cells_x, height // n_cells_y

        self.colors = {'white': (255, 255, 255), 'black': (0, 0, 0),
                       'gray': (128, 128, 128), 'green': (0, 255, 0),
                       'button_clicked': (255, 0, 0), 'button_unclicked': (0, 255, 0)}

        self.button_width, self.button_height = 200, 50
        self.button_x, self.button_y = (width - self.button_width) // 2, height - self.button_height - 10
        self.save_button_x, self.save_button_y = self.button_x - self.button_width - 10, self.button_y
        self.load_button_x, self.load_button_y = self.button_x + self.button_width + 10, self.button_y

        self.running_simulation, self.simulation_delay, self.tick_interval = False, 100, 1
        self.game_state = np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=[0.8, 0.2])

        self.font = pygame.font.Font(None, 36)

    def draw_button(self):
        button_text = "Stop" if self.running_simulation else "Start"
        pygame.draw.rect(self.screen, self.colors['green'], (self.button_x, self.button_y, self.button_width, self.button_height))
        text = self.font.render(button_text, True, self.colors['black'])
        text_rect = text.get_rect(center=(self.button_x + self.button_width // 2, self.button_y + self.button_height // 2))
        self.screen.blit(text, text_rect)

    def draw_grid(self):
        for y in range(0, self.height, self.cell_height):
            for x in range(0, self.width, self.cell_width):
                cell = pygame.Rect(x, y, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, self.colors['gray'], cell, 1)

    def next_generation(self):
        if self.running_simulation:
            new_state = np.copy(self.game_state)

            for y in range(self.n_cells_y):
                for x in range(self.n_cells_x):
                    n_neighbors = np.sum(self.game_state[(x - 1):(x + 2) % self.n_cells_x, (y - 1):(y + 2) % self.n_cells_y]) - self.game_state[x, y]

                    if self.game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                        new_state[x, y] = 0
                    elif self.game_state[x, y] == 0 and n_neighbors == 3:
                        new_state[x, y] = 1

            self.game_state = new_state

    def draw_cells(self):
        for y in range(self.n_cells_y):
            for x in range(self.n_cells_x):
                cell = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                if self.game_state[x, y] == 1:
                    pygame.draw.rect(self.screen, self.colors['black'], cell)

    def draw_save_load_button(self, button_x, button_y, button_text, button_clicked):
        button_color = self.colors['button_clicked'] if button_clicked else self.colors['button_unclicked']
        pygame.draw.rect(self.screen, button_color, (button_x, button_y, self.button_width, self.button_height))
        text = self.font.render(button_text, True, self.colors['black'])
        text_rect = text.get_rect(center=(button_x + self.button_width // 2, button_y + self.button_height // 2))
        self.screen.blit(text, text_rect)

    def save_game_state(self):
        with open("game_state.pkl", "wb") as file:
            pickle.dump(self.game_state, file)

    def load_game_state(self):
        try:
            with open("game_state.pkl", "rb") as file:
                loaded_state = pickle.load(file)
                if loaded_state.shape == self.game_state.shape:
                    return loaded_state
                else:
                    print("Error: Incompatible game state dimensions.")
        except FileNotFoundError:
            print("Error: Save file not found.")
        return None

    def run(self):
        last_tick_time = pygame.time.get_ticks()
        running, save_button_clicked, load_button_clicked = True, False, False

        while running:
            self.screen.fill(self.colors['white'])
            self.draw_grid()
            self.draw_cells()
            self.draw_button()
            self.draw_save_load_button(self.save_button_x, self.save_button_y, "Save", save_button_clicked)
            self.draw_save_load_button(self.load_button_x, self.load_button_y, "Load", load_button_clicked)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_x <= event.pos[0] <= self.button_x + self.button_width and self.button_y <= event.pos[1] <= self.button_y + self.button_height:
                        self.running_simulation = not self.running_simulation
                    elif self.save_button_x <= event.pos[0] <= self.save_button_x + self.button_width and self.save_button_y <= event.pos[1] <= self.save_button_y + self.button_height:
                        save_button_clicked = True
                        self.save_game_state()
                    elif self.load_button_x <= event.pos[0] <= self.load_button_x + self.button_width and self.load_button_y <= event.pos[1] <= self.load_button_y + self.button_height:
                        load_button_clicked = True
                        loaded_state = self.load_game_state()
                        if loaded_state is not None:
                            self.game_state = loaded_state
                    elif not self.running_simulation:
                        x, y = event.pos[0] // self.cell_width, event.pos[1] // self.cell_height
                        self.game_state[x, y] = not self.game_state[x, y]

                if event.type == pygame.MOUSEBUTTONUP:
                    save_button_clicked = False
                    load_button_clicked = False

            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - last_tick_time

            if self.running_simulation and elapsed_time >= self.tick_interval * 1000:
                self.next_generation()
                last_tick_time = current_time

            pygame.time.delay(self.simulation_delay)

        pygame.quit()

# Initialize and run the game
game = GameOfLife(800, 600, 40, 30)
game.run()
