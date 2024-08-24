import os
import pyperclip
import subprocess
import argparse

CONFIG_FILE = os.path.expanduser("~/.copyclipboard_config")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Copy repository structure and file contents to clipboard.")
    parser.add_argument('--extensions', nargs='+', help="File extensions to include (e.g., .py .yaml)")
    return parser.parse_args()

def update_config_file(extensions):
    # Write the extensions to the configuration file
    with open(CONFIG_FILE, 'w') as config:
        for ext in extensions:
            config.write(f"{ext}\n")
    print(f"Configuration updated with extensions: {', '.join(extensions)}")

def get_allowed_extensions():
    # Default to None, meaning all file types are allowed if the config file doesn't exist
    allowed_extensions = None
    
    # Read the config file if it exists
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config:
            extensions = {line.strip() for line in config if line.strip()}
            if extensions:
                allowed_extensions = extensions
    
    return allowed_extensions

def get_folder_structure_with_contents(root_dir, allowed_extensions):
    output = []
    
    # Get the folder structure using the 'tree' command
    try:
        tree_output = subprocess.run(['tree', root_dir], text=True, capture_output=True)
        folder_structure = tree_output.stdout
    except Exception as e:
        folder_structure = f"Error running tree command: {e}"
    
    # Prepend the folder structure to the output
    output.append("Here is the folder structure:\n")
    output.append(folder_structure)
    output.append("\n")
    
    # Walk through the directory to get file contents
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude hidden directories like .git
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        for filename in filenames:
            # Skip hidden files, but allow all file types if allowed_extensions is None
            if filename.startswith('.') or (allowed_extensions and not any(filename.endswith(ext) for ext in allowed_extensions)):
                continue
            
            file_path = os.path.join(dirpath, filename)
            relative_file_path = os.path.relpath(file_path, root_dir)
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
            except Exception as e:
                content = f"Error reading file: {e}"
            
            # Format the content with triple quotes and two new lines after the closing quotes
            output.append(f"{relative_file_path}:\n\"\"\"\n{content}\n\"\"\"\n\n")
    
    return "\n".join(output)

def main():
    # Parse command-line arguments
    args = parse_arguments()
    
    if args.extensions:
        # If extensions are provided, update the configuration file
        update_config_file(args.extensions)
        allowed_extensions = set(args.extensions)
    else:
        # Otherwise, read from the configuration file
        allowed_extensions = get_allowed_extensions()
    
    # Specify the root directory of your repository (can be current working directory)
    root_dir = os.getcwd()
    
    # Get the folder structure and contents
    output = get_folder_structure_with_contents(root_dir, allowed_extensions)
    
    # Copy to clipboard
    pyperclip.copy(output)
    if allowed_extensions:
        print(f"Repository structure and contents copied to clipboard for file types: {', '.join(allowed_extensions)}")
    else:
        print("Repository structure and contents copied to clipboard for all file types.")

if __name__ == "__main__":
    main()
