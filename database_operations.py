from database import get_db_connection

def get_language_id(code):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM languages WHERE code = %s", (code,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None

def get_pos_id(abbr):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM parts_of_speech WHERE abbr = %s", (abbr,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None

def insert_word(entry):
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Get language and POS IDs
        minang_id = get_language_id('min')
        pos_id = get_pos_id(entry['pos_abbr'])
        
        # Insert word
        cur.execute("""
            INSERT INTO words (language_id, word, part_of_speech_id)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (minang_id, entry['headword'], pos_id))
        word_id = cur.fetchone()[0]
        
        # Insert definition
        cur.execute("""
            INSERT INTO definitions (word_id, definition, sense_number)
            VALUES (%s, %s, 1)
        """, (word_id, entry['definition']))
        
        # Insert example if exists
        if entry['example']:
            cur.execute("""
                INSERT INTO sentence_examples (word_id, example_sentence)
                VALUES (%s, %s)
                RETURNING id
            """, (word_id, entry['example']))
            example_id = cur.fetchone()[0]
            
            # Insert translation
            indonesian_id = get_language_id('id')
            cur.execute("""
                INSERT INTO sentence_example_translations 
                (example_id, language_id, translation)
                VALUES (%s, %s, %s)
            """, (example_id, indonesian_id, entry['translation']))
        
        conn.commit()
        print(f"Inserted: {entry['headword']}")
        
    except Exception as e:
        print(f"Error inserting {entry['headword']}: {str(e)}")
        conn.rollback()
    finally:
        conn.close()