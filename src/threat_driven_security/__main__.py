"""Command-line interface."""
import fire

from .security import Security
#from threat_driven_security import Security


def main():
    fire.Fire(Security)


if __name__ == "__main__":
    main()
