from ftplib import FTP
import os


def upload_folder_to_ftp(ftp, folder_path, remote_path):

    for root, dirs, files in os.walk(folder_path):
        for dirname in dirs:
            local_dir = os.path.join(root, dirname)
            remote_dir = os.path.join(
                remote_path, os.path.relpath(local_dir, folder_path)
            )
            try:
                ftp.mkd(remote_dir)
            except Exception as e:
                print(
                    f"Directory {remote_dir} already exists or couldn't be created: {e}"
                )

        for filename in files:

            local_file = os.path.join(root, filename)
            remote_file = os.path.join(
                remote_path, os.path.relpath(local_file, folder_path)
            )
            with open(local_file, "rb") as file:
                ftp.storbinary(f"STOR {remote_file}", file)
                print(f"Uploaded {local_file} to {remote_file}")


def main():
    # Define las credenciales del servidor FTP
    ftp_host = ""
    ftp_user = ""
    ftp_password = ""

    # Directorio actual del script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Define las rutas relativas para el directorio de entrada y salida
    out_directory_path = os.path.join(script_directory, "Salida")

    # Carpeta local para subir
    folder_to_upload = out_directory_path
    remote_folder_path = "/public_html/img/prod"

    # Conectar al servidor FTP
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_password)

    # Subir la carpeta
    upload_folder_to_ftp(ftp, folder_to_upload, remote_folder_path)

    # Cerrar la conexión FTP
    ftp.quit()


if __name__ == "__main__":
    main()
