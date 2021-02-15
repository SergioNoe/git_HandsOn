#!/usr/bin/env python

# Imports
import sys, re
from argparse import ArgumentParser

# Command arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Show help in command
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Obtaining arguments passed in command
args = parser.parse_args()

# Avoiding lower case letters
args.seq = args.seq.upper()

# Check sequence type
if re.search('^[ACGTU]+$', args.seq):
    # If the sequence has T and not U, is DNA
    if re.search('T', args.seq) and not re.search('U', args.seq):
        print ('The sequence is DNA')
    # If the sequence has U and not T, is DNA
    elif re.search('U', args.seq) and not re.search('T', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence is not DNA nor RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Search for a motif inside the sequence
if args.motif:
  args.motif = args.motif.upper()
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if re.match(args.motif, args.seq):
    print("FOUND IT")
  else:
    print("NOT FOUND IT")
