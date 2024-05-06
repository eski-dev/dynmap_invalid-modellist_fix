import os

def process_logfile(source_file, target_dir, dry_run=False):

    mod_names_to_delete = {}

    with open(source_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if "models enabled" in line:
                mod_name = line.split("[Dynmap] ")[1].split(" models enabled")[0].split("[")[0]
                if mod_name not in mod_names_to_delete:
                    mod_names_to_delete[mod_name] = []
            elif "Invalid modellist patch for box" in line and mod_name in mod_names_to_delete:
                new_line_num_to_delete = int(line.split("at line ")[1].split()[0])
                if new_line_num_to_delete not in mod_names_to_delete[mod_name]:
                    mod_names_to_delete[mod_name].append(new_line_num_to_delete)

    for mod_name, line_numbers_to_delete in mod_names_to_delete.items():
        if line_numbers_to_delete:
            target_file = os.path.join(target_dir, f"{mod_name}-models.txt")
            if os.path.exists(target_file):
                if not dry_run:
                    delete_lines(target_file, line_numbers_to_delete)
                    print(f"Deleted lines {line_numbers_to_delete} from {target_file}")
                else:
                    print(f"Would delete lines {line_numbers_to_delete} from {target_file} in a real run")
            else:
                print(f"{target_file} does not exist")
    return mod_names_to_delete

def delete_lines(file_path, line_numbers):
    if file_path is None:
        raise ValueError("file_path is null")

    if line_numbers is None:
        raise ValueError("line_numbers is null")

    lines = []
    try:
        with open(file_path, 'r') as source:
            lines = source.readlines()
    except IOError as e:
        raise e

    lines_to_keep = [line for i, line in enumerate(lines) if i + 1 not in line_numbers]

    try:
        with open(file_path, 'w') as destination:
            destination.writelines(lines_to_keep)
    except IOError as e:
        raise e

if __name__ == "__main__":
    while True:
        source_file = input("Enter the path to the log file: ")
        if not os.path.isfile(source_file) or not source_file.endswith(".log"):
            print("Invalid log file path. Please enter a valid path to a log file.")
        else:
            break

    while True:
        target_dir = input("Enter the path to the target directory: ")
        if not os.path.isdir(target_dir):
            print("Invalid renderdata directory path. Please enter a valid path to the renderdata directory.")
        else:
            break

    dry_run = input("Do you want to perform a dry run? (y/n): ").lower() == "y"

    process_logfile(source_file, target_dir, dry_run)
