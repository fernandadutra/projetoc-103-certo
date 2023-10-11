import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/55319/Downloads"
to_dir ="C:/Users/55319/Documents/Code/Projeto C-103"
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Olá,{event.src_path} foi criado!")

    def on_deleted(self, event):
        print(f"Opa, alguém excluiu {event.src_path}!") 

    def on_modified(self, event):
        print(f"O {event.src_path} foi modificado!") 

    def on_moved(self, event):
        print(f"O {event.src_path} foi movido!")

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()       

try:
    while True:
        time.sleep(2)
        print("Executando...")
except KeyboardInterrupt:
    print("Interrompido!")
    observer.stop()
