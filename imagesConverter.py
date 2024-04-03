# Instalar Librería pillow antes de ejecutar
# pip install pillow
from PIL import Image
import os


def convert_to_webp(image_path, image_out_path):
    try:
        # Abrir imagen
        img = Image.open(image_path)

        # Construir nombre del archivo de salida
        output_filename = os.path.splitext(os.path.basename(image_path))[0] + ".webp"
        output_path = os.path.join(image_out_path, output_filename)
        # Convert the image to webp format
        img.save(output_path, "WEBP")
        print(f"Converted {image_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {image_path}: {e}")


def convert_images_in_directory(directory, output_dir):
    # Buscar todos los archivos del directorio
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Convertir cada imagen a webp
            convert_to_webp(os.path.join(directory, filename), output_dir)


# Directorio actual del script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define las rutas relativas para el directorio de entrada y salida
in_directory_path = os.path.join(script_directory, "Entrada")
out_directory_path = os.path.join(script_directory, "Salida")

# Convertir imágenes en el directorio de entrada y guardarlas en el directorio de salida
convert_images_in_directory(in_directory_path, out_directory_path)