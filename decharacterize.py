import sys

def decharacterize(sent):
  char_list = sent.split(u" ")
  char_list = map(lambda c: c if c != u"<w/>" else u" ", char_list)
  return u"".join(char_list)

line = sys.stdin.readline()
while line:
  char_line = decharacterize(line)
  sys.stdout.write(char_line)
  line = sys.stdin.readline()

