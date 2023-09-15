import os
import shutil
from datetime import datetime as dt
import openpyxl

# crea una copia de seguridad a partir de una fecha
def copiar_archivos(desde_directorio, a_directorio, fecha):
    # Crear un archivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Archivos copiados"

    # Agregar encabezados de columna
    sheet['A1'] = "Ruta original"
    sheet['B1'] = "Ruta de destino"

    # Fila actual en la hoja de cálculo
    fila_actual = 2

    # Recorrer los directorios y archivos del directorio desde_directorio
    for root, dirs, files in os.walk(desde_directorio):
        for file in files:
            ruta_completa = os.path.join(root, file)

            # Verificar la fecha de modificación del archivo
            fecha_modificacion = dt.fromtimestamp(os.path.getmtime(ruta_completa))

            # Comprobar si el archivo fue generado o modificado después de la fecha especificada
            if fecha_modificacion >= fecha:
                # Obtener la ruta de destino en la unidad de red
                ruta_destino = ruta_completa.replace(desde_directorio, a_directorio)

                # Crear los directorios en caso de que no existan
                os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)

                # Copiar el archivo a la unidad de red
                shutil.copy2(ruta_completa, ruta_destino)
                print(f"Archivo copiado: {ruta_completa} -> {ruta_destino}")

                # Agregar información del archivo a la hoja de cálculo
                sheet[f"A{fila_actual}"] = ruta_completa
                sheet[f"B{fila_actual}"] = ruta_destino

                fila_actual += 1

    # Agregar la fecha de la copia en una celda adicional
    fecha_copia = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    sheet[f"A{fila_actual}"] = "Fecha de copia:"
    sheet[f"B{fila_actual}"] = fecha_copia

    # Guardar el archivo Excel
    nombre_archivo = "archivos_copiados.xlsx"
    ruta_archivo = os.path.join(a_directorio, nombre_archivo)
    workbook.save(ruta_archivo)
    print(f"Archivo Excel guardado: {ruta_archivo}")


# Ejemplo de uso
directorio_origen = "F:/Andres"
directorio_destino = "Z:/Andres/backup"
fecha_limite = dt(2023, 6, 5)  # Fecha límite para copiar los archivos

copiar_archivos(directorio_origen, directorio_destino, fecha_limite)
