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
