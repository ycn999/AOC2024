def pair_transform(pair_text):
  left = []
  right = []

  pairs = pair_text.split("\n")

  for p in pairs:
    left.append(int(p.split(" ")[0]))
    right.append(int(p.split(" ")[-1]))

  return left, right
  
pairs = pair_transform(input)


def find_distance(pairs):
  for lists in pairs:
    left_sort = sorted(pairs[0])
    right_sort = sorted(pairs[1])

  rows = len(left_sort) 
  distance = 0

  for i in range(0, rows):
    distance += abs(left_sort[i] - right_sort[i])

  return distance
  
# puzzle 1 output
puzzle1 = find_distance(pairs)

def find_similarity(pairs):
  left_list = pairs[0]
  right_list = pairs[1]
  rows = len(left_list)

  score = 0
  for i in range(0, rows):
    score += sum(r == left_list[i] for r in right_list) * left_list[i]
  
  return score

# puzzle 2 output
puzzle2 = find_similarity(pairs)
