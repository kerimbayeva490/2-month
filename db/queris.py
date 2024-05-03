class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone_number INTEGER,
            time_of_visit TEXT,
            rate_of_food TEXT,
            rate_of_cleaning,
            additional_review
        )
    """

    CREATE_TYPES_TABLE = """
        CREATE TABLE IF NOT EXISTS types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
    CREATE_MEALS_TABLE = """
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            picture TEXT,
            type_id INTEGER,
            FOREIGN KEY (type_id) REFERENCES types(id)
        )
    """
    DROP_TYPES_TABLE = "DROP TABLE IF EXISTS types"
    DROP_MEALS_TABLE = "DROP TABLE IF EXISTS meals"
    POPULATE_TYPES = """
        INSERT INTO types (id, name) VALUES (1, 'супы'),
        (2, 'пиццы'), (3, 'роллы')
    """
    POPULATE_MEALS = """
        INSERT INTO meals (name, price, picture, type_id) VALUES ('Пицца 30см', 1000, 'images/pizza30cm.jpeg', 2),
        ('Пицца 40см', 2000, 'images/pizza40cm.jpeg', 2),
        ('Том Ям', 700, 'images/tomyam.jpeg', 1),
        ('Гороховый', 750, 'images/gorohovyi.jpeg', 1),
        ('Филадельфия', 3000, 'images/philadelphi.jpeg', 3),
        ('Массиро', 4000, 'images/massiro.jpeg', 3)
    """