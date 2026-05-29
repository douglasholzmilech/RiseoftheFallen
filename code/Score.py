#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Database import Database
from Const import COLOR_WHITE


class Score:

    def __init__(self, window):
        self.window = window

    def run(self):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT points
            FROM score
            ORDER BY points DESC
            LIMIT 10
        """)

        scores = cursor.fetchall()

        conn.close()

        while True:

            self.window.fill((0, 0, 0))

            font = pygame.font.SysFont("Arial", 40)

            title = font.render(
                "TOP SCORES",
                True,
                COLOR_WHITE
            )

            self.window.blit(title, (250, 50))

            for i, score in enumerate(scores):

                txt = font.render(
                    f"{i+1} - {score[0]}",
                    True,
                    COLOR_WHITE
                )

                self.window.blit(
                    txt,
                    (300, 150 + i * 40)
                )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    return