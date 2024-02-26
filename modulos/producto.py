import modulos.corefile as cf
import json
import os

def searchDataPro(data):
    criterio = input('Ingrese el codigo del Producto a buscar: ')
    result = data['productos'].get(criterio)
    codigo, nombre, stockMax, stockMin, stock, estado, proveedor = result.values()
    print(f'Producto: {nombre}')
    os.system('pause')

def delDataPro(data):
    criterio = input('Ingrese el codigo del Producto a Eliminar: ')
    data['productos'].pop(criterio)
    updateFilePro('inventario.json',data)
    os.system('pause')

def updateDataPro(data, srcData):
    if (len(data) <= 0):
        print('No se encontro informacion')
    else: 
        for key in data.keys():
            if (key != 'codigo'):
                if (bool(input(f'Desea modificar el {key} S(si) o Enter No: '))):
                    os.system('cls')
                    data[key] = input(f'Ingrese el nuevo valor para {key}: ')
        srcData['productos'].update({data['codigo'] : data})
        updateFilePro('inventario.json',srcData)
    os.system('pause')

def updateFilePro(archivo : str, data : dict):
    with open(cf.MY_DATABASE + archivo, "w") as fw:
        json.dump(data, fw, indent=4)