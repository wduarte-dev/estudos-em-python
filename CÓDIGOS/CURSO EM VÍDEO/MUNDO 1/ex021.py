#faça um programa em python que leia um arquivo .mp3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('SOAD_Toxicity.mp3')
pygame.mixer.music.play()

