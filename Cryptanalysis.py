import string
from collections import Counter

# English letter frequency (approximate percentages)
ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_analysis(ciphertext):
    ciphertext = ciphertext.upper()
    letter_counts = Counter(char for char in ciphertext if char in string.ascii_uppercase)
    
    # Sort letters by frequency in descending order
    sorted_cipher_letters = [pair[0] for pair in letter_counts.most_common()]
    
    # Create a substitution map based on frequency mapping
    substitution_map = {}
    for i, letter in enumerate(sorted_cipher_letters):
        if i < len(ENGLISH_FREQ):
            substitution_map[letter] = ENGLISH_FREQ[i]
    
    return substitution_map

def decrypt_with_map(ciphertext, substitution_map):
    decrypted_text = ""
    for char in ciphertext:
        if char in substitution_map:
            decrypted_text += substitution_map[char]
        else:
            decrypted_text += char  # Keep spaces and punctuation unchanged
    return decrypted_text

# User input
encrypted_text = input("Enter the encrypted text: ").upper()

# Perform frequency analysis
sub_map = frequency_analysis(encrypted_text)

decrypted_text = decrypt_with_map(encrypted_text, sub_map)

print("\nSubstitution Map:")
for k, v in sub_map.items():
    print(f"{k} -> {v}")

print("\nMost Likely Decryption:")
print(decrypted_text)
