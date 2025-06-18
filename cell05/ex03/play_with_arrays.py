original_array = [2, 8, 9, 48, 8, 22, -12, 2]

filtered_no_duplicates = []
seen = set()

for value in original_array:
    if value > 5 and value not in seen:
        filtered_no_duplicates.append(value)
        seen.add(value)

print(filtered_no_duplicates)