import re
import sys

def characterize(sent, split_regex="."):
  splitter = re.compile(split_regex)
  char_list = splitter.findall(sent)
  char_list = map(lambda c: c if c != " " else u"<w/>", char_list)
  return u" ".join(char_list)

line = sys.stdin.readline()
while line:
  char_line = characterize(line)
  sys.stdout.write(char_line + "\n")
  line = sys.stdin.readline()

