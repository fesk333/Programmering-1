import pygame
from pygame.locals import *
import random

pygame.init()
H = 800
B = 600

fivescore = []

clock = pygame.time.Clock()
Landing_timer = 0
win = pygame.display.set_mode((H,B))






######## Startup screen and ending screen #########
font = pygame.font.SysFont(None, 48)
def startup_screen(firstname, lastname):
    waiting = True
    while waiting:
        win.fill((0,0,0))


        title_text = font.render(f"Welcome captain {firstname} {lastname}", True, (255, 255, 255))
        instruction_text = font.render("Press SPACE to Start", True, (255, 255, 255))
        win.blit(title_text, (H//2 - title_text.get_width()//2, B//3))
        win.blit(instruction_text, (H//2 - instruction_text.get_width()//2, B//2))
        pygame.display.flip()
        event = pygame.event.wait()
        if event.type == QUIT:
            waiting = False
        elif event.type == KEYDOWN and event.key == K_SPACE:
            waiting = False

def ending_screen(message, score):
    waiting = True

    if len(fivescore) < 5:
        fivescore.append(score)
        average_score = sum(fivescore) / len(fivescore)
    else:
        fivescore.remove(fivescore[0])
        fivescore.append(score)
        average_score = sum(fivescore) / len(fivescore)
    

    while waiting:
        win.fill((0,0,0))
        title_text = font.render(f"You {message}", True, (255, 255, 255))
        win.blit(title_text, (H//2 - title_text.get_width()//2, B//3))
        score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
        win.blit(score_text, (H//2 - score_text.get_width()//2, B//3 + 50))
        if len(fivescore) > 0:
            highscore_text = font.render(f"Average score (over 5 games): {average_score:.2f}", True, (255, 255, 255))
            win.blit(highscore_text, (H//2 - highscore_text.get_width()//2, B//3 + 100))
        continuation_text = font.render("Press SPACE to Continue", True, (255, 255, 255))
        win.blit(continuation_text, (H//2 - continuation_text.get_width()//2, B//2 + 100))

        pygame.display.flip()
        event = pygame.event.wait()
        if event.type == QUIT:
            waiting = False
        elif event.type == KEYDOWN and event.key == K_SPACE:
            waiting = False
            repeat_game(True)

    
def repeat_game(restart):
    if restart:
        start_game()
    else:
        pygame.quit()
        

    





############ Physics ########
gravity = 1.2

    #colission detection
def check_collision(rocket_pos, surface_points, left_landing_gear_pos, right_landing_gear_pos):
    rocket_x, rocket_y = rocket_pos
    for i in range(len(surface_points) - 1):
        p1 = surface_points[i]
        p2 = surface_points[i + 1]
        if p1[0] <= rocket_x <= p2[0]:
            # Linear interpolation to find the y value on the surface at rocket_x
            surface_y = p1[1] + (p2[1] - p1[1]) * (rocket_x - p1[0]) / (p2[0] - p1[0])
            if rocket_y >= surface_y:
                return True
            if left_landing_gear_pos[1] >= surface_y:
                return True
            if right_landing_gear_pos[1] >= surface_y:
                return True
    
                
    return False


def start_game():

    
    Landing_timer = 0
    score = 1000
    
    run = True


    firstnames = ["Gruggle", "Bert", "Bob", "Alred", "Zorg", "Onion", "Gurt", "Mentos"]
    lastnames = ["the first", "the second", "the third", "the 1623rd", "Strindberg", "Kennedy", "uh. . . .", "Mcdoogle"]
    firstname = random.choice(firstnames)
    lastname = random.choice(lastnames)

    endings = ["crashed!", "uh. . . got eaten by aliens?", "Ate lunar dust", "failed Newton's laws", "found the lunar dust's traction amazing", "expectedly, crashed", "had a skillissiue", "got beaten by a rock", "landed in a not so soft manner"]
    ending = random.choice(endings)

    good_endings = ["stuck the landing like a pro!", "landed just by luck!", "you landed. . . somehow!", "uh, that's suprising", "landed", "made it!"]
    good_ending = random.choice(good_endings)


    startup_screen(firstname, lastname)

    ########### Rocket ########
    velocity_x = 0
    velocity_y = 0

    position_x = B/2 + random.randint(-50,50)
    position_y = H/10 + random.randint(-10,10)

    rocketwidth = int(H/25)
    rocketheight = int(B/13)

    rocket_angle = random.randint(-5,5) - 90

    thrust_power = 0.1
    side_power = 0.1
    side_angle_power = 1



    #Rocket body
    rocket_surf = pygame.Surface((rocketwidth, rocketheight), pygame.SRCALPHA)
    pygame.draw.rect(rocket_surf, (50,50,255), (0, 0, rocketwidth, rocketheight))

    #Rocket engine

    engine_surf = pygame.Surface((rocketwidth+60, rocketheight/4), pygame.SRCALPHA)
    pygame.draw.rect(engine_surf, (255,100,0), (0, 0, rocketwidth/4, rocketheight/3))



    ########### Landing gear ########

    landing_gear_angle = 50

    landing_gear_offset_x = rocketwidth
    landing_gear_offset_y = rocketheight + 10

    # Left

    Left_gear_surf = pygame.Surface((rocketwidth, rocketheight), pygame.SRCALPHA)
    pygame.draw.rect(Left_gear_surf, (150,75,0), (0, 0, rocketwidth/5, rocketheight/2))

    # Right

    Right_gear_surf = pygame.Surface((rocketwidth, rocketheight), pygame.SRCALPHA)
    pygame.draw.rect(Right_gear_surf, (150,75,0), (0, 0, rocketwidth/5, rocketheight/2))


    ########### Surface #######

    # Build a visible surface (terrain) using the window size correctly
    win_w, win_h = win.get_size()
    surface_nodes = 6
    surface_points = []

    for i in range(surface_nodes):
        # spread nodes across the screen width; use the window height for y
        x = win_w // 4 + random.randint(-100, 100) + i * (win_w // max(1, surface_nodes))
        y = win_h // 2 + random.randint(50, 150)
        surface_points.append((x, y))


    left_point = (0, win_h // 1.1)
    right_point = (win_w, win_h // 1.1)
    surface_points.insert(0, left_point)
    surface_points.append(right_point)

    for i in range(len(surface_points) - 1):
        poly = [surface_points[i], surface_points[i+1], (surface_points[i+1][0], win_h), (surface_points[i][0], win_h)]
        pygame.draw.polygon(win, (0, 0, 0), poly)

    Landcollision = False

    # Landing site #

    landing_variable = random.randint(1, surface_nodes - 2)
    landing_site_1 = surface_points[landing_variable]
    landing_site_2 = surface_points[landing_variable + 1]


    #################


    ############# rocket throw #############

    velocity_x = random.randint(-2,2)
    velocity_y = random.randint(-2,0)



    ########### Effects #########

    # rocket exhaust particles

    particle_list = []
    particle_lifetime = 30

    def create_particle(x, y, angle):
        speed = random.uniform(0.5, 2.0)
        direction = angle + random.uniform(-15, 15) + 180
        vel_x = speed * pygame.math.Vector2(1, 0).rotate(-direction).x
        vel_y = speed * pygame.math.Vector2(1, 0).rotate(-direction).y
        lifetime = particle_lifetime
        particle_list.append([x, y, vel_x, vel_y, lifetime])

    ############ Second player canon #########
    second_player_check = True

    if second_player_check:
        canon_position = random.choice(surface_points[1:-2]) 
        canon_image = pygame.image.load("C:\\Users\\fesk08001\\Pictures\\kanon.jpg")
        canon_image = pygame.transform.scale(canon_image, (50, 50))
        canon_angle = 0



    ###########################################

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
        keys = pygame.key.get_pressed()

        # Rotate with A/D keys
        if keys[K_w]:
            # Thrust in the direction the rocket is facing
            rad_angle = rocket_angle * (3.14159 / 180)
            thrust_x = -1 * thrust_power * pygame.math.Vector2(1, 0).rotate(-rocket_angle).x
            thrust_y = -1 * thrust_power * pygame.math.Vector2(1, 0).rotate(-rocket_angle).y
            velocity_x += thrust_x
            velocity_y += thrust_y
            # Create exhaust particles
            create_particle(position_x + (rocketheight/2) * pygame.math.Vector2(1, 0).rotate(-rocket_angle).x,
                            position_y - 50 + (rocketheight/2) * pygame.math.Vector2(1, 0).rotate(-rocket_angle).y,
                            rocket_angle + 180)
            score -= 1



        if Landcollision == False:
            if keys[K_a]:
                rocket_angle += side_angle_power
                velocity_x += side_power * 0.8
                velocity_y -= side_power * pygame.math.Vector2(1, 0).rotate(-rocket_angle).y * 0.2
                score -= 0.5
            elif keys[K_d]:
                rocket_angle -= side_angle_power
                velocity_x -= side_power * 0.8
                velocity_y -= side_power * pygame.math.Vector2(1, 0).rotate(-rocket_angle).y * 0.2
                score -= 0.5


        rocket_angle %= 360

        position_x += velocity_x
        position_y += velocity_y

        velocity_y += gravity * 0.05
        velocity_x -= velocity_x * 0.001

        rocket_velocity = (velocity_x ** 2 + velocity_y ** 2) ** 0.5

        left_landing_gear_pos = (position_x + landing_gear_offset_x * pygame.math.Vector2(1, 0).rotate(-rocket_angle).x,
                                 position_y + landing_gear_offset_y * pygame.math.Vector2(1, 0).rotate(-rocket_angle).y)
        right_landing_gear_pos = (position_x + landing_gear_offset_x * pygame.math.Vector2(1, 0).rotate(-rocket_angle).x,
                                  position_y + landing_gear_offset_y * pygame.math.Vector2(1, 0).rotate(-rocket_angle).y)

        ########### Game rules ###########

        # Out of bounds
        if (position_x+H/8) < 0 or (position_x-H/8) > H or (position_y+B/6) < 0 or position_y > B:
            run = False
            score -= 800
            ending_screen(ending, score)
            
        # Collision detection
        if check_collision((position_x, position_y + rocketheight / 2), surface_points, left_landing_gear_pos, right_landing_gear_pos):
            if rocket_velocity > 2.5:
                run = False
                score -= 700
                # explosion image

                explosion_image = pygame.image.load("C:\\Users\\fesk08001\\Pictures\\explosion.jpg")
                pygame.transform.scale(explosion_image, (H, B))
                win.blit((explosion_image), (position_x - H//4, position_y - B//4))
                pygame.display.flip()
                pygame.time.delay(1000)
                ending_screen(ending, score)
                
                
            else:
                Landcollision = True
                if rocket_velocity > 1:
                    velocity_x = velocity_x * 0.8
                    velocity_y = velocity_y * -0.8
                    #deform the landing gear
                    if landing_gear_angle > 30 and landing_gear_angle < 80:
                        landing_gear_angle = landing_gear_angle * random.uniform(0.5,0.8)
                        landing_gear_offset_x = landing_gear_offset_x * random.uniform(0.9,1.0)
                        landing_gear_offset_y = landing_gear_offset_y * random.uniform(0.9,1.0)
                        score -= 100


                else:
                    velocity_x = velocity_x * 0.2
                    velocity_y = velocity_y * 0.2

                if position_x > landing_site_1[0] or position_x < landing_site_2[0] and position_y > landing_site_1[1] - 10:
                    Landing_timer += 1
                else:
                    Landing_timer = 0

                if Landing_timer > 60:
                    ending_screen(good_ending, score)
                    run = False         
        else:
            Landcollision = False   


        ############ Second player canon #########

        if second_player_check:
            if keys[K_LEFT]:
                canon_angle += 2
            if keys[K_RIGHT]:
                canon_angle -= 2
            


    
        win.fill((0,0,0))
    
        # Rotate and draw the rocket
        rotated_rocket = pygame.transform.rotate(rocket_surf, rocket_angle)
        rocket_rect = rotated_rocket.get_rect(center=(int(position_x), int(position_y)))
        # Rotate and draw the engine
        rotated_engine = pygame.transform.rotate(engine_surf, rocket_angle +180)
        engine_rect = rotated_engine.get_rect(center=(int(position_x - (rocketheight/2) * pygame.math.Vector2(1, 0).rotate(-rocket_angle).x),
                                                      int(position_y - (rocketheight/2) * pygame.math.Vector2(1, 0).rotate(-rocket_angle).y)))
        win.blit(rotated_engine, engine_rect.topleft)
        win.blit(rotated_rocket, rocket_rect.topleft)

        # Landing gear: compute local offsets from rocket center, rotate them, then blit gears by center
        # Local offsets (relative to rocket center). Adjust these to move the gear pivots.
        local_left = pygame.math.Vector2(rocketwidth * 1.4, rocketheight * 0.35)
        local_right = pygame.math.Vector2(rocketwidth * 0.9, rocketheight * 0.00000001)

        # Rotate local offsets by rocket angle (use same sign convention as thrust math)
        rotated_local_left = local_left.rotate(-rocket_angle)
        rotated_local_right = local_right.rotate(-rocket_angle)

        # World positions for gear centers
        left_pos = (position_x + rotated_local_left.x, position_y + rotated_local_left.y)
        right_pos = (position_x + rotated_local_right.x, position_y + rotated_local_right.y)

        # Rotate gear surfaces so they angle relative to the rocket
        rotated_left_gear = pygame.transform.rotate(Left_gear_surf, rocket_angle + landing_gear_angle)
        left_gear_rect = rotated_left_gear.get_rect(center=(int(left_pos[0]), int(left_pos[1])))
        win.blit(rotated_left_gear, left_gear_rect.topleft)

        rotated_right_gear = pygame.transform.rotate(Right_gear_surf, rocket_angle - landing_gear_angle)
        right_gear_rect = rotated_right_gear.get_rect(center=(int(right_pos[0]), int(right_pos[1])))
        win.blit(rotated_right_gear, right_gear_rect.topleft)

        # Update and draw particles
        for particle in particle_list[:]:
            particle[0] += particle[2]
            particle[1] += particle[3]
            particle[4] -= 1
            pygame.draw.circle(win, (255, 150, 0), (int(particle[0]), (int(particle[1])+50)), 3)
            if particle[4] <= 0:
                particle_list.remove(particle)

        # Display the velocity
        velocity_text = font.render(f"Velocity: {rocket_velocity:.2f}", True, (255, 255, 255))
        win.blit(velocity_text, (10, 10))

    
        pygame.draw.line(win, (0, 255, 0), landing_site_1, landing_site_2, 10)
        pygame.draw.polygon(win, (255, 255, 255), surface_points)

        # Second player
        if second_player_check:
            canon_rotated = pygame.transform.rotate(canon_image, canon_angle)
            canon_rect = canon_rotated.get_rect(center=(int(canon_position[0]), int(canon_position[1])))
            win.blit(canon_rotated, canon_rect.topleft)

        pygame.display.flip()
        clock.tick(60)

repeat_game(True)