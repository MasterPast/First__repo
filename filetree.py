import sys
import pathlib


def recursive_print(path, depth=0, margin_simbol='-'):
    margin = margin_simbol * depth
    if path.is_dir():
        print(margin + path.name + '/')
        for item in path.iterdir():
            recursive_print(item, depth=depth+1)
    else:
        print(margin + path.name)
    


def main():
    path = pathlib.Path()
    #print(path)
    recursive_print(path)


if __name__ == '__main__':
    main()
