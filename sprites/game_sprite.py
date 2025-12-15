import pygame
from abc import ABC, abstractmethod
import os


class GameSprite(pygame.sprite.Sprite, ABC):
    def __init__(self, image_path):
        super().__init__()
        self.image = self.load_img(image_path)

    def load_img(self, name):
        # Assuming all images are located in the assets folder
        path = os.path.join("assets\PNG", name)
        try:
            # convert_alpha() is crucial as it preserves the image's transparent background.
            return pygame.image.load(path).convert_alpha()
        except FileNotFoundError:
            print(f"Error: 找不到图片 {path}")
            # If no image is found, return a red square as a fallback to prevent the program from crashing.
            surf = pygame.Surface((30, 30))
            surf.fill((255, 0, 0))
            return surf

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
