import argparse, json, sys, shutil


class Test(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()


def main():
    parser = Test().parser
    parser.add_argument(
        "-f",
        "--filename",
        default="var/log/nginx/error.log",
        help="File location (default = var/log/nginx/error.log)",
    )
    parser.add_argument(
        "-t",
        "--type",
        help="Type",
        choices=["json", "text"],
        dest="type",
        default="text",
    )
    parser.add_argument(
        "-o", "--o", help="Output file", dest="output", nargs="?", default=sys.stdout
    )

    args = parser.parse_args()

    if args.output is not None:
        try:
            with open(args.output, "w") as fwrite:
                with open(args.filename, "r") as fread:
                    fwrite.write(fread.read())
        except:
            pass

    if args.type == "json":
        with open(args.filename, "r") as fread:
            data = json.load(fread)
            print(data)
    elif args.type == "text":
        with open(args.filename, "r") as fread:
            print(fread.read())


if __name__ == "__main__":
    main()
