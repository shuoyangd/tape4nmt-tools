import sys

def characterize(sent):
  char_list = list(sent)
  char_list = map(lambda c: c if c != " " else "<w/>", char_list)
  return " ".join(char_list)

line = sys.stdin.readline()
while line:
  char_line = characterize(line)
  sys.stdout.write(char_line)
  line = sys.stdin.readline()

