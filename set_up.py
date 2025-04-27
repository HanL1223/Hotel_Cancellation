import os

structure = {
    'data': ['raw', 'processed'],
    'notebooks': [],  # No files, just folders
    'src': [],
    'models': [],
    'reports': ['figures'],  # 'figures' is a subfolder
    'config': [],
}

for folder, subfolders in structure.items():
    os.makedirs(folder, exist_ok=True)  # Create parent folder
    for subfolder in subfolders:
        os.makedirs(os.path.join(folder, subfolder), exist_ok=True)  # Create subfolders