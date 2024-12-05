import argparse

BULKY_TOTAL_DIMENSIONS = 1000000
BULKY_SINGLE_DIMENSION = 150
HEAVY_WEIGHT = 20
REJECTED_VALUE = "REJECTED"
SPECIAL_VALUE = "SPECIAL"
STANDARD_VALUE = "STANDARD"


def sort(width: int, height: int, length: int, mass: int) -> str:
    """Returns a STATUS based on the given dimensions and weight"""
    
    # Check for any invalid arguments
    for argument_name in ["width", "height", "length", "mass"]:
        argument_value = locals()[argument_name]
        if type(argument_value) != int or argument_value <= 0:
            raise ValueError(f"{argument_name} must be a positive integer, but got '{argument_value}'")

    total_dimensions = width * height * length
    max_dimension = max([width, height, length])
    
    is_bulky = total_dimensions >= BULKY_TOTAL_DIMENSIONS or max_dimension >= BULKY_SINGLE_DIMENSION
    is_heavy = mass >= HEAVY_WEIGHT

    if is_bulky and is_heavy:
        # The package is both bulky and heavy, reject it
        return REJECTED_VALUE
    
    if is_bulky or is_heavy:
        # The package is either bulky or heavy, so it is special
        return SPECIAL_VALUE
    
    # The package is neither bulky nor heavy, so it is standard
    return STANDARD_VALUE

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter a package width, height, length, and mass, all as positive integrers.")
    parser.add_argument("width", type=int, help="The width of the package")
    parser.add_argument("height", type=int, help="The height of the package")
    parser.add_argument("length", type=int, help="The length of the package")
    parser.add_argument("mass", type=int, help="The mass of the package")
    args = parser.parse_args()

    print(sort(args.width, args.height, args.length, args.mass))