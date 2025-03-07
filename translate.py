import os
import yaml
from translation.translate_docx import translate_docx
from translation.utils import parse_args


def main():
    """
    Main entry point for document translation.
    Translates a sample document from English to French Canadian.
    """
    args = parse_args()
    # Open the YAML file and load its contents
    with open('lang_code.yml', 'r') as file:
        trans_code = yaml.safe_load(file)

    input_paths = os.listdir(args.input_path)
    print(input_paths)
    for input_path in input_paths:  
        base_name = os.path.basename(input_path).split('.')[0]
        output_path = f"{args.output_path}/{base_name}_{trans_code[args.tar_lang]}.docx"
        input_path = args.input_path + '/' + input_path
        translate_docx(args, input_path, output_path, source_lang=trans_code[args.src_lang], target_lang=trans_code[args.tar_lang])
        print(f"Document translated and saved to '{output_path}'.")


def translate(input_path, output_path, source_lang, target_lang):
    """
    Translates the given DOCX document from the source language to the target language and saves it.

    Args:
        input_path (str): The path to the DOCX file to be translated.
        output_path (str): The path to save the translated DOCX file.
        src_lang (str): The source language code (e.g., 'en' for English).
        tar_lang (str): The target language code (e.g., 'fr' for French).

    Returns:
        None: The function saves the translated document to the provided output path.
    """
    args = parse_args()
    with open('lang_code.yml', 'r') as file:
        trans_code = yaml.safe_load(file)

    return translate_docx(args, input_path, output_path, source_lang=trans_code[source_lang], target_lang=trans_code[source_lang])


if __name__=="__main__":


    main()
