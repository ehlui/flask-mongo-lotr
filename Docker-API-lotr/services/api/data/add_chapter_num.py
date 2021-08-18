import json


def append_json(json_el):
    with open('chapters_v2.json', mode='+a') as output:
        output.write(json.dumps(json_el))
        output.write(',')


with open('chapters.json', mode='r') as input:
    json_file = json.loads(input.read())
    counter = 1
    for e in json_file:
        e['chapter'] = counter
        print(e)
        append_json(e)
        counter += 1
