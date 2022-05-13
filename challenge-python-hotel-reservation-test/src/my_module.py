from src.__init__ import * #importar arquivo init

def get_cheapest_hotel(number):   #DO NOT change the function's name
    #Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed) exemplo de entrada

    #define-se se o cliente é regular ou participante do programa fidelidade
    regular = True
    if number[0:7] == "Rewards":
        regular = False
    
    #Retiramos a parte inicial e dividimos pela virgula os dias que o cliente irá ficar no hotel
    number = number[7:]
    days = number.split(',')


    #procura e calcular quantos dias do final de semana e da semana útil o cliente quer ficar no hotel
    fds = 0
    for day in days:
        if day[-4:-1] == 'sat' or day[-4:-1] == 'sun':
            fds += 1
    sem = len(days) - fds
    somaf = 99999


    #loop de repetição para calcular qual o valor de cada hotel nos dias que o cliente irá ficar hospedado
    for hotel in [h1,h2,h3]:
        soma = 0
        if regular == True:
            soma = hotel.price_normal * sem + hotel.price_wek * fds
        
        else:
            soma = hotel.premium_normal * sem + hotel.premium_wek *fds
        
        #condicional, guarda o valor do hotel mais barato assim como seu nome e sua classificação
        if soma < somaf:
            star = hotel.classif
            somaf = soma
            cheapest_hotel = hotel.name

        #condicional para recomendar o melhor hotel quando o preço da estadia é igual
        if soma == somaf and hotel.classif > star:
            star = hotel.classif
            somaf = soma
            cheapest_hotel = hotel.name

    return cheapest_hotel

