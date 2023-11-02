import json
def task() -> float:
    filename = 'input.json'
    summ = 0
    with open(filename) as file:
        data = json.load(file)
    list_score = [item["score"] for item in data]
    list_weight = [item["weight"] for item in data]
    for i in range(len(list_score)):
        summ += list_score[i]*list_weight[i]
    return round(summ,3)
print(task())