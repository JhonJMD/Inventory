import modulos.corefile as cf
import ui.menu as m

def main():
    cf.checkFile('inventario.json', m.inventario)
    isActive = True
    while isActive:
        m.menuMain()
        try: 
            op = int(input(': '))
        except ValueError:
            print('Tipo de dato erroneo')
            cf.os.system('pause')
        else:
            if (op == 1):
                m.menuProductos()
                cf.os.system('pause')
            elif (op == 2):
                m.menuProveedores()
                cf.os.system('pause')
            elif (op == 5):
                print('Gracias por utilizar nuestro sistema.....')
                isActive = False
            else:
                print('Opcion ingresada invalida')
                cf.os.system('pause')

if __name__ == '__main__':
    main()