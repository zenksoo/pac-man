from scoringsys import ScoreSys
from logs import Log
from ghosts import Blinky

class player:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
if __name__ == "__main__":
    score = ScoreSys("highscore.json")


    # Log.show_logs = True
    # score._load()
    # score._update_or_add_player_heighscore("johan", 10000)
    # score._update_or_add_player_heighscore("johan two", 10000)
    # score._update_or_add_player_heighscore("johan 3", 10000)
    # score._update_or_add_player_heighscore("baki", "invalid type")
    # score._update_or_add_player_heighscore("baki", -100)

    # print(score.scores)

    map = [
        [0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000],
        [0b0000,0b0000,0b0000,0b0000,0b0000,0b0100,0b0100,0b0100,0b0100,0b0000,0b0000,0b0000],
        [0b0000,0b0000,0b0000,0b0000,0b0010,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000],
        [0b0010,0b0000,0b0100,0b0100,0b0010,0b0000,0b0010,0b0000,0b0000,0b0000,0b0000,0b0000],
        [0b0010,0b0010,0b0000,0b0000,0b0000,0b0000,0b0010,0b0000,0b0100,0b0100,0b0100,0b0100],
        [0b0000,0b0000,0b0010,0b0000,0b0000,0b0000,0b0010,0b0000,0b0000,0b0000,0b0000,0b0000],
        [0b0000,0b0000,0b0000,0b0000,0b0010,0b0100,0b0110,0b0000,0b0000,0b0010,0b0000,0b0000],
        [0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0010,0b0000,0b0000],
        [0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0000,0b0010,0b0000,0b0000],
        [0b0000,0b0010,0b0000,0b0000,0b0010,0b0000,0b0000,0b0000,0b0000,0b0000,0b0001,0b0000]


        ] # 16 cell if the path enter all cell means the path have 16 position or greater

    p = player(0, 0)
    ghost = Blinky()
    ghost.grid_pos = (10, 8)

    print(ghost._is_ghostarea_body_entred(p, 1, 10, 10))

    ghost._get_path_to_body(map, p)

