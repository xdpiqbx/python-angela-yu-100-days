def error_not_found(location):
    return {
        "Not found": f"Sorry, we don't have a cafe at location - {location}"
    }


def added_new_cafe():
    return {
        "Success": "Successfully added the new cafe."
    }


def updated_price():
    return {
        "Success": "Successfully updated price"
    }


def wrong_api_key():
    return "That's not allowed. Incorrect API key"


def cafe_not_found_by_id(cafe_id):
    return f"Cafe with id: {cafe_id} was not found in the database"


def cafe_successfully_removed(cafe_name):
    return f"Cafe '{cafe_name}' successfully removed from the database"
