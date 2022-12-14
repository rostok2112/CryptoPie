import argparse
from arguments.options import general_options 

argparse_args = [
    {
        "name" : "parser",
        "kwargs" : {
            "prog" : "python crypto_pie.py",
            "description" : "Encryptor/Decryptor with CLI interface",
        },
        "handle_func" : argparse.ArgumentParser,
        "args" : [

        ],
        "options" : [
        
        ],
        "childs" : [
            {
                "name" : "purposes",
                "handle_func" : "add_subparsers",
                "kwargs" : {
                    "help" : "List of purposes handlers",
                    "dest" : "purpose",
                },
                "args" : [

                ],
                "childs" : [
                    {
                        "name" : "encrypt_parser",
                        "handle_func" : "add_parser",
                        "attrs" : {
                            "module" : "crypto_methods",
                        },
                        "kwargs" : {
                            "help" : "Encrypt options",
                        },
                        "args" : [
                            "encrypt",
                        ],
                        "options" : [

                        ],
                        "childs" : [
                            {
                                "name" : "methods",
                                "handle_func" : "add_subparsers",
                                "kwargs" : {
                                    "help" : "A cryptographic algorithm for encryption",
                                    "dest" : "method",
                                },
                                "args" : [

                                ],
                                "childs" : [
                                    {
                                        "name" : "ceasar_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A Ceasar cipher cryptographic algorithm for encryption",
                                        },
                                        "args" : [
                                            "ceasar",
                                        ],
                                        "options" : [
                                        *(set(general_options) - set(["length_key",])) 
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "sybstitution_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A substitution cipher cryptographic algorithm for encryption",
                                        },
                                        "args" : [
                                            "sybstitution",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["length_key", "borders"]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "additive_stream_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "An additive stream cipher cryptographic algorithm for encryption",
                                        },
                                        "args" : [
                                            "additive_stream",
                                        ],
                                        "options" : [
                                            *((set(general_options) | set(["length_key",])) - set([]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "s_des_block_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A simplified data enceryption standart block cipher cryptographic algorithm for encryption",
                                        },
                                        "args" : [
                                            "s-des-block",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["length_key", "borders", "verbose"]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "rsa_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A RSA asymetric cipher cryptographic algorithm",
                                        },
                                        "args" : [
                                            "rsa",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["length_key", "borders", "verbose"]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "name" : "decrypt_parser",
                        "handle_func" : "add_parser",
                        "attrs" : {
                            "module" : "crypto_methods",
                        },
                        "kwargs" : {
                            "help" : "Decrypt options",
                        },
                        "args" : [
                            "decrypt",
                        ],
                        "options" : [

                        ],
                        "childs" : [
                            {
                                "name" : "methods",
                                "handle_func" : "add_subparsers",
                                "kwargs" : {
                                    "help" : "A cryptographic algorithm for decryption",
                                    "dest" : "method",
                                },
                                "args" : [

                                ],
                                "childs" : [
                                    {
                                        "name" : "ceasar_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A Ceasar cipher cryptographic algorithm for decryption",
                                        },
                                        "args" : [
                                            "ceasar",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["generate_key", "length_key",]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                        
                                    },
                                    {
                                        "name" : "sybstitution_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A substitution cipher cryptographic algorithm for decryption",
                                        },
                                        "args" : [
                                            "sybstitution",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["generate_key", "borders", "length_key",]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "additive_stream_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "An additive stream cipher cryptographic algorithm for decryption",
                                        },
                                        "args" : [
                                            "additive-stream",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["generate_key", "length_key",]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "s_des_block_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A simplified data enceryption standart block cipher cryptographic algorithm for decryption",
                                        },
                                        "args" : [
                                            "s-des-block",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["generate_key", "length_key", "borders"]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "rsa_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A RSA asymetric cipher cryptographic algorithm",
                                        },
                                        "args" : [
                                            "rsa",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["generate_key", "length_key"]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "name" : "generate_key_parser",
                        "handle_func" : "add_parser",
                        "attrs" : {
                            "module" : "crypto_methods",
                        },
                        "kwargs" : {
                            "help" : "Generate key options",
                        },
                        "args" : [
                            "generate_key",
                        ],
                        "options" : [

                        ],
                        "childs" : [
                            {
                                "name" : "methods",
                                "handle_func" : "add_subparsers",
                                "kwargs" : {
                                    "help" : "A cryptographic algorithm for encryption",
                                    "dest" : "method",
                                },
                                "args" : [

                                ],
                                "childs" : [
                                    {
                                        "name" : "ceasar_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A Ceasar cipher cryptographic algorithm",
                                        },
                                        "args" : [
                                            "ceasar",
                                        ],
                                        "options" : [
                                            "borders",
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "sybstitution_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A substitution cipher cryptographic algorithm",
                                        },
                                        "args" : [
                                            "sybstitution",
                                        ],
                                        "options" : [
                                            "borders",
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "additive_stream_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "An additive stream cipher cryptographic algorithm",
                                        },
                                        "args" : [
                                            "additive-stream",
                                        ],
                                        "options" : [
                                            "borders",
                                            "length_key",
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "s_des_block_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A simplified data enceryption standart block cipher cryptographic algorithm",
                                        },
                                        "args" : [
                                            "s-des-block",
                                        ],
                                        "options" : [

                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                    {
                                        "name" : "rsa_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A RSA asymetric cipher cryptographic algorithm",
                                        },
                                        "args" : [
                                            "rsa",
                                        ],
                                        "options" : [

                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "name" : "encode_parser",
                        "handle_func" : "add_parser",
                        "attrs" : {
                            "module" : "encode_methods",
                        },
                        "kwargs" : {
                            "help" : "Encode options",
                        },
                        "args" : [
                            "encode",
                        ],
                        "options" : [

                        ],
                        "childs" : [
                            {
                                "name" : "methods",
                                "handle_func" : "add_subparsers",
                                "kwargs" : {
                                    "help" : "An encoding algorithm",
                                    "dest" : "method",
                                },
                                "args" : [

                                ],
                                "childs" : [
                                    {
                                        "name" : "b64_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A Base64 encoding algorithm",
                                        },
                                        "args" : [
                                            "b64",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["key", "generate_key", "length_key", "borders"]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "name" : "decode_parser",
                        "handle_func" : "add_parser",
                        "attrs" : {
                            "module" : "encode_methods",
                        },
                        "kwargs" : {
                            "help" : "Decode options",
                        },
                        "args" : [
                            "decode",
                        ],
                        "options" : [

                        ],
                        "childs" : [
                            {
                                "name" : "methods",
                                "handle_func" : "add_subparsers",
                                "kwargs" : {
                                    "help" : "A decoding algorithm",
                                    "dest" : "method",
                                },
                                "args" : [

                                ],
                                "childs" : [
                                    {
                                        "name" : "b64_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A Base64 decoding algorithm",
                                        },
                                        "args" : [
                                            "b64",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["key", "generate_key", "length_key", "borders"]))
                                        ],
                                        "childs" : [
                                        
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        ],
    },
]
