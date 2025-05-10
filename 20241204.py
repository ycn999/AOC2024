from collections import defaultdict

input = 'drive/MyDrive/Colab Notebooks/aoc2024/aoc202404_full.txt'

words = []
with open(input, 'r') as file:
  for line in file:
    words.append(line.strip())

char_search = words
def count_xmas_search(char_search):

  def get_diagonal(words_list):
    height = len(words_list)
    width = [len(i) for i in words_list][0]

    diagonal_dict = defaultdict(list)
    for row in range(0, width):
      for col in range(0, height):
        diagonal_dict[row-col].append(words_list[row][col])

    diagonal = [''.join(v) for v in diagonal_dict.values()]

    return diagonal

  # get character strings in all directions
  left_right = char_search
  up_down = [''.join(chars) for chars in zip(*char_search)]
  diag = get_diagonal(left_right) + get_diagonal([l[::-1] for l in left_right])

  combined = left_right + up_down + diag

  sum = 0
  for char in combined:
    sum += char.count('XMAS')
    sum += char.count('SAMX')

  return sum

ans = count_xmas_search(words)
print(ans)
