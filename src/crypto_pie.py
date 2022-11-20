import datetime
from importlib import import_module
from pathlib import Path
from arguments import args

def output_to_stdout(output: str, header: str):
    print(f'{header}:\n"""\n{output}\n"""\n') 

def output_to_file(output: str, name_of_file: str):
    with (dest_path / f"output_{datetime.datetime.now().timestamp()}_{name_of_file}").open(mode='w', encoding=args.encoding) as file_output:
        file_output.write(output)

def process_file(path: Path):
    with path.open(encoding=args.encoding) as file_input:
        processed_text = current_handler(file_input.read(), current_key, args.borders)
        output_to_file(processed_text, Path(file_input.name).name)
    return processed_text

dest_path = Path(args.destination)

current_method_module = import_module(f"crypto_methods.{args.method}") # get corresponding module to selected algorithm
current_handler = getattr(current_method_module, f"{args.method}_{args.purpose}", None) # get corresponding handling function to selected usage purpose and algorithm
current_key = getattr(current_method_module, f"{args.method}_generate_key", None)(args.borders) if getattr(args, "generate_key", False) else args.key # get key from corresponding to selected method keygen function or get specified key 

def main():
    dest_path.mkdir(parents=True, exist_ok=True)

    print(f"Key: {current_key}\n")
    for i, input_ in enumerate(args.input):
        processed_text = current_handler(input_, current_key, args.borders)
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
