def calculator():
    print("Python console calculating number of nucleotides")
    print("You can exit by typing 'q' at any time\n")

    while True:
        # Let's ask the user to enter a DNA sequence
        operation = input("Enter a DNA sequence (A, T, C, G): ")

        if operation.lower() == 'q':
            print("Exiting...")
            break

        # Let's convert the string to uppercase
        operation = operation.upper()

        # Let's check the validity of the DNA sequence
        valid_bases = set('ATCG')
        if not set(operation).issubset(valid_bases):
            print("Invalid sequence. Please try again.")
            continue

        # Let's count the nucleotides
        a_count = operation.count('A')
        t_count = operation.count('T')
        c_count = operation.count('C')
        g_count = operation.count('G')

        # Let's print the numbers on the screen
        print(f"A count: {a_count}")
        print(f"T count: {t_count}")
        print(f"C count: {c_count}")
        print(f"G count: {g_count}\n")

if __name__ == "__main__":
    calculator()