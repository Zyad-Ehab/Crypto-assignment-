import itertools
import string

def decrypt(ciphertext, key_map):
    decrypted_text = ""
    for char in ciphertext:
        if char in key_map:
            decrypted_text += key_map[char]
        else:
            decrypted_text += char  # Keep spaces and punctuation unchanged
    return decrypted_text

def brute_force_monoalphabetic(ciphertext):
    alphabet = string.ascii_uppercase
    all_permutations = itertools.permutations(alphabet)  # Generate all possible key mappings
    
    count = 0
    for perm in all_permutations:
        key_map = {cipher: plain for cipher, plain in zip(alphabet, perm)}
        decrypted_text = decrypt(ciphertext, key_map)
        print(f"Attempt {count + 1}: {decrypted_text}")
        count += 1
        
        if count >= 1000:  # Limit the output to 1000 attempts for practicality
            print("Stopping after 1000 attempts to avoid excessive output.")
            break

# Example encrypted text (Assuming uppercase letters only)
ciphertext = input("Enter the encrypted message: ").upper()
brute_force_monoalphabetic(ciphertext)
