import socket
import urllib.parse
import utils

def _whois(host):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("whois.iana.org", 43,))
  s.send(bytes(host + "\r\n", encoding="utf-8"))

  done = False
  res = []
  while (not done):
    res.append(s.recv(256))
    if (res[-1] == b''):
      done = True

  res = b''.join(res)
  return res.decode("utf-8")

# scan sites in web server
def reverse_ip(website):
  host = socket.gethostbyname(website)
  res = socket.gethostbyaddr(host)
  a = lambda: utils.print_color(utils.RED, "[*] ")
  
  for i in res:
    if isinstance(i, str):
      print(utils.RED + "[*] " + utils.BLUE + i)

  return

# whois query
# TODO tidy-up the code
def whois(website):
  if (not website.startswith("http")):
    website = "http://" + website

  host = urllib.parse.urlparse(website).netloc.split(":")[0]
  res = _whois(host)

  res = res.splitlines()
  res2 = []
  for i in res:
    if not i.startswith('%') and not i.strip() == "":
      res2.append(i)

  res = res2
  for i in res:
    i = i.split(":")
    print(utils.RED + i[0].strip() + utils.BLUE + " -> " + utils.GREEN +
          i[1].strip())
  
  return

# dns scan
def dns_scan(website):
  # not implemented
  return

def scriptcheck(website):
  pass

def wpscan(website):
  pass
