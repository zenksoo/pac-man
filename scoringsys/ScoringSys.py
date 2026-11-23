from typing import Dict, Any
import json
from gameLog import Log

class ScoreSys:
    def __init__(self, file_name: str) -> None:
        self.scoring_file = file_name
        self.scores: Dict[str, Any] = {}

    def _parcing_scoring_data(self) -> None:
        # i need to check each player his name and score and then when i find some problem on it i remove it from the dict and diplay logs to stderr as warrning and then skip crashing the game

        for key, val in self.scores.items():
            print(key, val)
            pass


    def _save(self, new_data: Dict[str, Any]) -> None:
        with open(self.scoring_file, 'w') as f:
            json.dump(new_data, f, indent=4)

    def _load(self) -> Dict[str, Any]:
        """ load old players score and sorte them from bigger to smaller

        Returns:
            Dict[str, Any]: _description_
        """
        try:
            with open(self.scoring_file, 'r') as f:
                self.scores = json.load(f)
            self._parcing_scoring_data()
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
        return dict(sorted(self.scores.items(), key=lambda x: x[1], reverse=True))

    def _update_or_add_player_score(self, player_name: str, player_score: int) -> None:
        # this function was called every time the player end the game so to save his new score or create one if it's does't exits
        # we will to check if the player name and score is correct then updating/saving them
        # if there's a broblem i will to skip it without crashing the game and dipslay clean msg to the user to tell them that his new score was't updatd

        if len(player_name) > 10:
            Log._tty_logs(f"player highscore don't saved", Log.WARNING)
            Log._tty_logs(f"invalid player name '{player_name}', player name length must be less then 10 characters", Log.WARNING)

        try:
            player_score = int(player_score)
        except ValueError:
            Log._tty_logs(f"", Log.ERROR)

        self.scores[player_name] = player_score
        self._save(self.scores)

# wach kadakol tbn
