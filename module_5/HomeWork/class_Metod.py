import json


class C1:
    title = '1'
    text = '2'
    author = '3'

    def save(self):

        attributes = {}

        for attr in (list(filter(lambda x: not x.startswith('_'), dir(C1)))):
            attr_value = getattr(self, attr)

            if str(type(attr_value)) != "<class 'method'>":
                attributes[attr] = attr_value

        attributes_json = json.dumps(attributes)

        with open("attributes.json", "w") as my_file:
            my_file.write(attributes_json)


def main():
    c = C1()
    c.save()


if __name__ == '__main__':
    main()
