import sys
import pickle


def read_file(filename):

    with open(filename, 'rb') as raccoon:
        return pickle.load(raccoon)


def map_to_int(measurements):

    measurements_copy = {key: int(value[0:2]) for key, value in measurements.items()}
    return measurements_copy


def find_faulty(primary, secondary, threshold):

    prim_sec = set()

    for rac in secondary:
        if (secondary[rac] - primary[rac] > threshold or secondary[rac] - primary[rac] < -threshold):
            prim_sec.add(rac)

    return prim_sec


def display_warnings(faulty_sensors):

    print('Analyzis of the provided files is complete.')
    print('-------------------------------------------')
    print('\nThe following sensors differ more than 2°:')

    for x in faulty_sensors:
        print(x)


def main():

    try:
        if len(sys.argv) != 3:
            print('Error')
        else:
            file_1 = sys.argv[1]
            file_2 = sys.argv[2]
            rac_1 = read_file(file_1)
            rac_2 = read_file(file_2)
            m_to_i_1 = map_to_int(rac_1)
            m_to_i_2 = map_to_int(rac_2)
            raccoon = find_faulty(m_to_i_1, m_to_i_2, 2)
            display_warnings(raccoon)
    except FileNotFoundError:
        print('Error: The files given as arguments are not valid.')


if __name__ == '__main__':
    main()
