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
                                        "name" : "cesar_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A Cesar cipher cryptographic algorithm for encryption",
                                        },
                                        "args" : [
                                            "cesar",
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
                                            *(set(general_options) - set(["length_key",]))
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
                                ],
                            },
                        ],
                    },
                    {
                        "name" : "decrypt_parser",
                        "handle_func" : "add_parser",
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
                                        "name" : "cesar_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A Cesar cipher cryptographic algorithm for decryption",
                                        },
                                        "args" : [
                                            "cesar",
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
                                            *(set(general_options) - set(["generate_key", "length_key",]))
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
                                            "additive_stream",
                                        ],
                                        "options" : [
                                            *(set(general_options) - set(["generate_key", "length_key",]))
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
                                        "name" : "cesar_parser",
                                        "handle_func" : "add_parser",
                                        "kwargs" : {
                                            "help" : "A Cesar cipher cryptographic algorithm for encryption",
                                        },
                                        "args" : [
                                            "cesar",
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
                                            "help" : "A substitution cipher cryptographic algorithm for encryption",
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
                                            "help" : "An additive stream cipher cryptographic algorithm for encryption",
                                        },
                                        "args" : [
                                            "additive_stream",
                                        ],
                                        "options" : [
                                            "borders",
                                            "length_key",
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
