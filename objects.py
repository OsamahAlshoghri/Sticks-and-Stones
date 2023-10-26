from functions import *
from classes import *
from misc_var import *

player = Character()  # creates player object
web_grp = pg.sprite.Group()
artilleries = pg.sprite.Group()
web_grp_2 = pg.sprite.Group()
artilleries_2 = pg.sprite.Group()
web_grp_3 = pg.sprite.Group()
artilleries_3 = pg.sprite.Group()
web_grp_4 = pg.sprite.Group()
artilleries_4 = pg.sprite.Group()

'''
OSAMAH: START -->
'''
# level 1
platform_grp_1 = pg.sprite.Group()  # creates a group for platforms for the first level
create_platform(Platform, platform_grp_1, 3500, 20, 0, 490)
create_platform(Platform, platform_grp_1, 40, 1000, -50, 450)
create_platform(Platform, platform_grp_1, 200, 20, 200, 350)
create_platform(Platform, platform_grp_1, 100, 20, 200, 180)
create_platform(Platform, platform_grp_1, 150, 20, 730, 300)
create_platform(Platform, platform_grp_1, 150, 20, 1200, 300)
create_platform(Platform, platform_grp_1, 150, 20, 2100, 490)
create_platform(Platform, platform_grp_1, 10, 50, 1750, 490)
create_platform(Platform, platform_grp_1, 200, 20, 2550, 490)
create_platform(Platform, platform_grp_1, 40, 1000, 2650, 490)

enemies_grp_1 = pg.sprite.Group() # creates a group for enemies on the first level

create_enemy(Enemy, enemies_grp_1, 400, 500, 1)
a = create_enemy(Enemy, enemies_grp_1, 1400, 500, 2)
create_projectile_enemy(Projectile_Enemy, enemies_grp_1, 1200, 300, 0)
create_projectile_enemy(Projectile_Enemy, enemies_grp_1, 1200, 400, 1)
create_spikes(Spikes, enemies_grp_1, 700, 482)
create_spikes(Spikes, enemies_grp_1, 760, 482)


exits_grp_1 = pg.sprite.Group()
exits_grp_1.add(Finish(70, 200, 2550, 490))

coins_grp_1 = pg.sprite.Group()
consumables_grp_1 = pg.sprite.Group() 

idle_weapon_grp_1 = pg.sprite.Group()

def_groups_1 = [enemies_grp_1, platform_grp_1, exits_grp_1, coins_grp_1, consumables_grp_1]
'''
OSAMAH: END -->
'''

'''
OSAMAH: START -->
'''
#level 2
platform_grp_2 = pg.sprite.Group()
create_platform(Platform, platform_grp_2, 3000, 20, 0, 490)
create_platform(Platform, platform_grp_2, 40, 1000, -50, 450)
create_platform(Platform, platform_grp_2, 150, 20, 1300, 350)
create_platform(Platform, platform_grp_2, 200, 20, 1300, 200)
create_platform(Platform, platform_grp_2, 1700, 100, 2650, 490)
create_platform(Platform, platform_grp_2, 1000, 100, 2650, 390)
create_platform(Platform, platform_grp_2, 400, 100, 2650, 290)
create_platform(Platform, platform_grp_2, 500, 20, 3500, 490)
create_platform(Platform, platform_grp_2, 40, 1000, 3750, 450)


enemies_grp_2 = pg.sprite.Group()
create_spider(Spider, enemies_grp_2, web_grp, 60, 40, 350, -20, 3)
create_spider(Spider, enemies_grp_2, web_grp, 40, 20, 600, -100, 6)
create_spikes(Spikes, enemies_grp_2, 720, 482)
create_artillery(Artillery, enemies_grp_2, artilleries, 1000, 490)
create_spider(Spider, enemies_grp_2, web_grp, 60, 40, 1500, -20, 2)
create_artillery(Artillery, enemies_grp_2, artilleries, 2650, 240)
create_enemy(Enemy, enemies_grp_2, 2000, 30, 1)

exits_grp_2 = pg.sprite.Group()
exits_grp_2.add(Finish(70, 200, 3650, 481))

coins_grp_2 = pg.sprite.Group()
consumables_grp_2 = pg.sprite.Group() 

idle_weapon_grp_2 = pg.sprite.Group()

checkpoints_grp_2 = pg.sprite.Group()
checkpoints_grp_2.add(Checkpoint(55, 70, 1300, 191, 1))

def_groups_2 = [enemies_grp_2, web_grp, artilleries, platform_grp_2, exits_grp_2, coins_grp_2, consumables_grp_2, checkpoints_grp_2]
'''
OSAMAH: END -->
'''

'''
OSAMAH: START -->
'''
#level 3
platform_grp_3 = pg.sprite.Group()
create_platform(Platform, platform_grp_3, 400, 20, 200, 490)
create_platform(Platform, platform_grp_3, 200, 20, 400, 150)
create_platform(Platform, platform_grp_3, 200, 20, 900, 150)
create_platform(Platform, platform_grp_3, 400, 20, 1200, 490)
create_platform(Platform, platform_grp_3, 20, 1000, 1600, 550)
create_platform(Platform, platform_grp_3, 20, 1000, 1450, -250)
create_platform(Platform, platform_grp_3, 100, 20, 1800, 300)
create_platform(Platform, platform_grp_3, 400, 20, 2100, 490)
create_platform(Platform, platform_grp_3, 20, 1000, 2400, -200)
create_platform(Platform, platform_grp_3, 20, 1000, 2250, -250)
create_platform(Platform, platform_grp_3, 80, 20, 2290, 125)
create_platform(Platform, platform_grp_3, 600, 20, 2900, 490)
create_platform(Platform, platform_grp_3, 50, 300, 3100, 490)
create_platform(Platform, platform_grp_3, 50, 450, 3150, 490)
create_platform(Platform, platform_grp_3, 50, 700, 3200, 490)
create_platform(Platform, platform_grp_3, 100, 20, 2900, 200)
create_platform(Platform, platform_grp_3, 500, 20, 3600, 490)
create_platform(Platform, platform_grp_3, 50, 20, 3500, 250)
create_platform(Platform, platform_grp_3, 50, 20, 3700, 200)
create_platform(Platform, platform_grp_3, 200, 20, 4200, 490)
create_platform(Platform, platform_grp_3, 20, 1000, 4400, 550)
create_platform(Platform, platform_grp_3, 20, 1000, 4250, -250)
create_platform(Platform, platform_grp_3, 150, 20, 4600, 200)

enemies_grp_3 = pg.sprite.Group()
create_projectile_enemy(Projectile_Enemy, enemies_grp_3, 900, 150, 0)
for i in range(3):
    create_spikes(Spikes, enemies_grp_3, 1200 + (i * 60), 482)
create_spider(Spider, enemies_grp_3, web_grp_2, 60, 40, 1650, -20, 2)
create_artillery(Artillery, enemies_grp_3, artilleries_2, 2100, 480)
create_enemy(Enemy, enemies_grp_3, 3000, 490, 1)
create_projectile_enemy(Projectile_Enemy, enemies_grp_3, 3150, 340, 0)
create_projectile_enemy(Projectile_Enemy, enemies_grp_3, 3100, 90, 0)
create_artillery(Artillery, enemies_grp_3, artilleries_2, 3600, 480)
create_artillery(Artillery, enemies_grp_3, artilleries_2, 3500, 240)
create_artillery(Artillery, enemies_grp_3, artilleries_2, 3700, 190)


exits_grp_3 = pg.sprite.Group()
exits_grp_3.add(Finish(70, 200, 4600, 200))

coins_grp_3 = pg.sprite.Group()
consumables_grp_3 = pg.sprite.Group() 

idle_weapon_grp_3 = pg.sprite.Group()

checkpoints_grp_3 = pg.sprite.Group()
checkpoints_grp_3.add(Checkpoint(55, 70, 1800, 300, 1))
checkpoints_grp_3.add(Checkpoint(55, 70, 3200, 140, 2))

def_groups_3 = [enemies_grp_3, platform_grp_3, checkpoints_grp_3, exits_grp_3, coins_grp_3, consumables_grp_3, web_grp_2]
'''
OSAMAH: END -->
'''

'''
ABDULLAH: START -->
'''
# level 4
platform_grp_4 = pg.sprite.Group()
create_platform(Platform, platform_grp_4, 5300, 30, 50, 500)
create_platform(Platform, platform_grp_4, 30, 1000, 100, 500)
create_platform(Platform, platform_grp_4, 125, 30, 215, 350)
create_platform(Platform, platform_grp_4, 125, 30, 215, 150)
create_platform(Platform, platform_grp_4, 125, 30, 515, 270)
create_platform(Platform, platform_grp_4, 50, 280, 750, 500)
create_platform(Platform, platform_grp_4, 50, 280, 1101, 500)
create_platform(Platform, platform_grp_4, 50, 400, 1101, 60)
create_platform(Platform, platform_grp_4, 80, 40, 1550, 350)
create_platform(Platform, platform_grp_4, 40, 20, 1700, 270)
create_platform(Platform, platform_grp_4, 30, 400, 2050, 500)
create_platform(Platform, platform_grp_4, 600, 30, 2285, 285)

enemies_grp_4 = pg.sprite.Group()
create_artillery(Artillery, enemies_grp_4, artilleries_3, 515, 270)
create_artillery(Artillery, enemies_grp_4, artilleries_3, 1550, 330)
j = 1.5
for i in range(4):
    create_spider(Spider, enemies_grp_4, web_grp_3, 60, 50, 2100 + (i * 60) + (i * 20), -20, j)
    j += 0.25
for i in range(5):
    create_spikes(Spikes, enemies_grp_4, 805 + (i * 60), 485)
create_enemy(Enemy, enemies_grp_4, 1200, 400, 1)
create_enemy(Enemy, enemies_grp_4, 2100, 400, 1.2)
create_projectile_enemy(Projectile_Enemy, enemies_grp_4, 1101, 365, 0, 50)
create_projectile_enemy(Projectile_Enemy, enemies_grp_4, 2210, 490, 0, 50)

exits_grp_4 = pg.sprite.Group()
exits_grp_4.add(Finish(70, 200, 2550, 285))

coins_grp_4 = pg.sprite.Group()
consumables_grp_4 = pg.sprite.Group()

idle_weapon_grp_4 = pg.sprite.Group()

checkpoints_grp_4 = pg.sprite.Group()

def_groups_4 = [platform_grp_4, enemies_grp_4, exits_grp_4, checkpoints_grp_4, coins_grp_4, consumables_grp_4]
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
# level 5
platform_grp_5 = pg.sprite.Group()
create_platform(Platform, platform_grp_5, 40, 1000, 80, 400)
create_platform(Platform, platform_grp_5, 150, 30, 220, 450)
create_platform(Platform, platform_grp_5, 60, 30, 450, 360)
create_platform(Platform, platform_grp_5, 60, 30, 700, 300)
create_platform(Platform, platform_grp_5, 60, 30, 950, 250)
create_platform(Platform, platform_grp_5, 120, 30, 1260, 340)
create_platform(Platform, platform_grp_5, 60, 20, 1550, 320)
create_platform(Platform, platform_grp_5, 60, 20, 1700, 320)
create_platform(Platform, platform_grp_5, 60, 20, 1850, 320)
create_platform(Platform, platform_grp_5, 600, 30, 1850, 490)
create_platform(Platform, platform_grp_5, 30, 100, 2050, 360)
create_platform(Platform, platform_grp_5, 300, 30, 2185, 295)
create_platform(Platform, platform_grp_5, 1300, 30, 1850, 190)
create_platform(Platform, platform_grp_5, 900, 100, 1900, 40)
create_platform(Platform, platform_grp_5, 600, 30, 3250, 295)
create_platform(Platform, platform_grp_5, 150, 25, 3250, 130)
create_platform(Platform, platform_grp_5, 70, 20, 3800, 100)

enemies_grp_5 = pg.sprite.Group()
create_projectile_enemy(Projectile_Enemy, enemies_grp_5, 1550, 320, 0)
create_projectile_enemy(Projectile_Enemy, enemies_grp_5, 1700, 320, 0)
create_projectile_enemy(Projectile_Enemy, enemies_grp_5, 1850, 320, 0)
for i in range(8):
    create_spider(Spider, enemies_grp_5, web_grp_4, 60, 50, 2960 + (i * 60) + (i * 20), 125, 0)
for i in range(5):
    create_enemy(Enemy, enemies_grp_5, 1600 + (i * 170), 190, 0)
create_enemy(Enemy, enemies_grp_5, 3200, 325, 1)

exits_grp_5 = pg.sprite.Group()
exits_grp_5.add(Finish(70, 200, 220, 450))

coins_grp_5 = pg.sprite.Group()
consumables_grp_5 = pg.sprite.Group()

idle_weapon_grp_5 = pg.sprite.Group()

checkpoints_grp_5 = pg.sprite.Group()
checkpoints_grp_5.add(Checkpoint(55, 70, 2380, 190, 1))
checkpoints_grp_5.add(Checkpoint(55, 70, 3800, 90, 2))

def_groups_5 = [enemies_grp_5, platform_grp_5, exits_grp_5, checkpoints_grp_5, coins_grp_5, consumables_grp_5]

all_coins = [coins_grp_1, coins_grp_2, coins_grp_3, coins_grp_4, coins_grp_5]
all_consumables = [consumables_grp_1, consumables_grp_2, consumables_grp_3, consumables_grp_4, consumables_grp_5]
all_weapons = [idle_weapon_grp_1, idle_weapon_grp_2, idle_weapon_grp_3, idle_weapon_grp_4, idle_weapon_grp_5]
'''
ABDULLAH: END -->
'''