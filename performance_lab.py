# Problem 1: Find Most Frequent Element
# Return the value that appears the most. If tied, return either value.

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    most_common = numbers[0]
    highest_count = 0

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
        if counts[number] > highest_count:
            highest_count = counts[number]
            most_common = number

    return most_common


"""
Time and Space Analysis for Problem 1:
- Best-case time: O(n), because we check every number.
- Worst-case time: O(n) on average with a dictionary, but rare hash
  collisions can make dictionary operations slower.
- Average-case time: O(n), because each dictionary update is usually O(1).
- Space complexity: O(n) in the worst case if all numbers are different.
- Why this approach? A dictionary keeps track of counts in one pass.
- Could it be optimized? Sorting could save extra memory in some situations,
  but sorting takes O(n log n) time and might change the input order.
- Trade-off: The dictionary uses more memory to get faster counting.
"""


# Problem 2: Remove Duplicates While Preserving Order

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for Problem 2:
- Best-case time: O(n), since every item must be checked.
- Worst-case time: O(n) expected with a set; unusual hash collisions
  can make set operations slower.
- Average-case time: O(n), because set lookups are usually O(1).
- Space complexity: O(n), for the set and the new list.
- Why this approach? The set quickly checks for values already seen.
- Could it be optimized? A basic list check would avoid the set but
  could take O(n^2) time. An in-place version could reduce output storage,
  but it would change the original list.
- Trade-off: Using a set costs memory but speeds up duplicate checks.
"""


# Problem 3: Return All Pairs That Sum to Target
# Original version: compare each number with every later number.

def find_pairs_original(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs


# Optimized version: use a set instead of checking every possible pair.
def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        needed = target - number
        if needed in seen:
            pairs.append((needed, number))
        seen.add(number)

    return pairs


"""
Time and Space Analysis for Problem 3:
- Best-case time: O(n) for the optimized version, since it scans the list.
- Worst-case time: O(n) expected with a set; rare hash collisions can
  slow lookups.
- Average-case time: O(n), since set membership is usually O(1).
- Space complexity: O(n), for the set and result list.
- Why this approach? The set lets us find a matching number quickly.
- Could it be optimized? This is already O(n) expected time. A sorted
  two-pointer approach also works, but sorting usually costs O(n log n).
- Trade-off: The set uses extra memory to save time.

Optimization comparison:
- Original version: O(n^2) time because of the nested loops.
  It uses O(1) extra working space, not counting the output pairs.
- Optimized version: O(n) expected time and O(n) extra space.
- I optimized this by checking a set for the number needed to make the
  target, instead of comparing every pair. It uses more memory but
  runs faster for larger inputs.
"""


# Problem 4: Simulate List Resizing (Amortized Cost)
# Begin with capacity 2 and double it whenever the list fills up.

def add_n_items(n):
    if n < 0:
        raise ValueError('n cannot be negative')

    capacity = 2
    size = 0
    items = [None] * capacity

    for number in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f'Resizing from {capacity} to {new_capacity}')
            new_items = [None] * new_capacity
            for i in range(size):
                new_items[i] = items[i]
            items = new_items
            capacity = new_capacity

        items[size] = number
        size += 1

    return items[:size]


"""
Time and Space Analysis for Problem 4:
- When do resizes happen? When the list is full. Starting at capacity 2,
  it grows to 4, 8, 16, and so on.
- Best-case single append: O(1) if there is room.
- Worst-case single append: O(n) when copying all existing items.
- Average / amortized time per append: O(1).
- Total time for n appends: O(n), including all resizing copies.
- Space complexity: O(n), since extra capacity grows with the list.
- Why this approach? It shows how dynamic lists grow without resizing
  every time a new item is added.
- Could it be optimized? We could allocate all n slots in advance if
  we know n. That avoids resizing, but it does not demonstrate amortization.
- Trade-off: Doubling uses unused memory in return for fewer copies.
- Why doubling helps: Each full resize copies 2, then 4, then 8 items,
  etc. Those copies add up to less than 2n, so average append cost
  stays constant even though individual resizing steps cost more.
"""


# Problem 5: Compute Running Totals

def running_total(nums):
    totals = []
    current_sum = 0

    for number in nums:
        current_sum += number
        totals.append(current_sum)

    return totals


"""
Time and Space Analysis for Problem 5:
- Best-case time: O(n), because each number is processed once.
- Worst-case time: O(n), because there is just one loop.
- Average-case time: O(n), because there is just one loop.
- Space complexity: O(n), since we return a new list of the same size.
- Why this approach? Keeping a running sum avoids adding earlier
  numbers over and over.
- Could it be optimized? An in-place version could use O(1) extra
  space, but it would modify the input list instead of returning a new one.
- Trade-off: The new list uses memory but keeps the original data safe.
"""


# Test cases for all five problems, including edge cases.
def run_tests():
    # Problem 1
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([7, 7, 7]) == 7
    assert most_frequent([-2, -2, 1]) == -2
    assert most_frequent([]) is None
    assert most_frequent([2, 3]) in (2, 3)  # Tie

    # Problem 2
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([-1, 0, -1, 0]) == [-1, 0]

    # Problem 3 (input is assumed to have no duplicates)
    for function in (find_pairs_original, find_pairs):
        assert {frozenset(p) for p in function([1, 2, 3, 4], 5)} == {
            frozenset((1, 4)), frozenset((2, 3))
        }
        assert function([], 5) == []
        assert function([1], 2) == []
        assert {frozenset(p) for p in function([-2, -1, 0, 3, 5], 3)} == {
            frozenset((-2, 5)), frozenset((0, 3))
        }
        assert function([1, 2, 3], 100) == []

    # Problem 4
    import contextlib
    import io
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        assert add_n_items(6) == [0, 1, 2, 3, 4, 5]
    assert output.getvalue().strip().splitlines() == [
        'Resizing from 2 to 4', 'Resizing from 4 to 8'
    ]
    with contextlib.redirect_stdout(io.StringIO()):
        assert add_n_items(0) == []
        assert add_n_items(1) == [0]
        assert add_n_items(2) == [0, 1]
    try:
        add_n_items(-1)
        assert False, 'A negative n should raise an error'
    except ValueError:
        pass

    # Problem 5
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([]) == []
    assert running_total([5]) == [5]
    assert running_total([-2, 3, -1]) == [-2, 1, 0]
    assert running_total([0, 0, 0]) == [0, 0, 0]

    print('All tests passed!')


if __name__ == '__main__':
    run_tests()
    print('Example of resizing when adding 6 items:')
    add_n_items(6)
