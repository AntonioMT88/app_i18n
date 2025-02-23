import sys
import os
import argostranslate.package
from service.ios_translate import ios_translate
from service.android_translate import android_translate
from service.react_translate import react_translate


codes = ["es", "fr", "de"]
print(sys.argv)
#file_type = sys.argv[1].split('.')[-1]
file_path = os.path.basename(sys.argv[1])  # This converts ".\it.json" to "it.json"
source, ext = os.path.splitext(file_path)   # source will be "it" and ext will be ".json"
file_type = ext.lstrip('.')

if len(sys.argv) > 1:
    language_param = sys.argv[2].split(',')
    print(language_param)
    if len(language_param) >= 1:
        codes = language_param

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
required_packages = [
    ('it', 'en'),  # Da italiano a inglese
    *[(f'en', code) for code in codes]  # Da inglese alle altre lingue
]

# Trova e installa tutti i pacchetti necessari
for from_code, to_code in required_packages:
    package = next(
        (p for p in available_packages if p.from_code == from_code and p.to_code == to_code),
        None
    )
    if package:
        print(f"Installazione pacchetto: {package.from_code} -> {package.to_code}")
        argostranslate.package.install_from_path(package.download())
    else:
        print(f"Pacchetto non trovato: {from_code} -> {to_code}")

if file_type == 'xcstrings':
    ios_translate(file_path, codes)
elif file_type == 'json':
    react_translate(file_path, codes)
elif file_type == 'xml':
    android_translate(file_path, 'it', codes)






