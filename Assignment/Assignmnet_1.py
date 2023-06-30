def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10
print(find_pairs_with_sum(arr, target_sum))
