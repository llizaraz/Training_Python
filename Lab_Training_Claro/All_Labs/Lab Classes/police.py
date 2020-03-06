import time
##defining a Class

class police():
    country="Colombia"
    def __init__(self, name, gender=None, age="empty"):
        self.name = name
        self.gender = gender
        self.age=age
        self.shoot_authorization=False

    def shoot(self):
        if self.shoot_authorization:
            print(self.name+" ->  PUM PUM PUM PUM PUM")
        else:
            print(self.name+" no Esta autorizado para cargar Armas")

    def authorization_change(self,authorization):
        self.shoot_authorization=authorization


class esmad(police):

    def __init__(self, name):
        self.name = name
        self.shoot_authorization = True
        self.shield=True
        self.number_lacrimogen_gas = 10


    def shoot_lacrimogen(self):
        if self.number_lacrimogen_gas > 0:
            print(self.name+" ->  PAM  PAM PAM PAM PAM")
            self.number_lacrimogen_gas-=1
        else:
            print(self.name+" sin gas")
            self.recharge_lacrimogen()

    def recharge_lacrimogen(self):
        print("Recargando...")
        time.sleep(5)
        self.number_lacrimogen_gas = 10