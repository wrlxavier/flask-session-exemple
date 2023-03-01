import sqlite3


def get_user_items(email):
    connection = sqlite3.connect('./data/database.db')
    cursor = connection.cursor()
    response = cursor.execute(
        f"""
            SELECT 
                items.id, items.item_name, users.id 
            FROM 
                items
                INNER JOIN users ON users.id = items.user_id
            WHERE 
                users.email  = "{email}"
        """
    )
    sql_data = response.fetchall()
    cursor.close()
    connection.close()
    return sql_data


def is_registered(email, password):
    connection = sqlite3.connect('./data/database.db')
    cursor = connection.cursor()
    response = cursor.execute(
        f"""
            SELECT 
                users.email as "email",
                users.password as "password"
            FROM 
                users
            WHERE 
                users.email = '{email}'
            AND 
                users.password = '{password}'
        """
    )
    sql_data = response.fetchall()
    cursor.close()
    connection.close()
    return sql_data
