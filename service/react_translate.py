import json
import argostranslate.translate


def react_translate(source, codes):
    with open(source, encoding='utf-8') as input:
        data = json.load(input)
        source_language = source.split('.')[0]

        codes.remove(source_language)

        translated_date = dict()
        for code in codes:
            for key, value in data.items():
                try:
                    temp = argostranslate.translate.translate(
                        value,
                        source_language,
                        'en'
                    )

                    translated_date[key] = argostranslate.translate.translate(
                        temp,
                        'en',
                        code
                    )
                except Exception as e:
                    print(e)
            with open("out/react/" + code + ".json", 'w', encoding='utf-8') as jsonf:
                json.dump(translated_date, jsonf, ensure_ascii=False, indent=4)
            translated_date = dict()
