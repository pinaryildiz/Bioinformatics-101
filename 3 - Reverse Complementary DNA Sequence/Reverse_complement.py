

def complement():
    print("Reverse complementary sequence of DNA sequence in Python console")
    print("You can exit state 'q' at any time\n")


    while True:
        #Let's ask the user to enter a DNA sequence

        original_dna = input(
        "Enter a DNA sequence( A, T, C, G ):"
        )

        if original_dna.lower() == "q":
            print("Exiting...")
            break

        #Let's convert the string to uppercase    
        original_dna = original_dna.upper()

        #Let's check the validity of the  DNA sequence
        valid_bases = set('ATCG')

        if not set(original_dna).issubset(valid_bases):
            print("Invalid sequence. Please try again.")
            continue



        #Creating a translation table to match characters
        translation_table = str.maketrans('ATCG', 'TAGC')

        # Let's use the translate function to create a complementary array       
        complementary_dna = original_dna.translate(translation_table)

        print(complementary_dna)

        #Reverse the complementary sequence to create the reverse complementary sequence    
        reverse_complementary_dna = complementary_dna[::-1]     


        print(reverse_complementary_dna)


        # We show the result by adding the 5' and 3' ends
        print(f"Original DNA sequence: 5'-{original_dna}-3'")
        print(f"Complementary sequence: 3'-{complementary_dna}-5'")
        print(f"Reverse complementary sequence: 5'-{reverse_complementary_dna}-3'")


if __name__ == "__main__":
    complement()






