import utils_1
import argparse

def main():
    parser = argparse.ArgumentParser(description="Countdown and auto-open a file using your default system application.",
                                    epilog="Example: python main.py --file sample.pdf --delay 5")
    parser.add_argument("--file", required=True, help="Filename")
    parser.add_argument("--delay", type=int, default=10, help="Countdown duration in seconds")
    args = parser.parse_args()

    utils_1.countdown(args.delay)
    utils_1.open_file(args.file)

    print("File opened!")

if __name__ == "__main__":
    main()