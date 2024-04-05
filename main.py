import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo JSON de credenciales descargado
credentials_file = 'ruta/a/tu/archivo.json'

# Escopos necesarios para acceder a Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=credentials)
    return drive_service

def upload_file(file_path, drive_service):
    file_name = os.path.basename(file_path)
    file_metadata = {'name': file_name}

    media = drive_service.files().create(
        body=file_metadata,
        media_body=file_path,
        fields='id'
    ).execute()

    print(f'Archivo subido con ID: {media.get("id")}')

    return media.get('id')  # Devolver el ID del archivo subido

def delete_local_file(file_path):
    os.remove(file_path)
    print(f'Archivo local eliminado: {file_path}')

if __name__ == "__main__":
    # Autenticar y obtener servicio de Google Drive
    drive_service = authenticate()

    # Ruta al archivo que quieres subir
    archivo_a_subir = 'ruta/a/tu/archivo.pdf'

    try:
        # Subir archivo a Google Drive
        file_id = upload_file(archivo_a_subir, drive_service)

        # Eliminar archivo local en Replit
        delete_local_file(archivo_a_subir)

        print('Proceso completado exitosamente.')
    except Exception as e:
        print(f'Error durante la operación: {e}')
