# Player
life = 100
attk = 10
defence = 8

# Enemy
enemyLife = 150
enemyAttk = 5
enemyDefence = 4

while True:
    def attkenemy(life, enemyAttk):
        return life - (defence - enemyAttk)
    print("Agora sua vida é")
    print(attkenemy(life, enemyAttk))
    break
