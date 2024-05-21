class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.dormindo = False
        self.falando = False

    def comer(self, alimento=None, bebida=None):
        if self.dormindo or self.falando:
            print("Não posso comer enquanto estou dormindo ou falando.")
        else:
            if alimento and bebida:
                print(f"{self.nome} está comendo {alimento} e bebendo {bebida}")
            elif alimento:
                print(f"{self.nome} está comendo {alimento}")
            elif bebida:
                print(f"{self.nome} está bebendo {bebida}")
            else:
                print(f"{self.nome} não está comendo nem bebendo")
            self.comendo = True

    def falar(self):
        if self.comendo or self.dormindo:
            print("Não posso falar enquanto estou comendo ou dormindo.")
        else:
            print(f"{self.nome} está falando")
            self.falando = True

    def dormir(self):
        if self.comendo or self.falando:
            print("Não posso dormir enquanto estou comendo ou falando.")
        else:
            print(f"{self.nome} está dormindo")
            self.dormindo = True

    def parar_comer(self):
        if self.comendo:
            print("Eu já não estou comendo.")
        else:
            print(f"{self.nome} parou de comer.")
            self.comendo = False

    def parar_dormir(self):
        if self.dormindo:
            print("Eu já não estou dormindo.")
        else:
            print(f"{self.nome} parou de dormir.")
            self.dormindo = False

    def parar_falar(self):
        if not self.falando:
            print("Eu já não estou falando.")
        else:
            print(f"{self.nome} parou de falar.")
            self.falando = False

