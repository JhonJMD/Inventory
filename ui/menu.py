import os
import ui.title as t
import modulos.corefile as cf
import modulos.producto as pc

inventario = {
    'proveedores': {},
    'productos' : {}
}
inventario = cf.checkFile('inventario.json', inventario)

def menuMain():
    os.system('cls')
    t.headerMain()
    opciones = ['Administrar Productos','Proveedores','Compras','Ventas','Salir']
    for idx, item in enumerate(opciones):
        print(f'{idx+1}. {item}')

def menuProductos():
    os.system('cls')
    t.headerProductos()
    opciones = ['Agregar','Editar','Eliminar','Buscar','Regresar']
    for idx, item in enumerate(opciones):
        print(f'{idx+1}. {item}')
    try:
        op = int(input(': '))
    except ValueError:
        print('Tipo de dato incorrecto')
        os.system('pause')
    else:
        if (op == 1):
            codigo = input('Ingrese el Codigo: ')
            nombre = input('Ingrese el Nombre: ')
            stockMax = int(input('Ingrese el stock maximo: '))
            stockMin = int(input('Ingrese el stock minimo: '))
            stock = int(input('Ingrese el stock actual: '))
            estado = input('Ingrese el estado: ')
            nit = input('Ingrese el nit del Proveedor: ')
            for key, value in inventario['proveedores'].items():
                if inventario['proveedores'][key] == nit:
                    pass
                else:
                    print()
            prov = []
            prov.append(nit)
            producto = {
                'codigo': codigo,
                'nombre': nombre,
                'stockMax': stockMax,
                'stockMin': stockMin,
                'stock': stock,
                'estado': estado,
                'proveedor': prov
            }
            inventario.get('productos', {}).update({codigo : producto})       
            cf.createData('inventario.json',inventario)
        elif (op == 2):
            palabra = input('Ingrese el codigo del Producto a modificar: ')
            pc.updateDataPro(inventario.get('productos').get(palabra,{}), inventario)
        elif (op == 3):
            pc.delDataPro(inventario)
        elif (op == 4):
            pc.searchDataPro(inventario)
        elif (op == 5):
            menuMain()
        else:
            print('Opcion ingresada invalida')
            os.system('pause')

def menuProveedores():
    os.system('cls')
    t.headerProveedores()
    opciones = ['Agregar','Editar','Eliminar','Buscar','Regresar']
    for idx, item in enumerate(opciones):
        print(f'{idx+1}. {item}')
    try:
        op = int(input(': '))
    except ValueError:
        print('Tipo de dato incorrecto')
        os.system('pause')
    else:
        if (op == 1):
            nit = input('Ingrese el Nit: ')
            nombrePro = input('Ingrese el Nombre: ')
            tipo = input('Ingrese el Tipo de persona Natura o Juridica: ')
            ciudad = input('Ingrese la Ciudad: ')
            ubicacion = input('Ingrese la Ubicacion: ')
            longitud = float(input('Ingrese la Longitud: '))
            latitud = float(input('Ingrese la Latitud: '))
            proveedor={
                'nit':nit,
                'nombrePro':nombrePro,
                'tipo':tipo,
                'direccion':{
                    'ciudad':ciudad,
                    'ubicacion':ubicacion,
                    'longitud':longitud,
                    'latitud':latitud
                }
            }
            inventario.get('proveedores', {}).update({nit : proveedor})       
            cf.createData('inventario.json',inventario)
        elif (op == 2):
            palabra = input('Ingrese el Nro de identificacion del Proveedor a modificar: ')
            cf.updateData(inventario.get('proveedores').get(palabra,{}), inventario)
        elif (op == 3):
            cf.delData(inventario)
        elif (op == 4):
            cf.searchData(inventario)
        elif (op == 5):
            menuMain()
        else:
            print('Opcion ingresada invalida')
            os.system('pause')