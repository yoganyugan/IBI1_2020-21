def task_1(DNA):
  complementary = {'a':'T', 'g':'C', 'A':'T', 'T':'A', 'G':'C', 'c':'G', 't':'A', 'C':'G'}
  letters = list(DNA)

#convert it into the reverse complement
  letters = [complementary[x] for x in letters]
  list.reverse(letters)

#change the list to string
  return print("".join(letters))

#input DNA
print('input the DNA: TCgatcGGCTAtCac, the result is shown:')
task_1('TCgatcGGCTAtCac')