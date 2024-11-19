from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    start = datetime.now()
    for i in filenames:
        read_info(i)
    end = datetime.now()
    print(f'Линейный вызов {end - start}')

    start = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'Многопроцессный вызов {end - start}')