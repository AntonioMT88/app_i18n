import copy
import argostranslate.translate
import xmltodict
import os


def android_translate(source, source_language, codes):
    with open(source, encoding='utf-8') as input:
        data = input.read()

    codes.remove(source_language)
    xml_dict = xmltodict.parse(data)
    # print(xml_dict)

    for code in codes:

        local_dict = copy.deepcopy(xml_dict)

        for elem in local_dict['resources']['string']:
            # print(f"value: {elem}")
            try:
                if '@translatable' not in elem or elem['@translatable'] != 'false':

                    temp = argostranslate.translate.translate(
                        elem['#text'],
                        source_language,
                        'en'
                    )

                    elem['#text'] = argostranslate.translate.translate(
                        temp,
                        'en',
                        code
                    )
            except Exception as e:
                print(e)

        os.makedirs("out/android/values-" + code, exist_ok=True)
        with open("out/android/values-" + code + "/strings.xml", 'w', encoding='utf-8') as xmlf:
            xmlf.write(xmltodict.unparse(local_dict, pretty=True))
