import json

file = open('snopes_store.json', 'w+')

choice, result = input(), {}
print("Format: 1. URL || 2. STATUS || 3. CATEGORY")
while choice != 'exit':
    url, status, category = input().split()
    result[url] = {'status': status, 'category': category}
    choice = input()
json.dump(result, file)