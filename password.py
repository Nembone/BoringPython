print('diga su nombre')
name = input()
if name == 'emilio':
    print('hola')
    print('escribe tu password')
    psw = input()
    if psw == 'swordfish':
        print('acceso garantizado')
    else:
        print('clave erronea')
else:
    print('usuario erroneo')