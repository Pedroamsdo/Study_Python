verte = input()
animal = input()
blood = input()
x = 0
if(verte == 'vertebrado' and animal == 'ave' and blood == 'carnivoro'):
    x = 'aguia'
elif(verte == 'vertebrado' and animal == 'ave' and blood == 'onivoro'):
    x = 'pomba'
elif(verte == 'vertebrado' and animal == 'mamifero' and blood == 'onivoro'):
    x = 'homem'
elif(verte == 'vertebrado' and animal == 'mamifero' and blood == 'herbivoro'):
    x = 'vaca'
elif(verte == 'invertebrado' and animal == 'inseto' and blood == 'hematofago'):
    x = 'pulga'
elif(verte == 'invertebrado' and animal == 'inseto' and blood == 'herbivoro'):
    x = 'lagarta'
elif(verte == 'invertebrado' and animal == 'anelideo' and blood == 'hematofogo'):
    x = 'sanguessuga'
elif(verte == 'invertebrado' and animal == 'anelideo' and blood == 'onivoro'):
    x = 'minhoca'
print(x)
