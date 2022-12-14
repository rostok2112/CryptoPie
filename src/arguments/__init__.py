from arguments.options import general_options
from arguments.argparse_args import argparse_args

def traversal(node, parent=None):
    def handle(node_, parent_):
        handle_func = node_.get("handle_func")
        node__ = globals()[node_.get("name")] = (
            getattr(
                parent_, handle_func
            ) if type(handle_func) == str else handle_func
        )(*node_.get("args"), **node_.get("kwargs"))
        node_["is_handled"] = True
        
        for arg in node_.get("options", []):
            arg_ = general_options.get(arg)
            node__.add_argument(*arg_["args"], **arg_["kwargs"])
        if node_.get("attrs"):
            attrs[node_.get("args")[0]] = node_.get("attrs")
    if not node.get("is_handled"):
        handle(node, parent)

    for child in node.get("childs", []):
        child_parent = globals().get(node.get("name"))
        handle(child, child_parent)
        traversal(child, child_parent)
attrs = {}
for obj in argparse_args: 
    traversal(obj)

args = parser.parse_args()

if not getattr(args, "purpose", False):
    parser.error("Specify a purpose of use")
if not getattr(args, "method", False):
    parser.error("Specify an algorithm")

setattr(args, "purpose", args.purpose.replace('-', '_').lower())
setattr(args, "method", args.method.replace('-', '_').lower())

if args.purpose != "generate_key" and  not len(args.input) and not len(args.pathes):
   parser.error("At least one of input texts or input pathes (--pathes) required")

if args.purpose == "encrypt" and bool(args.key) == bool(args.generate_key): # if not or specified at the same time 
   parser.error("Specify key by -k (--key) key OR set -g (--generate_key) (not at the same time)")

if args.purpose == "decrypt" and not args.key:
    parser.error("Specify key by -k (--key) key for decryption")
