import os

import allure

environment = os.environ.get("environment")
game_id = int(os.environ.get("game_id"))
attribute_langs = []
for i in os.environ.get("attribute_langs").split(','):
    attribute_langs.append(i)
sys_lang = os.environ.get("sys_lang")
