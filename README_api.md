# Document Translation Project

This project provides a script to translate DOCX documents from one language to another using the Argos Translate library.

## Prerequisites
- Python
- Docker
- Docker Compose

## Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory.

run requirements.txt file
```
pip install -r requirements.txt
```

## Docker Setup

### Build the Docker Image

To build the Docker image, run the following command:

```sh
docker-compose build
```
Run the Docker Container
To run the Docker container, use the following command:

```sh
docker-compose up
```

Usage
The main script for translating documents is translate.py. This script reads the source and target languages from a YAML file (lang_code.yml) and translates all DOCX files in the specified input directory.

Command Line Arguments
--input_path: The path to the directory containing the DOCX files to be translated.
--output_path: The path to the directory where the translated DOCX files will be saved.
--src_lang: The source language code (e.g., English for 'en').
--tar_lang: The target language code (e.g., French for 'fr').
Example
To translate documents from English to French, you can run the following command:
```cmd
python translate.py --input-path input_docx --output_path output_docx --src-lang 'English' --tar-lang 'Bengali'
```
Below are list of language use can use
```
English: en
Afrikaans: af
Albanian: sq
Amharic: am
Arabic: ar
Armenian: hy
Basque: eu
Bengali: bn
Bosnian: bs
Bulgarian: bg
Catalan: ca
Chinese (Simplified): zh
Chinese (Traditional): zh-TW
Croatian: hr
Czech: cs
Danish: da
Dutch: nl
Estonian: et
Finnish: fi
French: fr
Georgian: ka
German: de
Greek: el
Gujarati: gu
Haitian Creole: ht
Hebrew: he
Hindi: hi
Hungarian: hu
Icelandic: is
Indonesian: id
Italian: it
Japanese: ja
Kannada: kn
Kazakh: kk
Khmer: km
Korean: ko
Latvian: lv
Lithuanian: lt
Macedonian: mk
Malay: ms
Mongolian: mn
Nepali: ne
Norwegian: no
Persian: fa
Polish: pl
Portuguese: pt
Punjabi: pa
Romanian: ro
Russian: ru
Serbian: sr
Slovak: sk
Slovenian: sl
Somali: so
Spanish: es
Swahili: sw
Swedish: sv
Tamil: ta
Telugu: te
Turkish: tr
Ukrainian: uk
Urdu: ur
Vietnamese: vi
Welsh: cy
Yiddish: yi
Zulu: zu
```

For using as an python api, call below method,
```python
from translate import translate

translated_txt = translate(input_path, output_path, src_lang, tar_lang)
translated_tx.save(output_path)
```

File Structure
translate.py: The main script for translating DOCX documents.
lang_code.yml: A YAML file containing language codes.
Dockerfile: The Dockerfile for building the Docker image.
docker-compose.yml: The Docker Compose file for setting up the Docker environment.
requirements.txt: A file listing the Python dependencies for the project.

## Possible improvement and speedup

Currently it can run 135.8s. If we can utilize multiprocesing or concurrent strategy by only spliting the txt as sentence, and execute all the cpu core then easily reduce the latency. Also we can use GPU machine if avalilabe which also reduce the execution time greatly.


