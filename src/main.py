import argparse
from utils import parse_fasta, gc_content

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
