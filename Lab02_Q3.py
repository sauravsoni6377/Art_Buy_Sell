import mysql.connector
import time

conn = mysql.connector.connect(host='localhost', user='root', password='saurav11ax0', database='ArtBuySell')
cursor = conn.cursor()

def execute_query(query):
    start_time = time.time()
    cursor.execute(query)
    results = cursor.fetchall()
    end_time = time.time()

    for row in results:
        print(row)

    print(f"Query execution time: {end_time - start_time} seconds")

# Query 1: Extract a list of all <artist_name, artwork> who have artwork listings in all months in 2023
print("Query 1: Artists with artwork listings in all months of 2023")
query1 = """
SELECT a.Name, aw.Title
FROM Artist a
JOIN Artwork aw ON a.ArtistID = aw.ArtistID
WHERE YEAR(aw.ArtworkCreationDate) = 2023
GROUP BY a.ArtistID, aw.ArtworkID
HAVING COUNT(DISTINCT MONTH(aw.ArtworkCreationDate)) = 12;
"""
execute_query(query1)

# Query 2: From the above list, print the names of all artists who have at least one sculpture
print("\nQuery 2: Artists with at least one sculpture in 2023")
query2 = """
SELECT a.Name
FROM Artist a
JOIN Artwork aw ON a.ArtistID = aw.ArtistID
WHERE aw.ArtworkMedium = 'Sculpture'
AND YEAR(aw.ArtworkCreationDate) = 2023
GROUP BY a.ArtistID
HAVING COUNT(DISTINCT MONTH(aw.ArtworkCreationDate)) = 12;
"""
execute_query(query2)

# Query 3: Extract a list of all <artist_profile> information for whom the database does not have any artwork listing
print("\nQuery 3: Artists without any artwork listings")
query3 = """
SELECT a.ArtistID, a.Name, a.Biography, a.Portfolio
FROM Artist a
LEFT JOIN Artwork aw ON a.ArtistID = aw.ArtistID
WHERE aw.ArtworkID IS NULL;
"""
execute_query(query3)

# Query 4: Print a list of all buyers who have made purchases of oil paintings in 2022
print("\nQuery 4: Buyers who purchased oil paintings in 2022")
query4 = """
SELECT DISTINCT u.UserID, u.Name, u.Email
FROM User u
JOIN `Order` o ON u.UserID = o.UserID
JOIN Artwork aw ON o.ArtworkID = aw.ArtworkID
WHERE aw.ArtworkMedium = 'Oil Painting' AND YEAR(o.OrderDate) = 2022
AND u.Role = 'Buyer';
"""
execute_query(query4)

# Query 5: From the above list, derive a list of the artists and their profile information
print("\nQuery 5: Artists who created oil paintings purchased in 2022")
query5 = """
SELECT DISTINCT a.ArtistID, a.Name, a.Biography, a.Portfolio
FROM Artist a
JOIN Artwork aw ON a.ArtistID = aw.ArtistID
JOIN `Order` o ON aw.ArtworkID = o.ArtworkID
WHERE aw.ArtworkMedium = 'Oil Painting' AND YEAR(o.OrderDate) = 2022;
"""
execute_query(query5)

# Query 6: Derive a list of all <buyer_profiles> who have not made any purchases
print("\nQuery 6: Buyers who have not made any purchases")
query6 = """
SELECT u.UserID, u.Name, u.Email
FROM User u
LEFT JOIN `Order` o ON u.UserID = o.UserID
WHERE o.OrderID IS NULL
AND u.Role = 'Buyer';
"""
execute_query(query6)

conn.close()
