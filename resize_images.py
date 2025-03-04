# pip install pillow
# pip install pyinstaller
# pyinstaller --onefile --icon=ricky.ico resize_images.py

import os
import sys
from PIL import Image

def resize_image(image_path):
    try:
        # Apri l'immagine
        img = Image.open(image_path)
        
        # Ottieni le dimensioni
        width, height = img.size
        
        # Calcola l'aspect ratio
        aspect_ratio = width / height
        
        # Imposta le dimensioni massime
        max_width = 640
        max_height = 480
        
        if width > height:        # Verifica se l'immagine è orizzontale
            new_width = min(width, max_width)
            new_height = int(new_width / aspect_ratio)
            if new_height > max_height:
                new_height = max_height
                new_width = int(new_height * aspect_ratio)
        else:        # o verticale
            new_height = min(height, max_height)
            new_width = int(new_height * aspect_ratio)
            if new_width > max_width:
                new_width = max_width
                new_height = int(new_width / aspect_ratio)
        
        # Ridimensiona l'immagine
        img_resized = img.resize((new_width, new_height))
        
        # Salva l'immagine ridimensionata nella stessa cartella di origine con nomefile+"_resized"
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_resized{ext}"
        img_resized.save(output_path)
        print(f"Immagine salvata: {output_path}")
    except Exception as e:
        print(f"Errore nell'elaborazione dell'immagine {image_path}: {e}")

def main():
    # Controlla se ci sono file trascinati sull'eseguibile
    if len(sys.argv) < 2:
        print("Trascina le immagini su questo eseguibile per ridimensionarle.")
        return
    
    # Elabora ogni immagine trascinata
    for image_path in sys.argv[1:]:
        if os.path.isfile(image_path):
            resize_image(image_path)
        else: # se sono tante immagini e ne elimini qualcuna nel mentre...
            print(f"File non trovato: {image_path}")

if __name__ == "__main__":
    main()
