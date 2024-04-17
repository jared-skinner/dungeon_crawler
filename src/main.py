import argparse
from typing import Any

from framework.util import load_game, list_saves
from games.quest import Quest

def parse_args() -> Any:
    parser = argparse.ArgumentParser()

    parser.add_argument("--list", help="list save games", action="store_true")
    parser.add_argument("--load", help="load saved game")
    parser.add_argument("--play", help="play a new game")
    parser.add_argument("--games", help="list games", action="store_true")

    return parser.parse_args()

def main() -> None:
    args = parse_args()

    if args.list:
        list_saves()

    if args.load:
        game = load_game(args.load)
        game.start()

    if args.play:
        if args.play == "quest":
            quest = Quest()
            quest.start()

    if args.games:
        print("Games: ")
        print("")
        print("    * quest")

if __name__ == "__main__":
    main()
