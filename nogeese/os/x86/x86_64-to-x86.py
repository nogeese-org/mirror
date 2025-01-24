import subprocess

def disassemble_x86_64(binary_file):
    try:
        # Run objdump to disassemble the binary in x86-64
        result = subprocess.run(['objdump', '-d', binary_file], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error: {e}")
        return None

def convert_to_x86(assembly_code):
    # Here you should implement the conversion logic to change 64-bit specific code
    # to 32-bit. This is a complex task that requires manually adjusting the code
    # (register names, instructions, system calls, etc.).
    # For now, we'll just print the assembly code for review.
    
    # For simplicity, let's assume we replace certain instructions as a placeholder.
    assembly_code = assembly_code.replace('rax', 'eax')  # Example: replace 64-bit register with 32-bit
    assembly_code = assembly_code.replace('rdx', 'edx')  # Same for other registers.
    
    return assembly_code

def save_to_file(assembly_code, output_file):
    try:
        with open(output_file, 'w') as f:
            f.write(assembly_code)
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    binary_file = input("Enter the path to the x86-64 binary: ")
    assembly_code = disassemble_x86_64(binary_file)
    
    if assembly_code:
        print("Disassembled Code:")
        print(assembly_code)
        
        converted_code = convert_to_x86(assembly_code)
        
        output_file = input("Enter output file name for 32-bit assembly: ")
        save_to_file(converted_code, output_file)
        print(f"Converted assembly saved to {output_file}")
