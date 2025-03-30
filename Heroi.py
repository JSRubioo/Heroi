class Heroi:
    def __init__(self,nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        



    
    def atacar (self):
        atkRealizado = self.ataque(self.tipo)
        print(f"O {self.tipo} atacou usando {atkRealizado}")
    @staticmethod
    def ataque(tipo):
        if tipo == "Mago":
           return"Usou magia"
        elif tipo == "Guerreiro":
           return"Usou espada"
        elif tipo == "Monge":
          return"Usou artes marciais"
        elif tipo == "Ninja":
          return"Usou shuriken"
        
    

'''def inserirInformacoes():
        nome = input("Informe o nome do Heroi: ")
        idade = input("Informe a idade do Heroi: ")
        tipo = input("Informe o tipo do heroi: ")
        return Heroi(nome,idade,tipo)'''


heroi = Heroi("","","")




while True:
    
    x = int(input("\nDigite a escolha do Heroi:\n 1- Mago\n 2- Guerreiro\n 3- Monge\n 4- Ninja\n 0-Sair\n"))
    if x == 1:
        heroi.tipo = "Mago"
    elif x == 2:
        heroi.tipo ="Guerreiro"
    elif x == 3:
        heroi.tipo ="Monge"
    elif x == 4: 
        heroi.tipo ="Ninja"
    elif x ==0:
        break
    
    heroi.nome = input("Informe o nome do Heroi: ")
    heroi.idade = input("Informe a idade do Heroi: \n")    
    
    heroi.atacar()