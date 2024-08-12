

def conversion():
    print("Python console convert the DNA sequence to an RNA sequence")
    print("You can exit state 'q' at any time\n")


    while True:
        #Let's ask the user to enter a DNA sequence

        dna_sequence = input(
        "Enter a DNA sequence( A, T, C, G ):"
        )

        if dna_sequence.lower() == "q":
            print("Exiting...")
            break

        #Let's convert the string to uppercase    
        dna_sequence = dna_sequence.upper()

        #Let's check the validity of the  DNA sequence
        valid_bases = set('ATCG')

        if not set(dna_sequence).issubset(valid_bases):
            print("Invalid sequence. Please try again.")
            continue
        #Let's convert the dna_sequence to rna_sequence
        rna_sequence = dna_sequence.replace('T','U')
        
        print(rna_sequence)
        

if __name__ == "__main__":
    conversion()






