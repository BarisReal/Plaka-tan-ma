import cv2
import tkinter as tk
from tkinter import filedialog

def select_image():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    if file_path:
        image = cv2.imread(file_path)
        detect_and_display_plate(image)

def detect_and_display_plate(image):
    # Plakayı tanıma için OpenCV'nin önceden eğitilmiş plaka tanıma modelini yükle
    plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

    # Gri tonlamalı görüntüyü elde et
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Plakaları algıla
    plates = plate_cascade.detectMultiScale(gray, 1.1, 4)

    # Plakaları çerçeve içine al ve sonucu göster
    for (x, y, w, h) in plates:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Sonuçları göster
    cv2.imshow('Plaka Tanıma', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

select_image()
