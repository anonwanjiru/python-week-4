import random
import string

def modify_content(text):
    """Modify the file content. This example converts all text to uppercase."""
    return text.upper()

def generate_random_filename(prefix="modified_", extension=".txt", length=8):
    """Generate a random filename."""
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{prefix}{random_str}{extension}"

def main():
    # Ask the user for input filename
    input_filename = input("📁 Enter the filename to read: ").strip()

    try:
        # Try to open and read the file
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
            print("✅ File read successfully.")
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
        return
    except IOError:
        print(f"❌ Error: Could not read the file '{input_filename}'.")
        return

    # Modify the content
    modified_content = modify_content(content)

    # Generate a random output filename
    output_filename = generate_random_filename()

    try:
        # Try to write to a new file
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
            print(f"🎉 Success! Modified content saved to: '{output_filename}'")
    except IOError:
        print(f"❌ Error: Could not write to file '{output_filename}'.")

if __name__ == "__main__":
    main()
