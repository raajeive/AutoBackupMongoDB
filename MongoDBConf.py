USERNAME = "raajeivemsk@gmail.com"

PASSWORD = "raajeivemsk@gmail.com"

COMMIT_MESSAGE = "\"New commit\""

EXPORT_DB_COLLECTION = [
    {
        "db": "production",
        "collection": "devices",
        "file_name": "devices"
    },
    {
        "db": "production",
        "collection": "users",
        "file_name": "users"
    },
    {
        "db": "production",
        "collection": "reservations",
        "file_name": "reservations"
    },
    {
        "db": "production",
        "collection": "equipments",
        "file_name": "equipments"
    }
]

IMPORT_DB_COLLECTION = [
    {
        "db": "development",
        "collection": "devices",
        "file_name": "devices"
    },
    {
        "db": "development",
        "collection": "users",
        "file_name": "users"
    },
    {
        "db": "development",
        "collection": "reservations",
        "file_name": "reservations"
    },
    {
        "db": "development",
        "collection": "equipments",
        "file_name": "equipments"
    }
]
