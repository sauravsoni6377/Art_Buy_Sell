import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ArtBuySell"
)
cursor = conn.cursor()

# Insert dummy data into Artist table
cursor.execute("INSERT INTO Artist (ArtistID, Name, Biography, Portfolio) VALUES (7, 'New Artist', 'Another passionate painter', 'https://portfolio.newartist.com')")

# Insert dummy data into Artwork table with unique ArtworkID
cursor.execute("INSERT INTO Artwork (ArtworkID, Title, Description, Image, Price, Availability, ArtistID) VALUES (12, 'Sunset Over Sea', 'A beautiful sunset painting over the sea', NULL, 150.00, TRUE, 7)")

# Insert dummy data into User table with a unique UserID
cursor.execute("INSERT INTO User (UserID, Name, Email, Password, Role) VALUES (7, 'John Smith', 'john.smith@example.com', 'hashedpassword7', 'Buyer')")

# Insert dummy data into Order table with a unique OrderID
cursor.execute("INSERT INTO `Order` (OrderID, UserID, ArtworkID, Quantity, TotalPrice, OrderDate, Status) VALUES (7, 7, 12, 1, 150.00, '2024-08-31 12:30:00', 'Completed')")

# Insert dummy data into Review table with a unique ReviewID
cursor.execute("INSERT INTO Review (ReviewID, UserID, ArtworkID, Rating, Comment) VALUES (7, 7, 12, 5, 'Amazing piece of art by the new artist')")

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()
