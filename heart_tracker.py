from datetime import datetime


def accept_package(package: tuple, storage_data: dict) -> dict:
    if check_correct_data(package, storage_data):
        storage_data[package[0]] = package[1]
    return storage_data


def check_correct_data(package: tuple, data_dict: dict) -> bool:
    if len(package) != 2 or package[0] == '' or package[1] in (0, ''):
        return False
    if data_dict:
        last_time = datetime.strptime(list(data_dict.keys())[-1],
                                      '%H:%M:%S').time()
        current_time = datetime.strptime(package[0], '%H:%M:%S').time()
        if last_time >= current_time:
            return False
    return True


if __name__ == '__main__':
    storage_data: dict = {}

    while True:
        package = tuple(input().split(','))
        storage_data = accept_package(package, storage_data)

        time, heart_rate = package

        if package[0] in storage_data:
            print()
            print(f'Время: {time}.')
            print(f'Частота сердечных сокращений за сегодня: {heart_rate} '
                  'уд/мин.')
            if int(heart_rate) < 60:
                print('Главное — быть активным!')
                print()
            elif 60 <= int(heart_rate) < 80:
                print('Хороший результат, Вы движетесь '
                      'в правильном направлении!')
                print()
            elif 80 <= int(heart_rate) < 100:
                print('Осторожно успокойтесь!')
                print()
            else:
                print('Осторожно что-то не так! Обратитесь к врачу')
                print()
