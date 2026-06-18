
import os

from cookiecutter.main import cookiecutter
from pathlib import Path
import zipfile,shutil
import hooks

def start_govcookiecutter():
    target_path = os.path.dirname(hooks.__file__)
    cookiecutter(template= os.path.join(target_path, "govcookiecutter.zip"))