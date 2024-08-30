def motif_finding():
    print("Finding DNA sequence motifs in Python console")
    print("You can exit state 'q' at any time\n")

    while True:
        # Let's ask the user to enter a DNA sequence

        dna_sequence = input("Enter a DNA sequence( A, T, C, G ):")

        if dna_sequence.lower() == "q":
            print("Exiting...")
            break

        # Let's convert the string to uppercase
        dna_sequence = dna_sequence.upper()

        # Let's check the validity of the  DNA sequence
        valid_bases = set("ATCG")

        if not set(dna_sequence).issubset(valid_bases):
            print("Invalid sequence. Please try again.")
            continue

        break  # We exit the loop when a valid DNA sequence is entered

    while True:
        # Let's ask the user to enter a motif sequence
        motif_sequence = input("Enter a motif sequence( A, T, C, G ):")

        if motif_sequence.lower() == "q":
            print("Exiting...")
            break

        # Let's convert the string to uppercase
        motif_sequence = motif_sequence.upper()

        # Let's check the validity of the  motif sequence
        valid_bases = set("ATCG")

        if not set(motif_sequence).issubset(valid_bases):
            print("Invalid sequence. Please try again.")
            continue

        # Finding Motif Positions
        positions = find_motif_positions(dna_sequence, motif_sequence)
        print("Motif positions:", positions)


def find_motif_positions(dna_sequence, motif_sequence):
    positions = []
    start = 0

    while True:
        
        pos = dna_sequence.find(motif_sequence, start)

        if pos == -1:  # If motif is not found, exit the loop
            break

        positions.append(pos)
        # We start the next search from where it is located
        start = pos + 1

    return positions


if __name__ == "__main__":
    motif_finding()
