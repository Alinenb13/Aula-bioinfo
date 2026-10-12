#!/usr/bin/env nextflow

nextflow.enable.dsl=2

params.dna = "$projectDir/data/dna.fa"

process TRANSCRIPTION {
    input:
    path dna_file

    output:
    path "rna.txt"

    script:
    """
    python3 ${projectDir}/bin/dna_to_rna.py ${dna_file} > rna.txt
    """
}

process TRANSLATION {
    input:
    path rna_file

    output:
    path "protein.txt"

    script:
    """
    python3 ${projectDir}/bin/rna_to_protein.py ${rna_file} > protein.txt
    """
}

process MASS_CALCULATION {
    input:
    path protein_file

    output:
    path "mass_result.txt"

    script:
    """
    python3 ${projectDir}/bin/protein_mass.py ${protein_file} > mass_result.txt
    """
}

workflow {
    dna_ch = Channel.fromPath(params.dna)
    
    rna_out = TRANSCRIPTION(dna_ch)
    protein_out = TRANSLATION(rna_out)
    MASS_CALCULATION(protein_out)
}