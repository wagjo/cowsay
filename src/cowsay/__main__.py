import argparse
import sys
from cowsay import impl

def main():
    parser = argparse.ArgumentParser(
        description="Announce a message with optional color and announcer. Default is cow."
    )
    parser.add_argument(
        "-c", "--color",
        help="Color of the text (optional)"
    )
    parser.add_argument(
        "-a", "--announcer",
        help="Name of the announcer (optional)"
    )
    parser.add_argument(
        "-t", "--think",
        action="store_true",
        help="Think instead of announce"
    )
    parser.add_argument(
        "message",
        nargs="?",
        help="The text message to announce (optional)"
    )

    args = parser.parse_args()

    if args.message == "-":
        data = sys.stdin.read()
    else:
        data = args.message

    impl.announce(data, args.color, args.think, args.announcer)

if __name__ == "__main__":
    main()