#!/usr/bin/env python3
import argparse
from collections import Counter

def read_fastq_sequences(filename):
    """Generator that yields sequences from a FASTQ file."""
    with open(filename, 'r') as f:
        while True:
            header = f.readline().strip()
            if not header:
                break  # EOF
            seq = f.readline().strip()
            f.readline()  # Plus line
            f.readline()  # Quality line
            yield seq


def count_kmers(sequences, k):
    """Count all k-mers of length k from a list or generator of sequences."""
    counts = Counter()
    for seq in sequences:
        seq = seq.upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            counts[kmer] += 1
    return counts


def main():
    parser = argparse.ArgumentParser(description="Count k-mers from a FASTQ file.")
    parser.add_argument("fastq", help="Input FASTQ file")
    parser.add_argument("k", type=int, help="k-mer size")
    parser.add_argument(
        "-n", "--top", type=int, default=None,
        help="Limit output to the top N most abundant k-mers"
    )
    args = parser.parse_args()

    sequences = read_fastq_sequences(args.fastq)
    kmer_counts = count_kmers(sequences, args.k)

    # Sort k-mers by count (descending), then alphabetically
    sorted_kmers = sorted(kmer_counts.items(), key=lambda x: (-x[1], x[0]))

    if args.top:
        sorted_kmers = sorted_kmers[:args.top]

    # Print results
    print("kmer\tcount")
    for kmer, count in sorted_kmers:
        print(f"{kmer}\t{count}")


if __name__ == "__main__":
    main()
