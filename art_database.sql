CREATE DATABASE ArtBuySell;

USE ArtBuySell;

CREATE TABLE Artist (
    ArtistID INT PRIMARY KEY,
    Name VARCHAR(100),
    Biography TEXT,
    Portfolio TEXT
);

CREATE TABLE Artwork (
    ArtworkID INT PRIMARY KEY,
    Title VARCHAR(100),
    Description TEXT,
    Image BLOB,
    Price DECIMAL(10, 2),
    Availability BOOLEAN,
    ArtistID INT,
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE User (
    UserID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(255),
    Role ENUM('Artist', 'Buyer')
);

CREATE TABLE `Order` (
    OrderID INT PRIMARY KEY,
    UserID INT,
    ArtworkID INT,
    Quantity INT,
    TotalPrice DECIMAL(10, 2),
    OrderDate DATETIME,
    Status ENUM('Pending', 'Completed', 'Cancelled'),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID)
);

CREATE TABLE Review (
    ReviewID INT PRIMARY KEY,
    UserID INT,
    ArtworkID INT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Comment TEXT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID)
);

INSERT INTO Artist (ArtistID, Name, Biography, Portfolio) VALUES 
(1, 'John Doe', 'A passionate painter from NYC.', 'https://portfolio.johndoe.com'),
(2, 'Alice Smith', 'An abstract artist exploring the human psyche.', 'https://portfolio.alicesmith.com'),
(3, 'Bob Brown', 'Surrealism artist who merges dreams with reality.', 'https://portfolio.bobbrown.com'),
(4, 'Cathy White', 'Modern art enthusiast who works with mixed media.', 'https://portfolio.cathywhite.com'),
(5, 'Eva Green', 'Portrait artist capturing the essence of personality.', 'https://portfolio.evangreen.com');

INSERT INTO Artwork (ArtworkID, Title, Description, Image, Price, Availability, ArtistID) VALUES 
(1, 'Sunset', 'A beautiful sunset over the mountains.', NULL, 150.00, TRUE, 1),
(2, 'Abstract Mind', 'A depiction of abstract thoughts and emotions.', NULL, 200.00, TRUE, 2),
(3, 'Dreamscape', 'A surreal landscape inspired by dreams.', NULL, 300.00, TRUE, 3),
(4, 'Urban Chaos', 'A modern art piece reflecting city life.', NULL, 250.00, TRUE, 4),
(5, 'Portrait of a Lady', 'A portrait capturing the essence of a mysterious woman.', NULL, 350.00, TRUE, 5),
(6, 'Ocean Waves', 'A calming representation of ocean waves.', NULL, 180.00, TRUE, 1),
(7, 'Color Burst', 'An abstract painting bursting with colors.', NULL, 220.00, TRUE, 2),
(8, 'Midnight Dream', 'A surreal representation of midnight thoughts.', NULL, 320.00, TRUE, 3),
(9, 'City Lights', 'A modern art piece capturing the lights of a city.', NULL, 270.00, TRUE, 4),
(10, 'Youth', 'A vibrant portrait of a young person full of life.', NULL, 370.00, TRUE, 5);

INSERT INTO User (UserID, Name, Email, Password, Role) VALUES 
(1, 'Jane Doe', 'jane.doe@example.com', 'hashedpassword1', 'Buyer'),
(2, 'Michael Johnson', 'michael.johnson@example.com', 'hashedpassword2', 'Buyer'),
(3, 'Emily Davis', 'emily.davis@example.com', 'hashedpassword3', 'Artist'),
(4, 'David Wilson', 'david.wilson@example.com', 'hashedpassword4', 'Artist'),
(5, 'Sarah Miller', 'sarah.miller@example.com', 'hashedpassword5', 'Buyer');

INSERT INTO `Order` (OrderID, UserID, ArtworkID, Quantity, TotalPrice, OrderDate, Status) VALUES 
(1, 1, 1, 1, 150.00, '2024-08-31 12:30:00', 'Completed'),
(2, 2, 2, 2, 400.00, '2024-08-29 10:15:00', 'Pending'),
(3, 3, 3, 1, 300.00, '2024-08-28 14:00:00', 'Completed'),
(4, 4, 4, 1, 250.00, '2024-08-30 09:45:00', 'Cancelled'),
(5, 5, 5, 1, 350.00, '2024-08-27 16:30:00', 'Completed');

INSERT INTO Review (ReviewID, UserID, ArtworkID, Rating, Comment) VALUES 
(1, 1, 1, 5, 'Stunning depiction of nature. Loved it!'),
(2, 2, 2, 4, 'Very abstract and thought-provoking.'),
(3, 3, 3, 5, 'Amazing work, truly captures the essence of dreams.'),
(4, 4, 4, 3, 'Interesting piece but not quite what I expected.'),
(5, 5, 5, 5, 'Beautiful portrait, very lifelike and detailed.');


#select *from artist;
