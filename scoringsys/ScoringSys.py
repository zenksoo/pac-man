from typing import Dict, Any
import json
from gameLog import Log

class ScoreSys:
    """_summary_
    """

    def __init__(self, file_name: str) -> None:
        self.scoring_file = file_name
        self.scores: Dict[str, Any] = {}

    @staticmethod
    def _valid_player_name(player_name: str) -> bool:
        if len(player_name) > 10:
            Log._tty_logs(f"New player score does't saved", Log.ERROR)
            Log._tty_logs(f"invalid player name '{player_name}', player name must be 10 character max!", Log.WARNING)
            return (False)
        if not "".join(player_name.split(" ")).isalpha():
            Log._tty_logs(f"New player score does't saved", Log.ERROR)
            Log._tty_logs(f"invalid player name '{player_name}', player name must be alphanumeric and spaces only!", Log.WARNING)
            return (False)
        return True

    @staticmethod
    def _valid_score_value(player_score: int) -> bool:
        try:
            player_score = int(player_score)
            if (player_score < 0):
                Log._tty_logs(f"New player score does't saved", Log.ERROR)
                Log._tty_logs(f"invalid highscore value, highscore value must be positive integer greater then or equal 0", Log.WARNING)
                return False
        except ValueError:
            Log._tty_logs(f"New player score does't saved", Log.ERROR)
            Log._tty_logs(f"invalid highscore value: '{player_score}'", Log.ERROR)
            return False
        return True

    def _save(self, new_data: Dict[str, Any]) -> None:
        with open(self.scoring_file, 'w') as f:
            json.dump(new_data, f, indent=4)

    def _load(self) -> Dict[str, Any]:
        """ load old players score and sorte them from bigger to smaller

        Returns:
            Dict[str, Any]: _description_
        """
        is_data_updated: bool = False
        try:
            with open(self.scoring_file, 'r') as f:
                self.scores = json.load(f)

            keys = list(self.scores.keys())
            for i in range(0, len(list(self.scores.keys()))):
                key = keys[i]
                val = self.scores[key]

                del self.scores[key]

                if (len(key) > 10 or not isinstance(val, int) or val < 0):
                    is_data_updated = True

                if (len(key) > 10):
                    Log._tty_logs(f"loading invalid player name '{key}'", Log.WARNING)
                    Log._tty_logs(f"truncate player name to '{key}'", Log.WARNING)
                    key = key[0:10]
                if (not isinstance(val, int)):
                    Log._tty_logs(f"invalid data type for player score", Log.WARNING)
                    val = 0
                elif (val < 0):
                    Log._tty_logs(f"invalid score value for {key}: '{val}'", Log.WARNING)
                    val = 0

                self.scores[key] = val

            if is_data_updated:
                self._save(self.scores)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
        return dict(sorted(self.scores.items(), key=lambda x: x[1], reverse=True))

    def _update_or_add_player_heighscore(self, player_name: str, player_score: int) -> None:
        # this function was called every time the player end the game to save his new score or create one if it's does't exits
        # we will to check if the player name and score is correct then updating/saving them
        # if there's a broblem i will to skip it without crashing the game and dipslay clean msg to the user to tell them that his new score was't updatd
        if not self.scores:
            self._load()

        if not self._valid_player_name(player_name) or not self._valid_score_value(player_score):
            return None

        if ((self.scores.get(player_name) and player_score > self.scores[player_name])
            or (not self.scores.get(player_name))):
            self.scores[player_name] = player_score
        self._save(self.scores)
