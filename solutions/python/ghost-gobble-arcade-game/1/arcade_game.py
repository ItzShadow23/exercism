
def eat_ghost(power_pellet: bool, touching_ghost: bool) -> bool:
    """Check whether Pac-Man can eat a ghost."""
    return power_pellet and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Check whether Pac-Man earns points."""
    return touching_power_pellet or touching_dot


def lose(power_pellet: bool, touching_ghost: bool) -> bool:
    """Check whether Pac-Man loses the game."""
    return touching_ghost and not power_pellet


def win(
    has_eaten_all_dots: bool,
    power_pellet: bool,
    touching_ghost: bool
) -> bool:
    """Check whether Pac-Man wins the game."""
    game_is_lost = lose(power_pellet, touching_ghost)
    return has_eaten_all_dots and not game_is_lost
