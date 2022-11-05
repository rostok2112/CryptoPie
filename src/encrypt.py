import datetime
from pathlib import Path
from args import args
from utils import recognise_letter_borders, shift_letter

def encrypt_file(path):
        dest_path = Path(args.destination)
        dest_path.mkdir(parents=True, exist_ok=True)
        with path.open(encoding=args.encoding) as file_input:
            with (dest_path / f"output_{int(datetime.datetime.now().timestamp())}_{Path(file_input.name).name}").open(mode='w', encoding=args.encoding) as file_output:
                file_output.write(
                    ""
                        .join([
                            shift_letter(
                                letter, 
                                args.shift, 
                                recognise_letter_borders(
                                    letter, 
                                    [border.split('-') for border in args.borders]
                                )
                            ) for letter in file_input.read()
                        ])
                )

def main():
    for path in args.pathes:
        path_ = Path(path)
        if path_.is_dir():
            
            for file in (path__ for path__ in (path_.rglob("*") if args.recursively else path_.iterdir()) if path__.is_file()):
                encrypt_file(file)
        else:
            encrypt_file(path_)

if __name__ == '__main__':
    main()
