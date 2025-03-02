import copy
import json
import argostranslate.translate
import os


# Placeholders iOS: “%lld”, “%lf”, and “%@” rispettivamente Int, Double e String
def ios_translate(source, out, from_language, to_languages):
    with open(source, encoding='utf-8') as f:
        data = json.load(f)
        source_language = data["sourceLanguage"]
        strings = data["strings"]

        for obj in strings.keys():
            local_codes = to_languages
            localizations = strings[obj]['localizations']
            for localization in localizations.keys():
                if localization in local_codes:
                    local_codes.remove(localization)

            for code in local_codes:
                if code != source_language:
                    if source_language in strings[obj]['localizations'].keys():

                        new_value = copy.deepcopy(strings[obj]['localizations'][source_language])
                        translated_text = new_value['stringUnit']['value']

                        try:
                            source_text = strings[obj]['localizations'][source_language]['stringUnit']['value']

                            if from_language != "en" and from_language != "EN":
                                source_text = argostranslate.translate.translate(
                                    strings[obj]['localizations'][source_language]['stringUnit']['value'],
                                    from_language,
                                    'en'
                                )
                            translated_text = argostranslate.translate.translate(
                                source_text,
                                'en',
                                code
                            )
                        except Exception as e:
                            print(e)

                        new_value['stringUnit']['value'] = translated_text
                        strings[obj]['localizations'][code] = new_value

        data["strings"] = strings

        os.makedirs(out, exist_ok=True)
        os.makedirs(out + os.sep + "ios", exist_ok=True)
        with open(out + os.sep + "ios" + os.sep + "Localizable.xcstrings", 'w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf, ensure_ascii=False, indent=4)
