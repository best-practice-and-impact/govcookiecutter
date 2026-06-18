
from pathlib import Path
import zipfile,shutil

def create_zip_template():
    """Zip the current directory into a zip file named 'govcookiecutter.zip' and place it in the 'hooks' directory."""
    
    root = Path(".")
    
    with zipfile.ZipFile("/govcookiecutter.zip", "w") as z:
        
        z.writestr("template/", "")
        for path in root.rglob("*"):
            if ".venv" in path.parts: #won't required during packaging, so skip it
                continue
            print(path)
            if path.is_file():
                
                arcname = Path("template") / path.relative_to(root)
                z.write(path, arcname.as_posix())
               
    import os
    cwd = os.getcwd()
    shutil.copy("/govcookiecutter.zip", cwd+"/hooks")


if __name__ == "__main__":
    create_zip_template()