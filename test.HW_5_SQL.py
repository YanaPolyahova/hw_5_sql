import psycopg2

# conn = psycopg2.connect(database='netology_db', user='postgres', password='1705Ars@')
# with conn.cursor() as cur:
#    cur.execute("""
#         DROP TABLE telephone;
#         DROP TABLE client;
#         """)
#    conn.commit()
#
# def create_db(conn):
#     conn = psycopg2.connect(database='netology_db', user='postgres', password='1705Ars@')
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS client(
#             client_id SERIAL PRIMARY KEY,
#             first_name VARCHAR(40),
#             last_name VARCHAR(40),
#             email VARCHAR(40)
#             );
#             """)
#         conn.commit()
#
#
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS telephone(
#             id SERIAL PRIMARY KEY,
#             number INTEGER,
#             c_id INTEGER NOT NULL REFERENCES client(client_id)
#             );
#             """)
#         conn.commit()



# def add_client(conn, first_name, last_name, email, phones=None):
#     conn = psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@")
#     with conn.cursor() as cur:
#         cur.execute('''
#             INSERT INTO client(first_name, last_name, email)
#             VALUES(%s, %s, %s);
#             ''', ("Ivan", "Ivanov",  "ivanovany@mail.ru"))
#         conn.commit()



# def add_phone(conn, client_id, phone):
#     conn = psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@")
#     with conn.cursor() as cur:
#         cur.execute('''
#             INSERT INTO telephone(c_id, number)
#             VALUES(%s, %s);
#             ''', (1, 123456789))
#         conn.commit()


# def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
#     conn = psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@")
#     with conn.cursor() as cur:
#         cur.execute('''
#             UPDATE client
#             SET first_name=%s, last_name=%s, email=%s
#             WHERE client_id=%s;
#             ''', ("Petr", "Petrov", "petrov@mail.ru", 3))
#         conn.commit()


# def delete_phone(conn, client_id, number):
#     conn = psycopg2.connect(database='netology_db', user='postgres', password='1705Ars@')
#     with conn.cursor() as cur:
#         phone_for_del = ({'client_id': client_id, 'number': number})
#         cur.execute('''
#             DELETE FROM telephone
#             WHERE number = %(number)s;
#             ''', phone_for_del)
#         conn.commit()


# def delete_client(conn, client_id):
#     conn = psycopg2.connect(database='netology_db', user='postgres', password='1705Ars@')
#     with conn.cursor() as cur:
#         client_for_del = ({"client_id": client_id})
#         cur.execute('''
#             DELETE FROM telephone
#             WHERE c_id = %(client_id)s;
#             ''', client_for_del)
#         cur.execute('''
#             DELETE FROM client
#             WHERE client_id = %(client_id)s;
#             ''', client_for_del)
#         conn.commit()



def find_client(conn, **values):
    conn = psycopg2.connect(database='netology_db', user='postgres', password='1705Ars@')
    with conn.cursor() as cur:
        for key, value in values.items():
            cur.execute(f'''
                SELECT client_id, first_name, last_name, email, phone
                FROM client INNER JOIN telephone USING(client_id)
                WHERE {key} = '{value}'
            ''')
            resalt = cur.fetcholl()
            if resalt:
                print(resalt)
        print('client not found')

# create_db(psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@"))
# add_client(psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@"), "Ivan", "Ivanov",  "ivanovany@mail.ru")
# add_phone(psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@"), 1, 123456789)
# change_client(psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@"), "Petr", "Petrov", "petrov@mail.ru", 3)
#delete_phone(psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@"), 1, 123456789)
# delete_client(psycopg2.connect(database="netology_db", user="postgres", password="1705Ars@"), 2)
#find_client('Ivanov')
