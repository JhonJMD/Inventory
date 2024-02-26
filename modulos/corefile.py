import os
import json

MY_DATABASE = 'data/'

def checkFile(archivo : str, data : dict):
    if (os.path.isfile(MY_DATABASE+archivo)):
        with open(MY_DATABASE+archivo, 'r') as fr:
            data = json.load(fr)
            return data
    else:
        with open(MY_DATABASE+archivo,'w') as fw:
            json.dump(data, fw, indent=4)

def readFile(*param):
    data = list(param)
    with open(MY_DATABASE+data[0], 'r') as fr:
        return json.load(fr)

def createData(archivo : str, data : dict):
    with open(MY_DATABASE+archivo,'w+') as rwf:
        json.dump(data, rwf, indent=4)

def searchData(data):
    criterio = input('Ingrese el nit del Proveedor a buscar: ')
    result = data['proveedores'].get(criterio)
    nit, nombrePro, tipo, direccion = result.values()
    ciudad, ubicacion, longitud, latitud = direccion.values()
    print(f'Nit {ciudad}')
    os.system('pause')

def delData(data):
    criterio = input('Ingrese el nit del Proveedor a Eliminar: ')
    data['proveedores'].pop(criterio)
    updateFile('inventario.json',data)
    os.system('pause')

def updateData(data, srcData):
    if (len(data) <= 0):
        print('No se encontro informacion')
    else: 
        for key in data.keys():
            if (key != 'nit'):
                if (type(data[key]) == dict):
                    for key2 in data[key].keys():
                        if (bool(input(f'Desea modificar el {key2} S(si) o Enter No: '))):
                            os.system('cls')
                            data[key][key2] = input(f'Ingrese el nuevo valor para {key2}: ') 
                else:
                    if (bool(input(f'Desea modificar el {key} S(si) o Enter No: '))):
                        os.system('cls')
                        data[key] = input(f'Ingrese el nuevo valor para {key}: ')
        srcData['proveedores'].update({data['nit'] : data})
        updateFile('inventario.json',srcData)
    os.system('pause')

def updateFile(archivo : str, data : dict):
    with open(MY_DATABASE + archivo, "w") as fw:
        json.dump(data, fw, indent=4)