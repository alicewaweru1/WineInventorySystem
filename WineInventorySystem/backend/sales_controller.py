from database.db import connect_db

def record_sale(wine_id, quantity_sold):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT price, quantity FROM wines WHERE id = ?",
        (wine_id,)
    )
    wine = cursor.fetchone()
    
    if wine:
        price = wine[0]
        stock = wine[1]
        if stock >= quantity_sold:
            total = price * quantity_sold   
            cursor.execute("""
                INSERT INTO sales (wine_id, quantity_sold, total_price)
                VALUES (?, ?, ?)
            """, (wine_id, quantity_sold, total))
            cursor.execute("""
                UPDATE wines SET quantity = quantity - ? WHERE id = ?   
            """, (quantity_sold, wine_id))
            conn.commit()
    conn.close()
