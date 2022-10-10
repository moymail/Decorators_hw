import datetime


def logger(path):
    def new_logger(some_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.now().strftime('%x %X')
            name = some_function.__name__
            result = f'Функция {name} с аргументами {args} и {kwargs} вызвана {date}'
            with open(path, "w", encoding='utf-8') as f:
                f.write(result)
            return result
        return new_function
    return new_logger
