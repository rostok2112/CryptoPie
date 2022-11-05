import argparse
import pkgutil
import encodings

parser = argparse.ArgumentParser(
    prog = 'CesarEncryptor',
    description='Simple CLI Cesar Encryptor/Decryptor'
)

parser.add_argument(
    "pathes",
    nargs='+',
    type=str,
    help="A path/pathes to a file/files/directory/directories"
)

parser.add_argument(
    "-d",
    "--destination",
    "--dest",
    default="output",
    type=str,
    help='Destination path'
)

parser.add_argument(
    "-r",
    "--recursively", 
    action="store_true",
    help="Recursively encrypt/decrypt everuthing in input path. Doesnt do anything if file on input"
)
parser.add_argument(
    "-s",
    "--shift", 
    default=2, 
    type=int, 
    help="The value by which the letters will be shifted relative to the alphabet"
)
parser.add_argument(
    "-b",
    "--borders", 
    default=("a-z", "A-Z"),
    nargs='*',
    type=str,
    help="Alphabet/alphabets borders in format: a-z A-Z а-я А-Я"
)

false_positives = set(["aliases"])
encodings_set = set(name for imp, name, ispkg in pkgutil.iter_modules(encodings.__path__) if not ispkg)
encodings_set.difference_update(false_positives)

parser.add_argument(
    "-e",
    "--encoding", 
    choices=list(encodings_set),
    default="UTF-8",
    help="Encoding of texts of input and output files"
)

args = parser.parse_args()
