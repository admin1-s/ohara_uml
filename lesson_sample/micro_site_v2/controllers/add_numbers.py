from utils import parse_post, render_template
from app_logic import set_first_value, set_second_value, get_addition, get_first_value, get_second_value


def add_numbers(environ):
    method = environ["REQUEST_METHOD"]

    if method == "POST":
        data = parse_post(environ)
        first_value = data.get("first_value", ["0"])[0]
        second_value = data.get("second_value", ["0"])[0]

        set_first_value(first_value)
        set_second_value(second_value)
    else:
        # GET時はデフォルト値をセット
        first_value = "0"
        second_value = "0"
        set_first_value(first_value)
        set_second_value(second_value)

    addition = get_addition()
    first_value = get_first_value()
    second_value = get_second_value()

    return render_template(
        "boundaries/add_numbers_data.html",
        first_value=first_value,
        second_value=second_value,
        addition=addition
    )
