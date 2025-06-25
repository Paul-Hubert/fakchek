import cv2
import pygame
import numpy as np

# Chargement vidéo
video_path = "trump_fakcheck.mp4"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Erreur : impossible d'ouvrir la vidéo.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# ⬇️ Initialise d'abord Pygame et la fenêtre
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# ✅ Maintenant on peut charger et convertir l’image
image_surface = pygame.image.load("dinguerie.png").convert_alpha()
# Resize image to width=100, height=100 (adjust as needed)
image_surface = pygame.transform.scale(image_surface, (150, 100))
padding = 10
image_position = (width - image_surface.get_width() - padding, padding)


# Intervalles d’affichage de l’image (secondes)
image_intervals = [(5, 8), (12, 14)]

running = True
frame_idx = 0

while running:
    ret, frame = cap.read()
    if not ret:
        break

    time_sec = frame_idx / fps
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_surface = pygame.surfarray.make_surface(np.transpose(frame_rgb, (1, 0, 2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(frame_surface, (0, 0))

    for start, end in image_intervals:
        if start <= time_sec <= end:
            screen.blit(image_surface, image_position)

    pygame.display.flip()
    clock.tick(fps)
    frame_idx += 1

cap.release()
pygame.quit()
