# Pathogen Sequence & GC-Content Analyzer

## Overview
A Python tool developed to parse multi-FASTA genomic files, compute nucleotide frequencies and GC content, and export summary metrics for downstream viral and bacterial sequence analysis.

## Tools & Libraries Used
* **Language:** Python 3.x (Standard Library: `sys`, `csv`)
* **Environment:** macOS / Linux / Bash

## How to Run
1. Download or clone this repository, then navigate into the project folder:
   `cd pathogen-fasta-analyzer`
2. Run the script with the included sample dataset:
   `python3 analyze_fasta.py sample_sequences.fasta`

## Sample Output
Generates `sequence_summary.csv` containing `Sequence_ID`, `Length_bp`, `GC_Content_Percent`, and individual base counts (`A`, `T`, `G`, `C`) for every FASTA record.
