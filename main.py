#Créé par Enzo Sanchez Valero
#Créé le 30/10/23
#Introduction à arcade

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        pass

    def setup(self):
        pass

    def on_update(self, delta_time: float):
        rayon_cercle = 20
        cercle_x = 0
        cercle_y = 0

        cercle_x += 3
        cercle_y += 3

        cercle_change_x = 3  # Nombre d'unité pour le déplacement sur l'axe des X
        cercle_change_y = 3  # Nombre d'unité pour le déplacement sur l'axe des Y

        cercle_x += cercle_change_x
        cercle_y += cercle_change_y
        if cercle_x < rayon_cercle:
            pass
        if cercle_x > SCREEN_WIDTH - rayon_cercle:
            pass
        if cercle_y < rayon_cercle:
            pass
        if cercle_y > SCREEN_HEIGHT - rayon_cercle:
            pass
        if cercle_x < rayon_cercle:
            cercle_x *= -1

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(100, 100, 20, (255, 54, 34))


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()

main()

