class Enenmy:
    life = 3

    def attack(self):
        print('Ouch!')
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life) + " Life left")


enemy1 = Enenmy()
enemy2 = Enenmy()

enemy1.attack()
enemy1.checklife()
enemy2.attack()
enemy2.checklife()