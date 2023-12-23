from Bio import SeqIO

def read_ids(id_file):
    """
    Read a list of IDs from a file.

    :param id_file: Path to the file containing IDs.
    :return: A set of IDs.
    """
    with open(id_file, 'r') as file:
        ids = {line.strip() for line in file}
    return ids

def filter_fasta(fasta_file, id_list, output_file):
    # Read the FASTA file and filter sequences
    selected_sequences = (record for record in SeqIO.parse(fasta_file, "fasta") if record.id in id_list)

    # Write the filtered sequences to a new file
    SeqIO.write(selected_sequences, output_file, "fasta")

if __name__ == "__main__":
    # Example usage
    fasta_file = "path/to/your/input.fasta"  # Replace with your FASTA file path
    id_file = "path/to/your/id_list.txt"  # Replace with your ID list file path
    output_file = "./output.fasta"  # Replace with your desired output file path

    id_list = read_ids(id_file)
    filter_fasta(fasta_file, id_list, output_file)