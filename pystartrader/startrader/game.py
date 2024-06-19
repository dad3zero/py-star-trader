from pystartrader.startrader import galaxy

planet_colors = {galaxy.EvolutionLevel.COSMOPOLITAN: "red",
                 galaxy.EvolutionLevel.DEVELOPED: "blue",
                 galaxy.EvolutionLevel.UNDERDEVELOPED: "grey",
                 galaxy.EvolutionLevel.FRONTIER: "green",
                 }

def start(star_system):
    import pygame

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        center = (screen.get_width() / 2, screen.get_height() /2)

        for planet in star_system:
            x = center[0] + (planet.x * 2)
            y = center[1] - (planet.y * 2)
            planet_pos = pygame.Vector2(x, y)
            pygame.draw.circle(screen, planet_colors[planet.level], planet_pos, 10)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

