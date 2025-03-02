import json
import argostranslate.translate
import os


def react_translate(source, out, from_language, to_languages):
    with open(source, encoding='utf-8') as f:
        data = json.load(f)

        translated_date = dict()
        for code in to_languages:
            for key, value in data.items():
                try:
                    source_text = value
                    if from_language != "en" and from_language != "EN":
                        source_text = argostranslate.translate.translate(
                            value,
                            from_language,
                            'en'
                        )

                    translated_date[key] = argostranslate.translate.translate(
                        source_text,
                        'en',
                        code
                    )
                except Exception as e:
                    print(e)

            os.makedirs(out, exist_ok=True)
            os.makedirs(out + os.sep + "react", exist_ok=True)
            with open(out + os.sep + "react" + os.sep + code + ".json", 'w', encoding='utf-8') as jsonf:
                json.dump(translated_date, jsonf, ensure_ascii=False, indent=4)
            translated_date = dict()
