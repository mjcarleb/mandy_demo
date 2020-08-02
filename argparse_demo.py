import sys
import argparse

parser = argparse.ArgumentParser()

# The first argument will be "key" to get actual value
parser.add_argument("encoder_type",
                    type=str,
                    help="first/only argument options:  bert roberta lstm")
parser.add_argument("nerd_IQ",
                    type=int,
                    help="IQ of nerd running program")
parser.add_argument("--nerd_name",
                    type=str,
                    help="name of nerd")

args = parser.parse_args()

# Left and right names can be different
# But named tuple argument matches string passed to add_argument
encoder_type = args.encoder_type
nerd_IQ = args.nerd_IQ
nerd_name = args.nerd_name

if nerd_name is None:
    print("The user did not give us a name")
else:
    print(f"The nerd's name is {nerd_name}")

print(f"encoder type = {encoder_type}")
print(f"nerd IQ = {nerd_IQ} with type={type(nerd_IQ)}")

"""
arg0 = sys.argv[0]
print(f"The first sys.argv is ALWAYS the source file of the script={arg0}")
print()

arg1 = sys.argv[1]
print(f"The user gave {arg1} as first positional option")
print(f"Type of arg1 is {type(arg1)}")

arg2 = sys.argv[2]
print(f"The user gave {arg2} as first positional option")
"""
