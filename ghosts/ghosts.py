from typing import List, Tuple, Any
from abc import ABC, abstractmethod


class Area2D:
    # i thing this class make the ghost object easy to control when we tallking about the ghost area when player enter them it detect them and change the ghost movement
    # i hope make it as signle when player enter the area this function called or make them detect the player
    def _is_area_body_entred(self, r: int, obj) -> bool:

        return False

class ghost(ABC):
    # abstract class for all ghost in the game so the abstract method must be implemented for each ghost :)
    def __init__(self) -> None:
        # self.mlximg: mlx_image_t
        self.grid_pos: Tuple[int, int] = (0, 0) # position of the ghost in maze grid
        # before we calculate the width and height of the cell
        # to centering the ghost inside cell
        self.pixel_pos: Tuple[float, float] = (0, 0) # position of the ghost in mlx window
        self.speed: int = 100

        # target enmey if
        # global variable assign the target object to it to make the ghost follow this object and when it enter ghost area detect them and follow them :)
        # self.target_obj = None

    def _calculate_new_pixel_pos(self, new_grid_pos: Tuple[int, int],
                                 cell_width: int, cell_height: int) -> Tuple[int, int]:
        new_pixel_pos: Tuple[int, int]
        x, y = new_grid_pos
        if (x > self.grid_pos[0]):
            px = (x - self.grid_pos[0]) * cell_width
        else:
            px = (self.grid_pos[0] - x) * cell_width

        if (y > self.grid_pos[1]):
            py = (y - self.grid_pos[1]) * cell_height
        else:
            py = (self.grid_pos[1] - y) * cell_height

        return (px, py)

    def _move_toward(self, new_pos: Tuple[float, float]) -> None:
        # this function called from mlx_loop_hock each frame he move the ghost one step forward
        # this function calculate direction of ghost to the target position and then move them by constant speed :)

        # the direction of the ghost is how much i need to move in x and in y at each time :)

        sx = abs(new_pos[0] - self.pixel_pos[0])
        sy = abs(new_pos[1] - self.pixel_pos[1])

        step = max(sx, sy)

        dx = sx / step
        dy = sy / step

        new_pos_x = self.pixel_pos[0] + dx * self.speed
        new_pos_y = self.pixel_pos[1] + dy * self.speed

        self.pixel_pos = (new_pos_x, new_pos_y)

        # take the mlximg and assign to them new coordinate x,y :)
        # self.mlximg.contents.instances[0].x = round(new_pos_x)
        # self.mlximg.contents.instances[0].y = round(new_pos_y)

    def _is_ghostarea_body_entred(self, body: Any, body_width: int, body_height: int, r: int) -> bool:
        # the body is must be an object with x and y coordinate to check his position with the ghost area
        if (body.x + (body_width // 2) >= self.pixel_pos[0] - r and
            body.x - (body_width // 2) <= self.pixel_pos[0] + r and
            body.y + (body_height // 2) >= self.pixel_pos[1] - r and
            body.y - (body_height // 2) <= self.pixel_pos[1] + r):
            return True
        return False

    @abstractmethod
    def _get_path_to_body(self, map: List[List[int]], player: Any) -> List[Tuple[int, int]]:
        pass

