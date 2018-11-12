import re
import sys

def merge_reserve(char_list):
  ret = []
  reserve_buf = ""
  reserving_and = False
  reserving_at = False
  for idx, char in enumerate(char_list):
    if char == '&' and not reserving_and:
      reserve_buf += char
      reserving_and = True
    elif char == '@' and not reserving_at:
      reserve_buf += char
      reserving_at = True
    elif char == ';' and reserving_and:
      reserve_buf += char
      reserving_and = False
      ret.append(reserve_buf)
      reserve_buf = ""
    elif char == '@' and reserving_at:
      reserve_buf += char
      reserving_at = False
      ret.append(reserve_buf)
      reserve_buf = ""
    elif reserve_buf:
      reserve_buf += char
    else:
      ret.append(char)
  return ret

def characterize(sent, split_regex="."):
  splitter = re.compile(split_regex)
  char_list = splitter.findall(sent)
  char_list = map(lambda c: c if c != " " else u"<w/>", char_list)
  char_list = merge_reserve(char_list)
  return u" ".join(char_list)

line = sys.stdin.readline()
while line:
  char_line = characterize(line)
  sys.stdout.write(char_line + "\n")
  line = sys.stdin.readline()

