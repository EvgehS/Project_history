from dataclasses import dataclass
import json
import os


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, '../questions.json')

questions = json.load(open(json_file_path))

config = Config(
    tg_bot=TgBot(
        token=(
            "7640949977:AAGgR2l5xtPQ4DUmo5K5HkTtYiiI-u14yME"
        )
    )
)
