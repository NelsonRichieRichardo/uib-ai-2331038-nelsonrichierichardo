import sys
import importlib

packages = ["numpy", "pandas", "sklearn", "skfuzzy", "cv2", "matplotlib", "nltk", "torch"]
for pkg in packages:
    try:
        m = importlib.import_module(pkg)
        print(f"{pkg}: OK, version: {getattr(m, '__version__', 'unknown')}")
    except Exception as e:
        print(f"{pkg}: Error - {e}")

print(f"Python: {sys.version}")