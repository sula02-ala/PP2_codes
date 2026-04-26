import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "snake_db",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": "5432"
}

def get_conn():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except:
        return None

def init_db():
    conn = get_conn()
    if not conn:
        return
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game_sessions (
        id SERIAL PRIMARY KEY,
        player_id INTEGER REFERENCES players(id),
        score INTEGER NOT NULL,
        level_reached INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT NOW()
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_or_create_player(username):
    conn = get_conn()
    if not conn:
        return None

    cur = conn.cursor()
    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    row = cur.fetchone()

    if row:
        pid = row[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        pid = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return pid

def save_score_db(username, score, level):
    conn = get_conn()
    if not conn:
        return False

    pid = get_or_create_player(username)
    if not pid:
        return False

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO game_sessions(player_id, score, level_reached)
        VALUES(%s, %s, %s)
    """, (pid, score, level))

    conn.commit()
    cur.close()
    conn.close()
    return True

def get_top_scores_db():
    conn = get_conn()
    if not conn:
        return []

    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON p.id = g.player_id
        ORDER BY g.score DESC
        LIMIT 10
    """)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows