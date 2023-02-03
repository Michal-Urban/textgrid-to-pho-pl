import sys
import subprocess
required_libraries = ["codecs", "parselmouth"]
for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        subprocess.run(["pip", "install", "praat-parselmouth"], check=True)
subprocess.run(["python", "textgrid-to-pho.py"])