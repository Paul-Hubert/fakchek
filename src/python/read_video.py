import cv2
import pygame
import numpy as np
import time

def show_video(video_path, audio_path):


    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erreur : impossible d'ouvrir la vidéo.")
        exit()

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # ⬇️ Initialisation de Pygame (affichage + audio)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # Initialiser le système audio
    pygame.mixer.init()

    # Charger l'audio (ça peut être la même vidéo si le format est supporté)
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Chargement image à afficher à un moment donné
    image_surface = pygame.image.load("no.png").convert_alpha()
    image_intervals = [(5, 8)]
    image_position = (0, 0)

    frame_idx = 0
    start_time = time.time()
    running = True

    while running:
        ret, frame = cap.read()
        if not ret:
            break

        # Calcul du temps écoulé
        elapsed = time.time() - start_time

        # Convertir et afficher la frame vidéo
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(np.rot90(frame_rgb))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(frame_surface, (0, 0))

        # Affichage conditionnel de l’image
        for start, end in image_intervals:
            if start <= elapsed <= end:
                screen.blit(image_surface, image_position)

        pygame.display.flip()
        clock.tick(fps)
        frame_idx += 1

    # Nettoyage
    cap.release()
    pygame.mixer.music.stop()
    pygame.quit()
