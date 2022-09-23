import psycopg2
conn = psycopg2.connect(database='netology_db', user='postgres', password='1705Ars@')

def create_db(conn):
     with conn.cursor() as cur:
         cur.execute("""
             CREATE TABLE IF NOT EXISTS client(
             client_id SERIAL PRIMARY KEY,
             first_name VARCHAR(40),
             last_name VARCHAR(40),
             email VARCHAR(40)
             );
             """)
         conn.commit()


         cur.execute("""
             CREATE TABLE IF NOT EXISTS telephone(
             id SERIAL PRIMARY KEY,
             number INTEGER,
             c_id INTEGER NOT NULL REFERENCES client(client_id)
             );
             """)
         conn.commit()



def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute('''
            INSERT INTO client(first_name, last_name, email)
            VALUES(%s, %s, %s);
            ''', ("Zlata", "Sahar",  "Sahar@mail.ru"))
        conn.commit()



def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
         cur.execute('''
             INSERT INTO telephone(c_id, number)
             VALUES(%s, %s);
             ''', (1, 123456777))
         conn.commit()


def change_client(conn, client_id, first_name=None, last_name=None, email=None, old_phone=None, new_phone=None):
    with conn.cursor() as cur:
        if first_name:
            cur.execute('''UPDATE client SET first_name=%s WHERE client_id =%s;''',
                        (first_name, str(client_id)))
        elif last_name:
            cur.execute('''UPDATE client SET second_name=%s WHERE client_id =%s;''',
                        (last_name, str(client_id)))
        elif email:
            cur.execute('''UPDATE customer_list SET e_mail=%s WHERE id =%s;''',
                        (email, str(client_id)))
        elif old_phone:
            cur.execute('''UPDATE customer_phone Set phone_number=%s WHERE phone_number=%s;''', (new_phone, old_phone))
        elif old_phone is None:
            old_phone = input('Какой номер телефона нужно заменить?: ')
            cur.execute('''UPDATE client_id Set number=%s WHERE number=%s;''', (new_phone, old_phone))
        conn.commit()


def delete_phone(conn, client_id, number):
     with conn.cursor() as cur:
         phone_for_del = ({'client_id': client_id, 'number': number})
         cur.execute('''
             DELETE FROM telephone
             WHERE number = %(number)s;
             ''', phone_for_del)
         conn.commit()


def delete_client(conn, client_id):
     with conn.cursor() as cur:
         client_for_del = ({"client_id": client_id})
         cur.execute('''
             DELETE FROM telephone
             WHERE c_id = %(client_id)s;
             ''', client_for_del)
         cur.execute('''
             DELETE FROM client
             WHERE client_id = %(client_id)s;
             ''', client_for_del)
         conn.commit()



def find_client(conn, **values):
    conn = psycopg2.connect(database='netology_db', user='postgres', password='1705Ars@')
    with conn.cursor() as cur:
        for key, value in values.items():
            cur.execute(f'''
            SELECT client_id, first_name, last_name, email, phone
            FROM client INNER JOIN telephone USING(client_id)
            WHERE {key} = '{value}'
            ''')
            result = cur.fetcholl()
            if result:
                return result
            print('client not found')


if __name__ == "__main__":
    with psycopg2.connect(database='netology_db', user='postgres', password='1705Ars@') as conn:
        create_db(conn)
        add_client(conn, "Zlata", "Sahar",  "Sahar@mail.ru")
        add_phone(conn, 1, 123456789)
        change_client(conn, 1, first_name='Petr', last_name='Ivanov', email='ivanovany@mail.ru')
        delete_phone(conn, 1, 123456777)
        delete_client(conn, 2)
        find_client('Ivanov')

conn.close()
