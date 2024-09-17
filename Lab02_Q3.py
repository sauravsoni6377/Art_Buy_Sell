
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='saurav11ax0', database='ArtBuySell')
cursor = conn.cursor()

# (a) 
query = """
SELECT a.Name, aw.Title
FROM Artist a
JOIN Artwork aw ON a.ArtistID = aw.ArtistID
WHERE YEAR(aw.ArtworkCreationDate) = 2023
GROUP BY a.ArtistID, aw.ArtworkID
HAVING COUNT(DISTINCT MONTH(aw.ArtworkCreationDate)) = 12;
"""

cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# (b) 
query = """
SELECT a.Name
FROM Artist a
JOIN Artwork aw ON a.ArtistID = aw.ArtistID
WHERE aw.ArtworkMedium = 'Sculpture'
AND YEAR(aw.ArtworkCreationDate) = 2023
GROUP BY a.ArtistID
HAVING COUNT(DISTINCT MONTH(aw.ArtworkCreationDate)) = 12;
"""

cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# (c) 
query = """
SELECT a.ArtistID, a.Name, a.Biography, a.Portfolio
FROM Artist a
LEFT JOIN Artwork aw ON a.ArtistID = aw.ArtistID
WHERE aw.ArtworkID IS NULL;
"""

cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# (d) 
query = """
SELECT DISTINCT u.UserID, u.Name, u.Email
FROM User u
JOIN `Order` o ON u.UserID = o.UserID
JOIN Artwork aw ON o.ArtworkID = aw.ArtworkID
WHERE aw.ArtworkMedium = 'Oil Painting' AND YEAR(o.PurchaseDate) = 2022
AND u.Role = 'Buyer';
"""

cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# (e) 
query = """
SELECT DISTINCT a.ArtistID, a.Name, a.Biography, a.Portfolio
FROM Artist a
JOIN Artwork aw ON a.ArtistID = aw.ArtistID
JOIN `Order` o ON aw.ArtworkID = o.ArtworkID
WHERE aw.ArtworkMedium = 'Oil Painting' AND YEAR(o.PurchaseDate) = 2022;
"""

cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# (f) 
query = """
SELECT u.UserID, u.Name, u.Email
FROM User u
LEFT JOIN `Order` o ON u.UserID = o.UserID
WHERE o.OrderID IS NULL
AND u.Role = 'Buyer';
"""

cursor.execute(query)
for row in cursor.fetchall():
    print(row)



conn.close()
