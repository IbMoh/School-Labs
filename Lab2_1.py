import sys


def read_file(filename):

    chatters = []
    with open(filename, 'r') as lab_file:
        line = lab_file.readline()

        while line != '':
            name = line.rstrip('\n')
            line = lab_file.readline()
            message = line.rstrip('\n')
            chatters.append((name, message))
            line = lab_file.readline()
    return chatters


def display_entry(name, message):

    print(f'[{name}] --> {message}')


def main():

    try:
        if len(sys.argv) != 2:
            print('Error')
        else:
            filename = sys.argv[1]
            messages = read_file(filename)
            otter = input('Enter a name to search for: ')
            for n in messages:
                if n[0] == otter:
                    display_entry(n[0], n[1])
    except FileNotFoundError:
        print(f'Error: The file \'{filename}\' could not be found.')


if __name__ == '__main__':

    main()
