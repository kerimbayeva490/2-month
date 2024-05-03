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