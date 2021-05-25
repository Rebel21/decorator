import datetime
import hashlib


def logger(file_name):
    def _logger(func):
        def _wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, 'a') as f:
                f.writelines(f'{datetime.datetime.today()} - {args} - {func.__name__} - {result}\n')
            return result

        return _wrapper

    return _logger


@logger('log.log')
def generator(file_name):
    with open(file_name) as f:
        for string1 in f:
            yield hashlib.md5(string1.encode()).hexdigest()


if __name__ == '__main__':
    for string in generator('country_links.txt'):
        print(string)
