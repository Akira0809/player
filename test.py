from collections import defaultdict

def sort_and_group(data):
    tmp_dict = defaultdict(list)

    for item in data:
        color = item['color']
        number = item.get('number')
        special = item.get('special')
        tmp_dict[color].append({'number': number, 'special': special})

    sorted_list = [
        {'color': color, **{k: v for k, v in item.items() if v is not None}}
        for color, items in sorted(tmp_dict.items(), key=lambda x: (len(x[1]), max((i['number'] or float('-inf')) for i in x[1]), any(i['special'] for i in x[1])), reverse=True)
        for item in sorted(items, key=lambda x: (x['special'] is not None, x['special'], x['number'] or float('-inf')), reverse=True)
    ]

    return sorted_list

data = [
    {'color': 'yellow', 'number': 3},
    {'color': 'yellow', 'number': 9},
    {'color': 'green', 'number': 7},
    {'color':'blue','number':7},
    {'color':'blue','number':8},
    {'color':'blue','number':2},
    {'color':'red','number':9},
    {'color':'red','special':'drow_2'},
    {'color':'red','special':'skip'},
]

result = sort_and_group(data)
print(result)
