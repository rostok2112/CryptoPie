import datetime
from pathlib import Path
from args import args
from utils import recognise_letter_borders, shift_letter

dest_path = Path(args.destination)

def output_to_stdout(output: str, header: str):
    print(f'{header}:\n"""\n{output}\n"""\n') 

def output_to_file(output: str, name_of_file: str):
    with (dest_path / f"output_{datetime.datetime.now().timestamp()}_{name_of_file}").open(mode='w', encoding=args.encoding) as file_output:
        file_output.write(output)

def encrypt_text(text: str) -> str:
    return (
        ""
            .join([
                shift_letter(
                    letter, 
                    args.shift, 
                    recognise_letter_borders(
                        letter, 
                        [border.split('-') for border in args.borders]
                    )
                ) for letter in text
            ])
    )

def encrypt_file(path: Path):
    with path.open(encoding=args.encoding) as file_input:
        encrypted_text = encrypt_text(file_input.read())
        output_to_file(encrypted_text, Path(file_input.name).name)
    return encrypted_text

def main():
    dest_path.mkdir(parents=True, exist_ok=True)

    for i, input_ in enumerate(args.input):
        encrypted_text = encrypt_text(input_)
        output_to_file(encrypted_text, f"Input{i}")
        if args.verbose:
            output_to_stdout(encrypted_text, f"Input_{i}")
    for path in args.pathes:
        path_ = Path(path)
        if path_.is_dir():
            for file in (path__ for path__ in (path_.rglob("*") if args.recursively else path_.iterdir()) if path__.is_file()):
                encrypted_text = encrypt_file(file)
                if args.verbose:
                    output_to_stdout(encrypted_text, file.name)
        else:
            encrypted_text = encrypt_file(file)
            if args.verbose:
                output_to_stdout(encrypted_text, file.name)

if __name__ == '__main__':
    main()