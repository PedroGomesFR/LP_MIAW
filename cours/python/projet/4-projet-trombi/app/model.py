# model.py
import os
import cv2
import shutil
import zipfile
from PIL import Image
import pandas as pd

class TrombiModel:
    def __init__(self):
        self.photos = []
        self.students = []
        self.template_path = None
        self.output_path = None
        self.temp_dir = "temp_docx"

    def load_photos(self, directory):
        self.photos = []
        for file in os.listdir(directory):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                self.photos.append(os.path.join(directory, file))
        return len(self.photos)

    def load_students(self, file_path):
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)
        self.students = df[['nom', 'prenom']].values.tolist()
        return len(self.students)

    def process_image(self, image_path):
        # Redimensionner et optimiser l'image
        img = cv2.imread(image_path)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Détection du visage
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            # Centrer sur le visage
            center_x = x + w//2
            center_y = y + h//2
            
            # Redimensionner
            target_size = (200, 200)
            img_resized = cv2.resize(img, target_size)
            
            # Convertir en JPG et optimiser
            img_pil = Image.fromarray(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB))
            return img_pil

        return None

    def create_trombi(self, template_path, output_path):
        # Créer dossier temporaire
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        os.makedirs(self.temp_dir)

        # Dézipper le template
        with zipfile.ZipFile(template_path, 'r') as zip_ref:
            zip_ref.extractall(self.temp_dir)

        # Traiter les images et remplacer dans le document
        for i, (photo, student) in enumerate(zip(self.photos, self.students)):
            processed_img = self.process_image(photo)
            if processed_img:
                img_path = os.path.join(self.temp_dir, f"word/media/image{i+1}.jpg")
                processed_img.save(img_path, "JPEG", quality=85)

        # Modifier le contenu XML pour les noms
        word_doc = os.path.join(self.temp_dir, "word/document.xml")
        # Ici, ajoutez la logique pour modifier le XML avec les noms des étudiants

        # Créer le nouveau fichier docx
        shutil.make_archive(output_path, 'zip', self.temp_dir)
        os.rename(f"{output_path}.zip", output_path)

        # Nettoyer
        shutil.rmtree(self.temp_dir)