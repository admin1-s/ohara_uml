from app_logic import set_my_name, get_my_name
from utils import parse_post, render_template


def calc():
    name = get_my_name()
    

    return render_template("boundaries/name.html", name=name, name_display=name or "未設定")