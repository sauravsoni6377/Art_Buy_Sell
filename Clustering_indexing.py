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
# Function to apply clustering indexing based on a specific key (e.g., ArtistID)
def apply_clustering_index(data, index_key):
    # Sort the data based on the specified index key
    clustered_data = sorted(data, key=lambda x: x[index_key])
    return clustered_data

# Apply clustering indexing on 'ArtistID'
clustered_artwork_listings = apply_clustering_index(artwork_listings, 'ArtistID')

# Display the clustered data
for artwork in clustered_artwork_listings:
    print(artwork)
