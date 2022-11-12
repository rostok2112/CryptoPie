import datetime
import random as rnd
from pathlib import Path
from args import args
from utils import shift_string

def cesar_encrypt(text: str) -> str:
    return shift_string(text, current_key, args.borders)
    
def cesar_decrypt(text: str) -> str:
    return shift_string(text, -current_key, args.borders)

def cesar_generate_key() -> int:
    max_key = max(
        map(
            lambda edges: ord(edges[1]) - ord(edges[0]),
            [border.split('-') for border in args.borders]
        )
    )
    return rnd.randint(1, max_key)


def output_to_stdout(output: str, header: str):
    print(f'{header}:\n"""\n{output}\n"""\n') 

def output_to_file(output: str, name_of_file: str):
    with (dest_path / f"output_{datetime.datetime.now().timestamp()}_{name_of_file}").open(mode='w', encoding=args.encoding) as file_output:
        file_output.write(output)

def process_file(path: Path):
    with path.open(encoding=args.encoding) as file_input:
        processed_text = current_handler(file_input.read())
        output_to_file(processed_text, Path(file_input.name).name)
    return processed_text

dest_path = Path(args.destination)

current_method = "cesar"
current_handler = locals()[f"{current_method}_{args.subparser}"] # get corresponding handling function to selected usage purpose and algorythm
current_key = locals()[f"{current_method}_generate_key"]() if getattr(args, "generate_key", False) else args.key # get corresponding keygen function to selected algorythm

def main():
    dest_path.mkdir(parents=True, exist_ok=True)

    print(f"Key: {current_key}\n")
    for i, input_ in enumerate(args.input):
        processed_text = current_handler(input_)
        output_to_file(processed_text, f"Input{i}")
        if args.verbose:
            output_to_stdout(processed_text, f"Input_{i}")
    for path in args.pathes:
        path_ = Path(path)
        if path_.is_dir():
            for file in (path__ for path__ in (path_.rglob("*") if args.recursively else path_.iterdir()) if path__.is_file()):
                processed_text = process_file(file)
                if args.verbose:
                    output_to_stdout(processed_text, file.name)
        else:
            processed_text = process_file(file)
            if args.verbose:
                output_to_stdout(processed_text, file.name)

if __name__ == '__main__':
    main()
