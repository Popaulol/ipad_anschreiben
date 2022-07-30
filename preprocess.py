import json
import sys
import pprint
import re
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf8")
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf8")


if __name__ == "__main__":
    if len(sys.argv) > 1:  # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    try:
        raise FileNotFoundError
        with open("names.json", "r") as f:
            names = json.load(f)
    except FileNotFoundError:
        with open("names_template.json", "r") as f:
            names = json.load(f)
    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)
    for section in book["sections"]:
        # pprint.pprint(section, sys.stderr)
        # print("-----------------------------------------", file=sys.stderr)
        try:
            content = section["Chapter"]["content"]

            # print(content, file=sys.stderr)
        except KeyError as e:
            pass  # print(e)
        if r"{{$" in content:
            indecies = tuple(re.finditer(r"{{\$.+}}", content))
            # print(f"{indecies}", file=sys.stderr)
            for index in indecies:
                # print(index[0][3:-2], file=sys.stderr)
                section["Chapter"]["content"] = section["Chapter"]["content"].replace(
                    index[0], names[index[0][3:-2]]
                )

    print(json.dumps(book))

# pprint.pprint(context, sys.stderr)
# pprint.pprint(book, sys.stderr)
