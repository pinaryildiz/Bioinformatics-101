def calculating_GC_content_of_DNA_sequence():
    print("Calculating GC content of DNA sequence in Python console")
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


        

        #The count() function is used to calculate the occurrences of each base.
        g_count = dna_sequence.count('G')
        c_count = dna_sequence.count('C')

        #These lines print the count of 'G' and 'C' bases in the DNA sequence to the screen.
        print(f"G base count: {g_count}")
        print(f"C base count: {c_count}")

        # Total GC content
        gc_content = g_count + c_count
        print(f"Total GC content: {gc_content}")




        # Total length of the DNA sequence
        total_length = len(dna_sequence)

        # Calculate the GC content percentage
        gc_percentage = (gc_content / total_length) * 100

        #  Print the results
        print(f"GC content: %{gc_percentage:.2f}")



if __name__ == "__main__":
    calculating_GC_content_of_DNA_sequence()




















   


