#include <mysql/mysql.h>
#include <stdio.h>

void execute_query(MYSQL *conn, const char *query) {
    MYSQL_RES *res;
    MYSQL_ROW row;
   
    if (mysql_query(conn, query)) {
        printf("Query failed: %s\n", mysql_error(conn));
        return;
    }

    // Store the result of the query
    res = mysql_store_result(conn);

    // Print the result of the query
    int num_fields = mysql_num_fields(res);
    while ((row = mysql_fetch_row(res)) != NULL) {
        for (int i = 0; i < num_fields; i++) {
            printf("%s\t", row[i] ? row[i] : "NULL");
        }
        printf("\n");
    }

    // Free the result memory
    mysql_free_result(res);
}

int main() {
    MYSQL *conn;
    conn = mysql_init(NULL);

    // Connect to database
    if (mysql_real_connect(conn, "localhost", "root", "password", "ArtBuySell", 0, NULL, 0) == NULL) {
        printf("Connection failed: %s\n", mysql_error(conn));
        mysql_close(conn);
        return 1;
    }

    // 1. Extract a list of all <artist_name, artwork> who have artwork listings in all months in 2023
    printf("Query 1: Artists with artwork listings in all months of 2023\n");
    const char *query1 =
        "SELECT a.Name, aw.Title "
        "FROM Artist a "
        "JOIN Artwork aw ON a.ArtistID = aw.ArtistID "
        "WHERE YEAR(aw.ArtworkCreationDate) = 2023 "
        "GROUP BY a.ArtistID, aw.ArtworkID "
        "HAVING COUNT(DISTINCT MONTH(aw.ArtworkCreationDate)) = 12;";
    execute_query(conn, query1);

    // 2. From the above list, print the names of all artists who have at least one sculpture
    printf("\nQuery 2: Artists with at least one sculpture in 2023\n");
    const char *query2 =
        "SELECT a.Name "
        "FROM Artist a "
        "JOIN Artwork aw ON a.ArtistID = aw.ArtistID "
        "WHERE aw.ArtworkMedium = 'Sculpture' "
        "AND YEAR(aw.ArtworkCreationDate) = 2023 "
        "GROUP BY a.ArtistID "
        "HAVING COUNT(DISTINCT MONTH(aw.ArtworkCreationDate)) = 12;";
    execute_query(conn, query2);

    // 3. Extract a list of all <artist_profile> information for whom the database does not have any artwork listing
    printf("\nQuery 3: Artists without any artwork listings\n");
    const char *query3 =
        "SELECT a.ArtistID, a.Name, a.Biography, a.Portfolio "
        "FROM Artist a "
        "LEFT JOIN Artwork aw ON a.ArtistID = aw.ArtistID "
        "WHERE aw.ArtworkID IS NULL;";
    execute_query(conn, query3);

    // 4. Print a list of all buyers who have made purchases of oil paintings in 2022
    printf("\nQuery 4: Buyers who purchased oil paintings in 2022\n");
    const char *query4 =
        "SELECT DISTINCT u.UserID, u.Name, u.Email "
        "FROM User u "
        "JOIN `Order` o ON u.UserID = o.UserID "
        "JOIN Artwork aw ON o.ArtworkID = aw.ArtworkID "
        "WHERE aw.ArtworkMedium = 'Oil Painting' AND YEAR(o.PurchaseDate) = 2022 "
        "AND u.Role = 'Buyer';";
    execute_query(conn, query4);

    // 5. From the above list, derive a list of the artists and their profile information
    printf("\nQuery 5: Artists who created oil paintings purchased in 2022\n");
    const char *query5 =
        "SELECT DISTINCT a.ArtistID, a.Name, a.Biography, a.Portfolio "
        "FROM Artist a "
        "JOIN Artwork aw ON a.ArtistID = aw.ArtistID "
        "JOIN `Order` o ON aw.ArtworkID = o.ArtworkID "
        "WHERE aw.ArtworkMedium = 'Oil Painting' AND YEAR(o.PurchaseDate) = 2022;";
    execute_query(conn, query5);

    // 6. Derive a list of all <buyer_profiles> who have not made any purchases
    printf("\nQuery 6: Buyers who have not made any purchases\n");
    const char *query6 =
        "SELECT u.UserID, u.Name, u.Email "
        "FROM User u "
        "LEFT JOIN `Order` o ON u.UserID = o.UserID "
        "WHERE o.OrderID IS NULL "
        "AND u.Role = 'Buyer';";
    execute_query(conn, query6);

    // Close the connection to the database
    mysql_close(conn);
    return 0;
}
