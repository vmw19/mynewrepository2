from app.database import get_user


def output_formatter(results):
    out = []
    for results in results:
        result_dict = {
            "id": results[0],
            "first_name": results[1],
            "last_name": results[2],
            "hobbies": results[3],
            "active": results[4],
        }
        out.append(results_dict)
    return out

def insert(user_dict):
    ""