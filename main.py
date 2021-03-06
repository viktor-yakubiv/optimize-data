import string
from re import findall
from pprint import pprint


def optimize_data(template, data):
    def resolve_dict(keys, data, result, i = 0):
        key = keys[i]

        if i == len(keys) - 1:
            if type(key) is int:
                while len(result) <= key:
                    result.append(None)
            else:
                dot = key.find('.')
                if dot > -1:
                    key = key[:dot]
            result[key] = data[key]
        else:
            if not key in result:
                if type(data[key]) in (list, tuple):
                    result[key] = list()
                    keys[i + 1] = int(keys[i + 1])
                elif type(data[key]) is dict:
                    result[key] = {}
                else:
                    result[key] = data[key]
            resolve_dict(keys, data[key], result[key], i + 1)

    result = {}

    for placeholder in findall(r'{([\w\[\].]+)}', template):
        keys = findall(r'\[?([\w.]+)\]?', placeholder)
        resolve_dict(keys, data, result)
    return result


def main():
    template = (
        'Python version: {languages[python][latest_version]}\n'
        'Python site: {languages[python][site]}\n'
        'Rust version: {languages[rust][latest_version]}\n'
    )

    data = {
        'languages': {
            'python': {
                'latest_version': '3.6',
                'site': 'http://python.org',
            },
            'rust': {
                'latest_version': '1.17',
                'site': 'https://rust-lang.org',
            },
        },
    }
    print("Original data:")
    pprint(data)

    new_data = optimize_data(template, data)
    print("Optimized data:")
    pprint(new_data)


if __name__ == '__main__':
    main()
