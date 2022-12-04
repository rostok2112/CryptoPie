import datetime
from importlib import import_module
from pathlib import Path
from arguments import args, attrs

def output_to_stdout(output: str, header: str):
    print(f'{header}:\n"""\n{output}\n"""\n') 

def output_to_file(output: str | bytearray, name_of_file: str, is_binary: bool = False):
    kwargs = {}
    kwargs["mode"] = 'w'
    if not is_binary:
        kwargs["encoding"] = args.encoding
    else:
        kwargs["mode"] += "b"

    with (dest_path / f"output_{datetime.datetime.now().timestamp()}_{name_of_file}").open(**kwargs) as file_output:
        file_output.write(output)

def process_file(path: Path):
    is_binary = current_settings.get(f"{args.purpose}_binary_input", False)
    kwargs = {}
    kwargs["mode"] = 'r'
    if not is_binary:
        kwargs["encoding"] = getattr(args, "encoding", None)
    else:
        kwargs["mode"] += "b"
    with path.open(**kwargs) as file_input:
        processed_text = current_handler(text=file_input.read(), key=current_key, borders=args.borders, encoding=getattr(args, "encoding", None))
        output_to_file(
            processed_text, 
            Path(file_input.name).name, 
            is_binary=current_settings.get(f"{args.purpose}_binary_output", False)
        )
        
    return processed_text

if args.purpose != "generate_key":
    dest_path = Path(args.destination)

current_method_module = import_module(f"{attrs.get(args.purpose).get('module')}.{args.method}") # get corresponding module to selected algorithm
current_handler = getattr(current_method_module, f"{args.method}_{args.purpose}", None) # get corresponding handling function to selected usage purpose and algorithm
current_settings = getattr(current_method_module, f"{args.method}_settings", None) # get corresponding object with some settings

optional_kwargs_generate_key = {}
if key_length := getattr(args, "length_key", False):
    optional_kwargs_generate_key["key_length"]=key_length
current_key = getattr(
    current_method_module, f"{args.method}_generate_key", None
)( # method call
    borders=getattr(args, "borders", None),
    **optional_kwargs_generate_key
) if getattr(args, "generate_key", args.purpose == "generate_key") else getattr(args, "key", None) # get key from corresponding to selected method keygen function or get specified key 

def main():
    if current_key:
        print(f"Key: {current_key}\n")
    if args.purpose != "generate_key":
        dest_path.mkdir(parents=True, exist_ok=True)
        
        for i, input_ in enumerate(args.input):
            processed_text = current_handler(text=input_, key=current_key, borders=getattr(args, "borders", None), encoding=getattr(args, "encoding", None))
            output_to_file(
                processed_text, 
                f"Input{i}",
                is_binary=current_settings.get(f"{args.purpose}_binary_output", False)
            )
            if getattr(args, "verbose", False):
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
