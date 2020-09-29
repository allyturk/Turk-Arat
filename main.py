#!/usr/bin/env python3

import colorama, time, argparse # required modules
import utils # utilities
from net import reverse_ip, whois, dns_scan, wpscan, scriptcheck

VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION_RC    = 0

VERSION_NO = "{}.{}-rc{}".format(VERSION_MAJOR, VERSION_MINOR, VERSION_RC)

def _(s):
  return s # TODO: implement i18n, l10n

def main(args):
  if args.reverse_ip:
    reverse_ip(args.reverse_ip)
  elif args.whois:
    whois(args.whois)
  elif args.dns:
    dns_scan(args.dns)
  elif args.wpscan:
    wpscan(args.wpscan)
  elif args.script:
    scriptcheck(args.script)
  elif args.list_tools:
    utils.print_color(utils.RED, "[*] Kullanılabilir araçlar:")
    utils.print_color(utils.BLUE, """
    1- Reverse IP taraması
    2- WHOIS sorgusu
    3- DNS taraması
    4- Wordpress taraması
    5- Hazır script tanıma
""")
  else:
    utils.print_banner()
    utils.print_color(utils.RED, _("hata: seçenek belirtilmedi") + "\n")
  return

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-r", "--reverse-ip", help=_("Reverse IP lookup"))
  parser.add_argument("-w", "--whois", help=_("Bir sitenin WHOIS sorgulaması"))
  parser.add_argument("-d", "--dns", help=_("Bir sitenin DNS sorgusu"))
  parser.add_argument("-s", "--script",
                      help=_("Sayfada hazır script tanımlaması yap"))
  parser.add_argument("-W", "--wpscan", 
                      help=_("Wordpress hakkında bilgi topla"))
  parser.add_argument("-V", "--version", action="version",
                      version="%(prog)s {}".format(VERSION_NO))
  parser.add_argument("-l", "--list-tools", help=_("Araçları listele"),
                      action="store_true")

  args = parser.parse_args()
  main(args)
