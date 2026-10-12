#!/usr/bin/env python3
import sys

weights = {
    'Ala': 89.09,  'Arg': 174.20, 'Asn': 132.12, 'Asp': 133.10, 'Cys': 121.16,
    'Glu': 147.13, 'Gln': 146.15, 'Gly': 75.07,  'His': 155.16, 'Ile': 131.17,
    'Leu': 131.17, 'Lys': 146.19, 'Met': 149.21, 'Phe': 165.19, 'Pro': 115.13,
    'Ser': 105.09, 'Thr': 119.12, 'Trp': 204.23, 'Y': 181.19, 'Val': 117.15,
    'Tyr': 181.19, 'Parada': 0.0, 'X': 0.0
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        protein_file = sys.argv[1]
        with open(protein_file, 'r') as f:
            for line in f:
                if not line.startswith('>'):
                    tokens = line.strip().split()
                    print("Cálculo de massa individual por aminoácido:")
                    total_mass = 0.0
                    for token in tokens:
                        if ':' in token:
                            codon, aa = token.split(':')
                            massa = weights.get(aa, 0.0)
                            total_mass += massa
                            print(f"Códão {codon} ({aa}) -> Massa: {massa:.2f} Da")
                    print(f"\nMassa molecular total: {total_mass:.2f} Da")