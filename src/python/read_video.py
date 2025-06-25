import cv2
import pygame
import numpy as np
import time

def show_video(is_true, video_path, audio_path):

    cap = cv2.VideoCapture(video_path)
    print(video_path)
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

    # ✅ Maintenant on peut charger et convertir l’image
    image_surface = pygame.image.load("dinguerie.png").convert_alpha()
    # Resize image to width=100, height=100 (adjust as needed)
    image_surface = pygame.transform.scale(image_surface, (150, 100))
    padding = 10
    image_position = (width - image_surface.get_width() - padding, padding)

    qr_surface = pygame.image.load("QR_code.png").convert_alpha()
    # Resize image to width=100, height=100 (adjust as needed)
    qr_surface = pygame.transform.scale(qr_surface, (100, 100))
    padding = 110
    qr_position = (width - image_surface.get_width()+10, padding)


    # Initialiser le système audio
    pygame.mixer.init()

    # Charger l'audio (ça peut être la même vidéo si le format est supporté)
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

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
        frame_surface = pygame.surfarray.make_surface(np.transpose(frame_rgb, (1, 0, 2)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(frame_surface, (0, 0))

        # Affichage conditionnel de l’image
        image_intervals=[(11,14), (21,25)]
        for start, end in image_intervals:
            if start <= elapsed <= end:
                screen.blit(image_surface, image_position)
                screen.blit(qr_surface, qr_position)

        pygame.display.flip()
        clock.tick(fps)
        frame_idx += 1

    # Nettoyage
    cap.release()
    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    video_path = "C:\\Users\\Simo\\Documents\\Python_Scripts\\Fakcheck\\fakchek\\trump_fakcheck.mp4"   # Chemin vers la vidéo
    audio_path = "C:\\Users\\Simo\\Documents\\Python_Scripts\\Fakcheck\\fakchek\\audio.wav"  # Chemin vers l'audio
    is_true = True  # Variable pour contrôler l'affichage de l'image

    show_video(is_true, video_path, audio_path)