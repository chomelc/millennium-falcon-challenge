import sys
from empire import Empire
from millennium_falcon import MillenniumFalcon


def compute_odds(empire_file, millennium_falcon_file="millennium-falcon.json"):
    """Computes the odds of the Falcon's mission to succeed.
    @param `empire_file`: the path to the `empire.json` file
    @param `millennium_falcon_file`: the path to the `millennium-falcon.json` file, 
        if not provided, it uses the default one stored in `backend/` 
    @return the computed odds
    """
    mf = MillenniumFalcon(millennium_falcon_file)
    empire = Empire(empire_file)
    return 4.2


if __name__ == '__main__':
    print(compute_odds(sys.argv[2], sys.argv[1]))
