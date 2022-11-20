import argparse
import os
from dotenv import load_dotenv
import sys

__version__ = "1.0.0-alpha"

def get_args() -> argparse.Namespace:
    """Get necessary environment variables for running the script"""
    load_dotenv()  # load .env.template file for defaults in parser arguments
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__), description="A Discord Bot that fetches posts from subreddits")
    parser.add_argument("--bot-token",
                        metavar="TOKEN",
                        type=str,
                        default=os.environ.get("BOT_TOKEN"),
                        help="Discord Bot Token"
                        )
    parser.add_argument("--reddit-id",
                        metavar="ID",
                        type=str,
                        default=os.environ.get("REDDIT_ID"),
                        help="Reddit Client ID"
                        )
    parser.add_argument("--reddit-secret",
                        metavar="KEY",
                        type=str,
                        default=os.environ.get("REDDIT_SECRET"),
                        help="Reddit Client Secret"
                        )
    parser.add_argument("--version",
                        action="store_true",
                        help="print script version"
                        )
    args = parser.parse_args()
    # check for version
    if args.version:
        sys.exit("%s %s" % (os.path.basename(__file__), __version__))
    if not args.bot_token:
        sys.exit("Error: Please supply BOT_TOKEN as environment variable or flag")
    if not args.reddit_id:
        sys.exit("Error: Please supply REDDIT_ID as environment variable or flag")
    if not args.reddit_secret:
        sys.exit("Error: Please supply REDDIT_SECRET as environment variable or flag")
    return args

def main() -> None:
    """Main bot function"""
    args = get_args()

if __name__ == "__main__":
    main()