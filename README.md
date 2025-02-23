# Translator Script

## Description

This Python script utilizes the [Argos Translate](https://github.com/argosopentech/argos-translate) model to translate language files for Android, iOS, and React applications (with Spring Boot support coming soon). The script automatically downloads and installs the required translation packages and organizes the translated files into designated folders with the appropriate naming conventions for each platform.

## Features

- **Automatic Package Management:** Updates the Argos Translate package index and installs the necessary packages to translate from Italian to English and from English to the specified target languages.
- **Multi-Platform Support:** Translates language files for:
  - **Android:** XML files containing string resources.
  - **iOS:** `.xcstrings` files (JSON formatted).
  - **React:** JSON files containing string values.
- **Output Organization:** Saves the translated files in platform-specific directories with the correct file naming conventions.

## Prerequisites

- **Python 3.x**
- **Argos Translate:** Installable via pip.
- **Other Dependencies:** See `requirements.txt`.

Make sure to install all the required dependencies before running the script.

## Project structure
  ```
    translator-script/
    ├── main.py              # Main script
    ├── service/             # Translation modules for each platform
    │   ├── android_translate.py
    │   ├── ios_translate.py
    │   └── react_translate.py
    └── out/                 # Output directories for translated files
        ├── android/
        ├── ios/
        └── react/
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/translator-script.git
2. Install all required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. python main.py <source_file> <languages>
   ```bash
   python main.py it.json it,en,es
   
- it.json: The source file containing the Italian strings.
- it,en,es: A comma-separated list of languages for translation (including the source language).
- The script determines the platform based on the file extension:
  - .xml for Android
  - .xcstrings for iOS
  - .json for React

## Notes
- The script automatically removes the source language from the target languages to prevent redundant translations.
- Output file paths are currently hard-coded in the code. Modify these paths if needed to suit your project structure.
- Any translation errors will be printed to the console.