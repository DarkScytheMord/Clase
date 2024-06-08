import os
os.system("cls")

import csv
import json

clasificacionEmpresa=[]

with open('listadoRutEmpresa.csv','r',encoding='UTF-8') as archivo_csv:
    lector_csv=csv.DictReader(archivo_csv)
    
    for fila in lector_csv:
        nombre = fila['nombre']
        rut = fila['rut']
        ventas = int(fila['ventas'])
        
        
        print(f"La Empresa '{nombre}' con RUT {rut}, tiene un total de ventas de ${ventas}")
        
        if ventas <= 100000000:
            clasificacion = 'Pequena Contribuyente'
            clasificacionEmpresa.append({
                    'Nombre': nombre,
                    'Rut':rut,
                    'Ventas': ventas,
                    'Clasificacion': clasificacion
                 })
            print(f'{clasificacion}\n')
            
        elif ventas >= 100000001 and ventas <= 200000000:
            clasificacion = 'Mediana Contribuyente'
            clasificacionEmpresa.append({
                    'Nombre': nombre,
                    'Rut':rut,
                    'Ventas': ventas,
                    'Clasificacion': clasificacion
                 })
            print(f'{clasificacion}\n')
            
        elif ventas > 200000000:
            clasificacion = 'Gran Contribuyente'
            clasificacionEmpresa.append({   
                    'Nombre': nombre,
                    'Rut':rut,
                    'Ventas': ventas,
                    'Clasificacion': clasificacion
                 })
            print(f'{clasificacion}\n')

with open ('segmentacionEmpresas.json','w') as archivo_json:
    json.dump(clasificacionEmpresa, archivo_json, indent=1 )
    