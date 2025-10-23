#!/usr/bin/env python3

from collections import Counter
import math

# --- Helper functions ---

def read_fastq_sequences(filename):
    with open(filename, 'r') as f:
        while True:
            header = f.readline().strip()
            if not header:
                break
            seq = f.readline().strip()
            f.readline()
            f.readline()
            yield seq

def count_kmers(sequences, k):
    counts = Counter()
    for seq in sequences:
        seq = seq.upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            counts[kmer] += 1
    return counts

def shannon_entropy(seq):
    freqs = Counter(seq)
    entropy = 0.0
    for base, count in freqs.items():
        p = count / len(seq)
        entropy -= p * math.log2(p)
    return entropy

def get_best_extension(kmer_counts, prefix, k):
    best_kmer = None
    best_count = 0
    for base in "ACGT":
        candidate = prefix + base
        if candidate in kmer_counts:
            if kmer_counts[candidate] > best_count:
                best_kmer = candidate
                best_count = kmer_counts[candidate]
    return best_kmer, best_count

def extend_contig(seed, kmer_counts, k):
    contig = seed

    # Extend forward
    prefix = contig[-(k-1):]
    while True:
        next_kmer, count = get_best_extension(kmer_counts, prefix, k)
        if not next_kmer:
            break
        contig += next_kmer[-1]
        kmer_counts[next_kmer] -= 1
        if kmer_counts[next_kmer] <= 0:
            del kmer_counts[next_kmer]
        prefix = contig[-(k-1):]

    # Extend backward
    suffix = contig[:k-1]
    while True:
        best_kmer = None
        best_count = 0
        for base in "ACGT":
            candidate = base + suffix
            if candidate in kmer_counts and kmer_counts[candidate] > best_count:
                best_kmer = candidate
                best_count = kmer_counts[candidate]
        if not best_kmer:
            break
        contig = best_kmer[0] + contig
        kmer_counts[best_kmer] -= 1
        if kmer_counts[best_kmer] <= 0:
            del kmer_counts[best_kmer]
        suffix = contig[:k-1]

    return contig

def inchworm_assemble(kmer_counts, k, min_entropy=1.5, min_count=1):
    assembled_contigs = []
    while True:
        if not kmer_counts:
            break
        seed, count = max(kmer_counts.items(), key=lambda x: x[1])
        if count < min_count:
            break
        if shannon_entropy(seed) < min_entropy:
            del kmer_counts[seed]
            continue
        contig = extend_contig(seed, kmer_counts, k)
        assembled_contigs.append(contig)
    return assembled_contigs


# --- Create synthetic FASTQ file ---
fastq_content = """@read1
ATGCGATGCA
+
IIIIIIIIII
@read2
TGCGATGCAT
+
IIIIIIIIII
@read3
GCGATGCATG
+
IIIIIIIIII
@read4
CATGCGATGC
+
IIIIIIIIII
"""

with open("test_reads.fastq", "w") as f:
    f.write(fastq_content)

# --- Run the assembler ---
k = 5
seqs = read_fastq_sequences("test_reads.fastq")
kmer_counts = count_kmers(seqs, k)

contigs = inchworm_assemble(kmer_counts, k, min_entropy=1.5, min_count=1)

print("Assembled contigs:")
for i, c in enumerate(contigs, 1):
    print(f">contig_{i}\n{c}")
