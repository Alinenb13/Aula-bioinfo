#!/usr/bin/env python3
import sys

def dna_to_rna(dna_sequence):
    return dna_sequence.upper().replace('T', 'U')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dna_file = sys.argv[1]
        with open(dna_file, 'r') as f:
            for line in f:
                if line.startswith('>'):
                    print(line.strip())
                else:
                    print(dna_to_rna(line.strip()))