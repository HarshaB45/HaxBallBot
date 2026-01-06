import pygame
import sys
import math

pygame.init()

# ---------- World ----------
WORLD_W, WORLD_H = 100, 60
SCALE = 5
SCREEN_W, SCREEN_H = WORLD_W * SCALE, WORLD_H * SCALE

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("HaxBall-like Playground")
clock = pygame.time.Clock()

# ---------- Constants ----------
BOT_RADIUS = 2
BALL_RADIUS = 1

BOT_SPEED = 0.5
DRIBBLE_FORCE = 0.15
KICK_FORCE = 2.8
BALL_DAMPING = 0.99

GOAL_Y1, GOAL_Y2 = 20, 40

# ---------- Colors ----------
GREEN = (30, 160, 30)
WHITE = (255, 255, 255)
BLUE = (60, 120, 220)
RED = (220, 60, 60)
YELLOW = (240, 220, 70)

# ---------- Reset ----------
def reset():
    return [20, 30], [20, 20], [30, 25], [0.0, 0.0]

bot1, bot2, ball, ball_vel = reset()

def clamp_bot(bot):
    bot[0] = max(BOT_RADIUS, min(WORLD_W - BOT_RADIUS, bot[0]))
    bot[1] = max(BOT_RADIUS, min(WORLD_H - BOT_RADIUS, bot[1]))

KICK_RANGE = BOT_RADIUS + BALL_RADIUS + 1.2  # slightly bigger than collision

def collide(bot, kick):
    dx = ball[0] - bot[0]
    dy = ball[1] - bot[1]
    dist = math.hypot(dx, dy)
    nx, ny = dx / (dist + 1e-6), dy / (dist + 1e-6)

    # ---------- Solid collision (dribble) ----------
    min_dist = BOT_RADIUS + BALL_RADIUS
    if dist < min_dist:
        overlap = min_dist - dist
        ball[0] += nx * overlap
        ball[1] += ny * overlap
        ball_vel[0] += nx * DRIBBLE_FORCE
        ball_vel[1] += ny * DRIBBLE_FORCE

    # ---------- Forceful kick (independent of bot motion) ----------
    if kick and dist <= KICK_RANGE:
        # always override velocity, stationary or moving
        ball_vel[0] = nx * KICK_FORCE
        ball_vel[1] = ny * KICK_FORCE




# ---------- Main loop ----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player 1
    if keys[pygame.K_LEFT]:  bot1[0] -= BOT_SPEED
    if keys[pygame.K_RIGHT]: bot1[0] += BOT_SPEED
    if keys[pygame.K_UP]:    bot1[1] -= BOT_SPEED
    if keys[pygame.K_DOWN]:  bot1[1] += BOT_SPEED

    # Player 2
    if keys[pygame.K_a]: bot2[0] -= BOT_SPEED
    if keys[pygame.K_d]: bot2[0] += BOT_SPEED
    if keys[pygame.K_w]: bot2[1] -= BOT_SPEED
    if keys[pygame.K_s]: bot2[1] += BOT_SPEED

    clamp_bot(bot1)
    clamp_bot(bot2)

    # Collisions
    collide(bot1, kick=keys[pygame.K_SPACE])
    collide(bot2, kick=keys[pygame.K_x])

    # Move ball
    ball[0] += ball_vel[0]
    ball[1] += ball_vel[1]
    ball_vel[0] *= BALL_DAMPING
    ball_vel[1] *= BALL_DAMPING

    # Ball walls
    if ball[0] <= BALL_RADIUS or ball[0] >= WORLD_W - BALL_RADIUS:
        ball_vel[0] *= -1
    if ball[1] <= BALL_RADIUS or ball[1] >= WORLD_H - BALL_RADIUS:
        ball_vel[1] *= -1

    ball[0] = max(BALL_RADIUS, min(WORLD_W - BALL_RADIUS, ball[0]))
    ball[1] = max(BALL_RADIUS, min(WORLD_H - BALL_RADIUS, ball[1]))

    # Goal
    if ball[0] >= WORLD_W - BALL_RADIUS and GOAL_Y1 <= ball[1] <= GOAL_Y2:
        print("GOAL!")
        bot1, bot2, ball, ball_vel = reset()

    # ---------- Draw ----------
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_W, SCREEN_H), 3)
    pygame.draw.rect(screen, YELLOW,
        (SCREEN_W - 6, GOAL_Y1 * SCALE, 6, (GOAL_Y2 - GOAL_Y1) * SCALE))

    pygame.draw.circle(screen, BLUE, (int(bot1[0]*SCALE), int(bot1[1]*SCALE)), BOT_RADIUS*SCALE)
    pygame.draw.circle(screen, BLUE, (int(bot2[0]*SCALE), int(bot2[1]*SCALE)), BOT_RADIUS*SCALE)
    pygame.draw.circle(screen, RED,  (int(ball[0]*SCALE), int(ball[1]*SCALE)), BALL_RADIUS*SCALE)

    pygame.display.flip()
    clock.tick(60)
