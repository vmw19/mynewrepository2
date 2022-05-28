from app.database import get_user


def output_formatter(results):
    out = []
    for results in results:
        result_dict = {
            "id": results[0],
            
        }