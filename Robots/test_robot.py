from robots import Robot

r1 = Robot(4, 10, 'est', 'Robert', 'Humanoide', 'En service')
print('r1 =', r1)
r2 = Robot(15, 7, 'sud', 'Juliette', 'Mobile', 'En service')
print('r2 =', r2)

r1.nom = "D2R2"  # on a ajouté un nom à r1 mais r2 n'a pas de nom


def tourner_gauche(robot):
    robot.direction = (robot.direction + 3) % 4

    Robot.pivoter_gauche = tourner_gauche

    r2.pivoter_gauche()  # direction devient 'est'
    print('r2 =', r2)
