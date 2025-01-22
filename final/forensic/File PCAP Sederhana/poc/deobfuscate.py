import json

with open('char_mapping.json', 'r') as file:
    data = json.load(file)

# Sorting berdasarkan length value
sorted_data = dict(sorted(data.items(), key=lambda item: len(item[1]), reverse=True))

with open('s.txt', 'r+') as file:
    lines = file.readlines()
    php_content = lines[2]

    # Replace value
    for value, key in sorted_data.items():
        php_content = php_content.replace(key, value)
    
    print(php_content)
