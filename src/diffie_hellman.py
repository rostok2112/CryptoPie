import argparse
import random
import utils

PRIME_NUMBER_LENGHT_BITS = 11
PRIME_NUMBER_LENGHT_DIGITS = 4

parser = argparse.ArgumentParser(description="Diffie Hellman protocol",)
subparser = parser.add_subparsers(
    help="Generate public key or generate joint key", 
    dest="purpose",
)

get_public_key_parser = subparser.add_parser(
    "get-public-key",
    help="Generate public key of this user by given/generated public prime number, public primitive root of this prime number and privite key of this user", 
)
get_joint_key_parser = subparser.add_parser(
    "get-joint-key",
    help="Get joint with other user key by public key of other user, public prime number and privite key of this user",
)

get_public_key_parser.add_argument(
    "-gp",
    "--generate-prime-number",  
    action="store_true",        
    help="Generate random public prime number",
)
get_public_key_parser.add_argument(
    "-gr",
    "--generate-primitive-root",  
    action="store_true",        
    help="Generate first public primitive root for given/generated prime number",
)
get_public_key_parser.add_argument(
    "-gk",
    "--generate-privite-key",  
    action="store_true",        
    help="Generate privite key",
)
get_public_key_parser.add_argument(
    "-p",
    "--prime-number",  
    type=int,        
    help="Public prime number",
)
get_public_key_parser.add_argument(
    "-r",
    "--primitive-root",  
    type=int,         
    help="Public primitive root for given prime number",
)
get_public_key_parser.add_argument(
    "-k",
    "--privite-key",
    type=int,   
    help="Privite key (1 <= privite_key <= given prime number - 1)",
)

get_joint_key_parser.add_argument(
    "-p",
    "--prime-number",  
    type=int,
    required=True,       
    help="Public prime number",
)
get_joint_key_parser.add_argument(
    "-pvk",
    "--privite-key",
    type=int,
    required=True,   
    help="Privite key of this user",
)
get_joint_key_parser.add_argument(
    "-pbk",
    "--public-key",
    type=int,
    required=True,
    help="Public key of other user",
)

args = parser.parse_args()
if args.purpose == "get-public-key":
    if not getattr(args, "generate_prime_number", False) and not getattr(args, "prime_number", False):
        parser.error("Specify a prime number or set -gp (--generate-prime-number)")
    if not getattr(args, "generate_primitive_root", False) and not getattr(args, "primitive_root", False):
        parser.error("Specify a primitive root for given prime number or set -gr (--generate-primitive-root)")
    if not getattr(args, "generate_privite_key", False) and not getattr(args, "privite_key", False):
        parser.error("Specify a primitive root for given prime number or set -gk (--generate-privite-key)")

def main():
    if args.purpose == "get-public-key":
        if getattr(args, "generate_prime_number", False):
            prime_number = 0
            while len(str(prime_number)) < PRIME_NUMBER_LENGHT_DIGITS:
                prime_number = utils.get_random_prime(PRIME_NUMBER_LENGHT_BITS)
        else:
            prime_number = args.prime_number
        if getattr(args, "generate_primitive_root", False):
            primitive_root = utils.get_first_primitive_root(prime_number)
        else:
            primitive_root = args.primitive_root
        if getattr(args, "generate_privite_key", False):
            privite_key = random.randint(1, prime_number - 1)
        else:
            privite_key = args.privite_key
        
        public_key = (primitive_root ** privite_key) % prime_number
        
        print(
            f"Output:\n\n"
            f"Prime number:\n{prime_number}\n"
            f"Primitive root:\n{primitive_root}\n"
            f"Private key:\n{privite_key}\n"
            f"Public key:\n{public_key}"
        )
    elif args.purpose == "get-joint-key":
        prime_number = args.prime_number
        privite_key = args.privite_key
        public_key = args.public_key

        joint_key = (public_key ** privite_key) % prime_number

        print(
            f"Output:\n\n"
            f"Prime number:\n{prime_number}\n"
            f"Private key:\n{privite_key}\n"
            f"Public key:\n{public_key}\n"
            f"Joint key:\n{joint_key}"
        )
    
if __name__ == '__main__':
    main()