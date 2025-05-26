from modeller import Environ
from modeller.automodel import AutoModel, assess

# Set up environment
env = Environ()
env.io.atom_files_directory = [r"C:\Users\millicent\Downloads"]

def check_alignment_file(file_path):
    valid_seq_chars = set("ACDEFGHIKLMNPQRSTVWY-*")  # Modeller standard residues + gap/stop
    seqs = {}
    current_seq_name = None
    current_seq_lines = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.rstrip("\r\n")

            # Identify sequence headers (starting with > or name; Modeller .ali usually has >name)
            if line.startswith(">"):
                # Save previous sequence if any
                if current_seq_name is not None:
                    seqs[current_seq_name] = "".join(current_seq_lines).replace(" ", "")
                current_seq_name = line[1:].strip()  # sequence identifier after '>'
                current_seq_lines = []
            else:
                # Skip empty lines or lines that look like Modeller .ali control lines (structure, sequence, etc)
                if line.strip() == "" or line.lower().startswith("sequence") or line.lower().startswith("structure"):
                    continue
                # Collect sequence lines
                current_seq_lines.append(line.strip())

        # Save last sequence
        if current_seq_name is not None:
            seqs[current_seq_name] = "".join(current_seq_lines).replace(" ", "")

    # Now check each sequence for invalid residues
    invalid_found = False
    for seq_name, seq in seqs.items():
        for pos, res in enumerate(seq, 1):
            if res not in valid_seq_chars:
                print(f"Unknown residue '{res}' in sequence '{seq_name}', position {pos}")
                invalid_found = True

    return not invalid_found

def build_model(alnfile, model_name, pdb_code, chain_id="A"):
    a = AutoModel(env,
                  alnfile=alnfile,
                  knowns=pdb_code,
                  sequence=model_name,
                  assess_methods=(assess.DOPE, assess.GA341))
    a.starting_model = 1
    a.ending_model = 1
    a.make()

if __name__ == "__main__":
    alnfile = r"C:\Users\millicent\Downloads\gp173_modeling.ali"

    print("Checking alignment file for invalid characters...")
    if check_alignment_file(alnfile):
        print("No invalid characters found. Proceeding with modelling.")
        print("Building wildtype model...")
        build_model(alnfile, "wildtype", "AF-A0A2G6QUI9-F1-model_v4")

        print("Building mutant model...")
        build_model(alnfile, "mutant", "AF-A0A2G6QUI9-F1-model_v4")

        print("Modelling complete!")
    else:
        print("Invalid characters found in alignment file. Please fix them before running the modeller.")
