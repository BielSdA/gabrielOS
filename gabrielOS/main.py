from core.identity import load_profile, Identity
from interface.cli import show_cli

if __name__ == "__main__":
    profile = load_profile()
    identidade = Identity(profile)
    show_cli(identidade)
