import argparse
def parse_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        seq_id = ""
        seq = ""
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq_id:
                    sequences[seq_id] = seq
                seq_id = line[1:]
                seq = ""
            else:
                seq += line
        
        if seq_id:
            sequences[seq_id] = seq

    return sequences


def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    return (g + c) / len(sequence) * 100


def main():
    parser = argparse.ArgumentParser(description="FASTA sequence analyzer")
    parser.add_argument("--input", required=True, help="Path to FASTA file")

    args = parser.parse_args()
    file_path = args.input

    sequences = parse_fasta(file_path)

    for seq_id, seq in sequences.items():
        print(f"ID: {seq_id}")
        print(f"Length: {len(seq)}")
        print(f"GC Content: {gc_content(seq):.2f}%")
        print("-" * 30)


if __name__ == "__main__":
    main()
