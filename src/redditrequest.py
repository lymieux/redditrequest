from rr_setup import get_config_args, get_env_args
from rr_bot_logic import Bot

_version = "1.0.0-alpha"


def main() -> None:
    """Main bot function"""
    env_vars = get_env_args(__file__, _version)
    config_vars = get_config_args()
    rr_bot = Bot(env_vars=env_vars, config_vars=config_vars)
    rr_bot.run()


if __name__ == "__main__":
    main()
