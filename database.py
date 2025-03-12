import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def initialize_database():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Insert basic languages
    cur.execute("""
        INSERT INTO languages (name, code)
        VALUES ('Minangkabau', 'min'), ('Indonesian', 'id')
        ON CONFLICT DO NOTHING
    """)
    
    # Insert common parts of speech
    cur.execute("""
        INSERT INTO parts_of_speech (pos_name, abbr)
        VALUES 
            ('Noun', 'n'),
            ('Verb', 'v'), 
            ('Adjective', 'adj'),
            ('Adverb', 'adv')
        ON CONFLICT DO NOTHING
    """)
    
    conn.commit()
    conn.close()