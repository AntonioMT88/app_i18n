import copy
import argostranslate.translate
import xmltodict
import os


def android_translate(source, out, from_language, to_languages):
    with open(source, encoding='utf-8') as f:
        data = f.read()

    xml_dict = xmltodict.parse(data)

    for code in to_languages:
        local_dict = copy.deepcopy(xml_dict)
        for elem in local_dict['resources']['string']:
            try:
                if '@translatable' not in elem or elem['@translatable'] != 'false':

                    source_text = elem['#text']

                    if from_language != "en" and from_language != "EN":
                        source_text = argostranslate.translate.translate(
                            elem['#text'],
                            from_language,
                            'en'
                        )

                    elem['#text'] = argostranslate.translate.translate(
                        source_text,
                        'en',
                        code
                    )
            except Exception as e:
                print(e)

        os.makedirs(out, exist_ok=True)
        os.makedirs(out + os.sep + "android", exist_ok=True)
        os.makedirs(out + os.sep + "android" + os.sep + "values-" + code, exist_ok=True)
        with open(out + os.sep + "android" + os.sep + "values-" + code + os.sep + "strings.xml", 'w', encoding='utf-8') as xmlf:
            xmlf.write(xmltodict.unparse(local_dict, pretty=True))
