"""
Pathogen Sequence & GC-Content Analyzer
Input: Multi-FASTA file containing viral or bacterial nucleotide sequences.
Output: CSV summary report with sequence lengths, nucleotide counts, and GC%.
"""

import sys
import csv


def parse_fasta(filepath):
    """Reads a FASTA file and returns a dictionary of {header: sequence}."""
    sequences = {}
    current_header = None
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                current_header = line[1:]
                sequences[current_header] = []
            else:
                sequences[current_header].append(line.upper())
    return {header: "".join(seq) for header, seq in sequences.items()}


def calculate_metrics(sequences):
    """Calculates sequence length, base counts, and GC percentage."""
    results = []
    for header, seq in sequences.items():
        length = len(seq)
        gc_count = seq.count("G") + seq.count("C")
        gc_percent = round((gc_count / length) * 100, 2) if length > 0 else 0
        results.append({
            "Sequence_ID": header,
            "Length_bp": length,
            "GC_Content_Percent": gc_percent,
            "A_Count": seq.count("A"),
            "T_Count": seq.count("T"),
            "G_Count": seq.count("G"),
            "C_Count": seq.count("C")
        })
    return results


def save_report(results, output_csv="sequence_summary.csv"):
    """Exports sequence metrics to a CSV file."""
    if not results:
        return
    keys = list(next(iter(results)).keys())
    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)
    print(f"Analysis complete. Report saved to {output_csv}")


if __name__ == "__main__":
    args = sys.argv[1:]
    input_file = args.pop(0) if args else "sample_sequences.fasta"
    seqs = parse_fasta(input_file)
    metrics = calculate_metrics(seqs)
    save_report(metrics)
