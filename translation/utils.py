from typing import List, Tuple, Any
import argparse
import signal

def is_equation(element: Any) -> bool:
    """Check if the element contains an equation."""
    omml_ns = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
    return any(child.tag.startswith(omml_ns) for child in element.iter())

def is_image(run: Any) -> bool:
    """Check if the run contains an image."""
    return bool(
        run._element.findall(
            ".//w:drawing",
            {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"},
        )
    )

def preserve_special_elements(paragraph) -> List[Tuple[Any, Any]]:
    """Extract and preserve special elements like images and equations."""
    special_elements = []
    for i, run in enumerate(paragraph.runs):
        if is_image(run) or (hasattr(run._element, 'iter') and is_equation(run._element)):
            # Store the run object and its index
            special_elements.append((i, run._element))
    return special_elements

def parse_args() -> None:
    signal.signal(signal.SIGINT, lambda signal_number, frame: destroy())
    program = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100))
    program.add_argument('--inpur-path', help='startup website name or prodcut name', dest='input_path', default='Input_docx')
    program.add_argument('--output-path', help='select an target image or video', dest='output_path', default='./output_docx')
    program.add_argument('--src-lang', help='select output file or directory', type= str, dest='src_lang', default='English')
   
    program.add_argument('--tar-lang', help='select output file or directory', type= str, dest='tar_lang', default='French')
    # program.add_argument('--device', help='machine type (choices: cpu, cuda, ...)', dest='target_lang', default="fr")
    # program.add_argument('--model-name', help='vllm model name', dest='model_name', action='store_true', default="Qwen/Qwen2.5-0.5B-Instruct")

    args = program.parse_args()
    return args