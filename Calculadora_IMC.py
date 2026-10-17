nome= input ('Qual o seu nome?')
idade= input (f'Olá {nome} quantos anos você tem?')
altura = float (input (f'Certo {nome}, agora me diz qual sua altura em metros?'))
peso = float (input ('Qual seu peso em quilos?'))
IMC= peso / altura **2
print  (f'Então seu IMC é: {IMC:.1f}')

