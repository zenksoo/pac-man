### ghosts.py module:
GHOST abstract base class that must all other ghosts objects inherit from it and implement it's own implementation of `_get_path_to_player` method

the class containe shared methods with other ghost objects like:

`_move_toward`: this method move the ghost 1 step forward from his position to the next step from his path that generated before by constant speed it change the object pixel_pos attr and change the position of image

`_is_ghostarea_body_entred`: this method check if the body object enter the ghost area it's accept body and Any data type and must be object has two required attr x and y to check them with the ghost current position and the second parameter is r which represent the raduis of the cube :) so (x + r and x - r , range of area in x-axis) and (y + r and y - r, range of area in y-axis)

`_calculate_new_pixel_pos`: this my additionall one, it's calculate new position of the ghost in pixel, like when we work with maze of grid the presentation of cell in mlx window not just 1px it's be bigger than that like 20 or 40 and this change the position of the object from (1,3) => (20, 60) i hop you understand this but i thing it's not required
