while True:
    print('quien eres')
    name = input()
    #si es !='bro' debe coincidir - == debe ser contrario
    if name == 'bro':
    #si aqui se equivoca, vuelve a quien eres
        continue
    print('la password es ?')
    password = input()
    if password == 'aaa':
    #si denuevo te equivocas, vuelves del principio
        break  
print('bienvenido')
