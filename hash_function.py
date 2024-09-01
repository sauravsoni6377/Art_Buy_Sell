def generate_hash(input_string, table_size):
    # Common alphabets in the roll numbers
    common_alphabets = ['B', 'A', 'I']
    
    # Initialize the hash value
    hash_value = 0
    
    # Iterate over each character in the input string
    for char in input_string:
        if char.upper() in common_alphabets:
            # Add the ASCII value of the character to the hash value
            hash_value += ord(char)
    
    # Apply modulus to ensure the hash value is within the table size
    hash_value = hash_value % table_size
    
    return hash_value

# Example usage with ArtworkID or Title
artwork_id = "Sunset"  # Example input (could be ArtworkID or Title)
table_size = 100       # Example table size (can be adjusted based on your use case)

hash_value = generate_hash(artwork_id, table_size)
print(f"Hash value for '{artwork_id}' is: {hash_value}")
