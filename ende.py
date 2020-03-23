#!/usr/bin/python3

from key_generator import new_key_generator
from algorithm import encryption,decryption
import sys
import pyperclip

class colors:
     HEADER = '\033[95m'
     OKBLUE = '\033[94m'
     LIGHT = '\033[2m'
     OKGREEN = '\033[92m'
     WARNING = '\033[93m'
     FAIL = '\033[91m'
     ENDC = '\033[0m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'

about = """
       ... In The Name Of Allah ...

   Programmer : Mohammad Sadegh Mirnasab
   Email : Mr.Mirnasab@gmail.com
   github ID : Rekcaha
   Project Link : https://github.com/RekcahA/ende
"""

error = """"""

help = colors.ENDC + """
Usage: ende [option] [input]

Options:

  -e, --encrypt ++       Encrypt your text

  -d, --decrypt ++       Decrypt your encrypted text
                         ** Make sure your encryption dictionary is right

  -p, --probability ++   Show Error probability percent
                         ** By reciving length of data

  -n, --new              Create a new encryption dictionary
                         ** You won't able to decrypt last encrypted text

  -fe, --file_enc ++     Encrypt a txt file -----|
  -fd, --file_dec ++     Decrypt a txt file --|  |
                                              |  |
                         ** Just write file name as input


  -h, --help             Show basic help message
  -m, --more             Show Advance help message
  -v, --version          Show program's version number
  -a, --about            Know who create this program


    *** Those options that marked by ++ needs an input ***
"""

logo = """
     #-------------------------->>>>#
     E                              D
     n      EnDe  v1.3 #Beta        e
     c                              c
     r      <--- RekcahA --->       r
     y                              y
     p    A PowerFul Encryptor      p
     t                              t
     #<<<<--------------------------#

"""

print(colors.OKBLUE + logo)

def router(user_data):

    result = 'noting'

    if len(sys.argv) > 3 :

        print(colors.FAIL + "[ERROR]",colors.LIGHT + """Write your text between two Quotation ** Ex: "Hello World!". """)
        result = error

    else :
       if user_data == "-e" or user_data == "--encrypt"  and len(sys.argv) == 3   :
           try:
               result = encryption(sys.argv[2])
           except:

               print(colors.FAIL + "[ERROR]",colors.LIGHT + "Please be sure that you entered enough inputs not more not less.")
               result = error

       if user_data == "-d" or user_data == "--decrypt"   and len(sys.argv) == 3  :
           try:

               a = sys.argv[3]
               print(colors.FAIL + "[ERROR]",colors.LIGHT + """Write your text between two Quotation ** Ex: "pws#V1dooV1os". """)
               result = error

           except:

               try: result = decryption(sys.argv[2])
               except:

                   print(colors.FAIL + "[ERROR]",colors.LIGHT + "Make sure your encryption dictionary is right")
                   result = error

       if user_data == "-n" or user_data == "--new"       and len(sys.argv) == 2  :
           new_key_generator()
           result = "Keys Changed! You won't able to decrypt last encrypted text."

       if user_data == "-m" or user_data == "--more"      and len(sys.argv) == 2  : result = "Open github link : https://github.com/RekcahA/ende"

       if user_data == "-v" or user_data == "--version"   and len(sys.argv) == 2  : result = "Ende v1.3.3 #Beta #GNU/Linux #debian"

       if user_data == "-a" or user_data == "--about"     and len(sys.argv) == 2  : result = about

       if user_data == "-h" or user_data == "--help"      and len(sys.argv) == 2  : result = help

    if result == 'noting': print(colors.FAIL + "[ERROR]",colors.LIGHT + "Your option is not right. To see help message use -h, --help option.")

    return result


if len(sys.argv) == 1 :
    print(colors.ENDC + """
Usage: ende [option] [input]

   Use -h, --help option to see help message...""")


if len(sys.argv) > 1 :

    out = router(sys.argv[1])
    if out != 'noting' : print(colors.WARNING + out)
    # Copy final output into your cilpboard
    pyperclip.copy(out)

print('\n')
