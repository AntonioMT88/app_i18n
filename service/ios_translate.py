import copy
import json
import argostranslate.translate


# Placeholders iOS: “%lld”, “%lf”, and “%@” rispettivamente Int, Double e String
def ios_translate(source, codes):
    with open(source, encoding='utf-8') as input:
        data = json.load(input)
        source_language = data["sourceLanguage"]
        strings = data["strings"]

        for obj in strings.keys():
            local_codes = codes
            localizations = strings[obj]['localizations']
            for localization in localizations.keys():
                if localization in local_codes:
                    local_codes.remove(localization)

            for code in local_codes:
                if code != source_language:
                    if source_language in strings[obj]['localizations'].keys():
                        # print(f"Translating {obj} from \'it\' to \'{code}\'")

                        new_value = copy.deepcopy(strings[obj]['localizations'][source_language])
                        translatedText = new_value['stringUnit']['value']

                        # print(f"New Value to build: {new_value}")
                        # print(f"Value to be translated: {translatedText}")

                        try:
                            temp = argostranslate.translate.translate(
                                strings[obj]['localizations'][source_language]['stringUnit']['value'],
                                'it',
                                'en'
                            )
                            # print(f"Translated Value into en \'{temp}\'")
                            translatedText = argostranslate.translate.translate(
                                temp,
                                'en',
                                code
                            )
                            # print(f"Translated Value into en \'{translatedText}\'")
                        except Exception as e:
                            print(e)

                        new_value['stringUnit']['value'] = translatedText
                        strings[obj]['localizations'][code] = new_value
                        # print(strings[obj]['localizations'])
                        # print("\n\n")

        data["strings"] = strings

        with open("out/ios/Localizable.xcstrings", 'w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf, ensure_ascii=False, indent=4)
