# Sample data from the Artwork Listings table
artwork_listings = [
    {"ArtworkID": 1, "Title": "Sunset", "ArtistID": 1, "Price": 150.00},
    {"ArtworkID": 2, "Title": "Abstract Mind", "ArtistID": 2, "Price": 200.00},
    {"ArtworkID": 3, "Title": "Dreamscape", "ArtistID": 3, "Price": 300.00},
    {"ArtworkID": 4, "Title": "Urban Chaos", "ArtistID": 4, "Price": 250.00},
    {"ArtworkID": 5, "Title": "Portrait of a Lady", "ArtistID": 5, "Price": 350.00},
    {"ArtworkID": 6, "Title": "Ocean Waves", "ArtistID": 1, "Price": 180.00},
    {"ArtworkID": 7, "Title": "Color Burst", "ArtistID": 2, "Price": 220.00},
    {"ArtworkID": 8, "Title": "Midnight Dream", "ArtistID": 3, "Price": 320.00},
    {"ArtworkID": 9, "Title": "City Lights", "ArtistID": 4, "Price": 270.00},
    {"ArtworkID": 10, "Title": "Youth", "ArtistID": 5, "Price": 370.00}
]

# Function to create a secondary index on a specific key (e.g., Title)
def create_secondary_index(data, index_key):
    secondary_index = {}
    
    # Populate the index
    for record in data:
        key_value = record[index_key]
        if key_value in secondary_index:
            secondary_index[key_value].append(record)
        else:
            secondary_index[key_value] = [record]
    
    return secondary_index

# Create a secondary index on the 'Title' column
title_index = create_secondary_index(artwork_listings, 'Title')

# Display the secondary index
for title, artworks in title_index.items():
    print(f"Title: {title}")
    for artwork in artworks:
        print(f"  {artwork}")
