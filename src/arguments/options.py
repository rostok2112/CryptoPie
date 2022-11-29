import pkgutil
import encodings

# + Start of getting set of encodings
false_positives = set(["aliases"])
encodings_set = set(name for imp, name, ispkg in pkgutil.iter_modules(encodings.__path__) if not ispkg)
encodings_set.difference_update(false_positives)
# + End of getting set of encodings

general_options = {
    "input" : {
        "kwargs" : {
            "nargs" : "*",
            "type" : str,
            "action" : "extend",
            "default" : [],
            "help" : "An input text for processing",
        },
        "args" : [
            "input",
        ],
    },
    "pathes" : {
        "kwargs" : {
            "nargs" : "*",
            "type" : str,
            "action" : "extend",
            "default" : [],
            "help" : "A path/pathes to a input file/files/directory/directories",

        },
        "args" : [
            "-p",
            "--pathes",
        ],
    },
    "destination" : {
        "kwargs" : {
            "type" : str,
            "default" : "output",
            "help" : "Destination path",
        },
        "args" : [
            "-d",
            "--destination",
            "--dest",
        ],
    },
    "recursively" : {
        "kwargs" : {
            "action" : "store_true",
            "help" : "Recursively encrypt/decrypt everuthing in input path. Doesnt do anything if file on input",

        },
        "args" : [
            "-r",
            "--recursively",
        ],
    },
    "verbose" : {
        "kwargs" : {
            "action" : "store_true",
            "help" : "Print results into stdout",

        },
        "args" : [
            "-v",
            "--verbose",
        ],
    },
    "borders" : {
        "kwargs" : {
            "nargs" : '*',
            "action" : "extend",
            "default" : ["a-z", "A-Z"],
            "help" : "Alphabet/alphabets borders in format: a-z A-Z а-я А-Я",

        },
        "args" : [
            "-b",
            "--borders",
        ],
    },
    "encoding" : {
        "kwargs" : {
            "choices" : list(encodings_set),
            "default" : "UTF-8",
            "help" : "Encoding of texts of input and output files",

        },
        "args" : [
            "-e",
            "--encoding",
        ],
    },
    "key" : {
        "kwargs" : {
            "help" : "The value by which an input will be encrypted/decrypted",
        },
        "args" : [
            "-k",
            "--key",
        ],
    },
    "generate_key" : {
         "kwargs" : {
            "help" : "Generate random key",
            "action" : "store_true",
        },
        "args" : [
            "-g",
            "--generate-key",
        ],
    },
    "length_key" : {
         "kwargs" : {
            "help" : "Specify key length for random key",
            "type" : int,
        },
        "args" : [
            "-l",
            "--length-key",
        ],
    },
}
