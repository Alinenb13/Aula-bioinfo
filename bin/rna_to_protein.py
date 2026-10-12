#!/usr/bin/env python3
import sys
import glob

g_code = {
    'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCU': 'Ala',
    'UGC': 'Cys', 'UGU': 'Cys',
    'GAC': 'Asp', 'GAU': 'Asp',
    'GAA': 'Glu', 'GAG': 'Glu',
    'UUC': 'Phe', 'UUU': 'Phe',
    'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGU': 'Gly',
    'CAC': 'His', 'CAU': 'His',
    'AUA': 'Ile', 'AUC': 'Ile', 'AUU': 'Ile',
    'AAA': 'Lys', 'AAG': 'Lys',
    'UUA': 'Leu', 'UUG': 'Leu', 'CUA': 'Leu', 'CUC': 'Leu', 'CUG': 'Leu', 'CUU': 'Leu',
    'AUG': 'Met',
    'AAC': 'Asn', 'AAU': 'Asn',
    'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCU': 'Pro',
    'CAA': 'Gln', 'CAG': 'Gln',
    'AGA': 'Arg', 'AGG': 'Arg', 'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGU': 'Arg',
    'AGC': 'Ser', 'AGU': 'Ser', 'UCA': 'Ser', 'UCC': 'Ser', 'UCG': 'Ser', 'UCU': 'Ser',
    'ACC': 'Thr', 'ACG': 'Thr', 'ACU': 'Thr', 'ACA': 'Thr',
    'GUA': 'Val', 'GUC': 'Val', 'GUG': 'Val', 'GUU': 'Val',
    'UGG': 'Trp',
    'UAC': 'Tyr', 'UAU': 'Tyr',
    'UAA': 'Parada', 'UAG': 'Parada', 'UGA': 'Parada'
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        rna_file = sys.argv[1]
    else:
        files = glob.glob("*.txt")
        rna_file = files[0] if files else "rna.txt"

    with open(rna_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                print(line.strip())
            else:
                rna = line.strip().upper()
                print("Codons -> Aminoácidos:")
                pairs = []
                for i in range(0, len(rna) - 2, 3):
                    codon = rna[i:i+3]
                    aa = g_code.get(codon, 'X')
                    pairs.append(f"{codon}:{aa}")
                print(" ".join(pairs))