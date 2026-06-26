from database.db import connect_db


def record_sale(wine_id, quantity_sold):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT price, quantity FROM wines WHERE id = ?",
        (wine_id,),
    )

    wine = cursor.fetchone()

    if wine:
        price = wine[0]
        stock = wine[1]

        if stock >= quantity_sold:
            total = price * quantity_sold

            cursor.execute(
                """
                INSERT INTO sales (
                    wine_id,
                    quantity_sold,
                    total_price
                )
                VALUES (?, ?, ?)
                """,
                (wine_id, quantity_sold, total),
            )

            cursor.execute(
                """
                UPDATE wines
                SET quantity = quantity - ?
                WHERE id = ?
                """,
                (quantity_sold, wine_id),
            )

            conn.commit()

    conn.close()


def get_total_sales():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM sales")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_revenue():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(total_price) FROM sales")

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0


def get_sales_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT sale_date, total_price
        FROM sales
        ORDER BY sale_date
        """
    )

    sales = cursor.fetchall()

    conn.close()

    return sales