import os
import ssl
import sys
import urllib.request
import validators

if len(sys.argv) < 3:
  sys.stderr.write("usage: python download_or_link.py src dst")
  sys.exit(1)

ssl._create_default_https_context = ssl._create_unverified_context  # work around certification

src = sys.argv[1]
dst = sys.argv[2]

if validators.url(src):
  urllib.request.urlretrieve(src, dst)
elif os.path.isfile(src):
  os.symlink(src, dst)
else:
  raise ValueError("Unidentified src type: {0}".format(sys.argv[1]))

