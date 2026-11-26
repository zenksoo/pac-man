from typing import List, Tuple, Any
from heapq import heappop, heappush
from .ghosts import ghost

class Blinky(ghost):
    def __init__(self) -> None:
        super().__init__()

    def _get_path_to_body(self, map: List[List[int]], player: Any) -> List[Tuple[int, int]]:
        path: List[tuple[int, List[Tuple[int, int]]]] = [] # (cost, List[(x, y)])

        queue = [(0, [(self.grid_pos[0], self.grid_pos[1])])]
        best_path: List[Tuple[int, int]] = []

        while (len(queue)):
            cost, curr_path = heappop(queue)
            end_path = curr_path[-1]
            ex, ey = end_path
            # the while stop if the queue is empty or when i reach the end point
            # or when the smallest path have more then (column * row) size that's mean it enter every cell in the map so no path between two point ;(
            if (ex == player.x and ey == player.y):
                best_path = curr_path
                break

            # 0000 1111
            # x + 1 => mean to left mean to east  | i need to check west of the target cell  :)
            # x - 1 => mean to right mean to west | i need to check east of the target cell  :)
            # y + 1 => mean to down mean to south | i need to check north of the target cell :)
            # y - 1 => mean to up mean to north   | i need to check south of the target cell :)
            neighbors = [(3, ex + 1, ey), (1, ex - 1, ey), (0, ex, ey + 1), (2, ex, ey - 1)]

            # cuz we pass a copy of map as 2d array i wiil to make bit index 5 from lsb 1 if the cell is visited :)
            # XXX1 XXXX mean the cell was visited :)
            for neigh in neighbors:
                shift, x, y = neigh
                if (x >= 0 and y >= 0 and x < len(map[0]) and y < len(map)):
                    if ((map[y][x] >> 4) & 1):
                        continue
                    if (not (map[y][x] >> shift) & 1):
                        heappush(queue, (cost + 1, curr_path + [(x, y)]))
                        map[y][x] |= (1 << 4)

        print("the best path is", best_path)

        print("")
        for y in range(len(map)):
            for x in range(len(map[y])):
                if ((x, y) == (player.x, player.y)):
                    print("\033[102m E \033[49m", end="")
                elif ((x, y) == (self.grid_pos[0], self.grid_pos[1])):
                    print("\033[103m S \033[49m", end="")
                elif ((x, y) in best_path):
                    print("\033[106m   \033[49m", end="")
                else:
                    print("\033[101m . \033[49m", end="")
            print("")
        print()

        return super()._get_path_to_body(map, player)
