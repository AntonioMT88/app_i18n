import sys
import os
import argparse
import argostranslate.package
from service.ios_translate import ios_translate
from service.android_translate import android_translate
from service.react_translate import react_translate


def main(source, out, from_language, to_languages):
    _, ext = os.path.splitext(source)
    file_type = ext.lstrip('.')

    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()

    required_packages = list()
    if from_language != "en":
        source_to_en = (from_language, 'en')
        required_packages.append(source_to_en)

    required_packages = [
        *[(f'en', code) for code in to_languages.split(",") if code != 'en']
    ]

    # Seek and install all needed packets
    for from_code, to_code in required_packages:
        package = next(
            (p for p in available_packages if p.from_code == from_code and p.to_code == to_code),
            None
        )
        if package:
            print(f"Installing packet: {package.from_code} -> {package.to_code}")
            argostranslate.package.install_from_path(package.download())
        else:
            print(f"Packet not found: {from_code} -> {to_code}")

    if file_type == 'xcstrings':
        ios_translate(source, out, from_language, to_languages.split(","))
    elif file_type == 'json':
        react_translate(source, out, from_language, to_languages.split(","))
    elif file_type == 'xml':
        android_translate(source, out, from_language, to_languages.split(","))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="app_i18n")
    parser.add_argument("--source", type=str, required=True, help="Source file to translate. Allowed are: *.xcstrings, *.json, *.xml")
    parser.add_argument("--out", type=str, required=True, help="Destination path for translated file. Output file name will follow specific platform requirement.")
    parser.add_argument("--from_language", type=str, required=False, default="en", help="If not specified, default is 'en'!")
    parser.add_argument("--to_languages", type=str, required=False, default="it,es,de", help="Multiple destination languages must be separated with comma. If not specifiedm default is 'it,es,de'")

    args = parser.parse_args()

    main(args.source, args.out, args.from_language, args.to_languages)
