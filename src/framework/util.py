import os
import pickle

from typing import Any

ROOT_DIR = os.path.dirname(__file__)
SAVES_DIR = os.path.join(ROOT_DIR, "..", "saves")

def save_game(game: Any, save_name: str) -> None:
    save_file_name = os.path.join(SAVES_DIR, save_name)

    if os.path.isfile(save_file_name):
        overwrite = input(f"the file {save_name} already exists.  Overwrite? (Y/n) ")

        if overwrite != "Y":
            return

    with open(save_file_name, "wb") as f:
        pickle.dump(game, f)


def load_game(save_name: str) -> Any:
    save_file_name = os.path.join(SAVES_DIR, save_name)

    if not os.path.isfile(save_file_name):
        print(f"Cannot find {save_name}!")

    with open(save_file_name, "rb") as f:
        game = pickle.load(f)

    return game

def list_saves() -> None:
    for file in os.listdir(SAVES_DIR):
        print(file)
