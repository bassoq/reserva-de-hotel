class Hotel:
    def __init__(self, name, classif, price_normal, premium_normal, price_wek, premium_wek):
        self.name = name  #nome
        self.classif = classif #classificação de estrelas
        self.price_normal = price_normal #preço do dia de semana para clientes regulares
        self.price_wek = price_wek #preço do final de semana para clientes regulares
        self.premium_normal = premium_normal #preço do dia desemana para clientes fidelidade
        self.premium_wek = premium_wek #preço do final de semana para clientes fidelidade

h1 = Hotel("Lakewood", 3, 110, 80, 90, 80)
h2 = Hotel("Bridgewood", 4, 160, 110, 60, 50)
h3 = Hotel("Ridgewood", 5, 220, 100, 150, 40)

