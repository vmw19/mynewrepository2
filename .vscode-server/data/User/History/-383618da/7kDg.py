from app.database import get_user


def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "hobbies": result[3],
            "active": result[4],
        }
        out.append(result_dict)
    return out

def insert(user_dict):
    ""This function creates a user in our user table.""
    value_tuple = (
        user_dict.get("first_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies"),
    )
    statement = ""
    INSERT INTO user (
        first_name,
        last_name,
        hobbies,
    ) VALUES (?, ?, ?)
""
cursor = get_db()
cursor.execute(statement, value_tuple)
cursor.commit()
cursor.close()
