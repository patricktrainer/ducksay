import sys


def print_duck(message):
    """prints duck ascii art to stdout"""
    duck = r"""
    \
     \
      \       _.-.
         __.-' ,  \
        '--'-'._   \
                '.  \
                 )-- \ __.--._
                /   .'        '--.
               .               _/-._
               :       ____._/   _-'
               '._          _.'-'
                  '-._    _.'
                      \_|/
                     __|||
                     >__/'
    """
    print(message, duck, sep='\n')


def main():
    msg = sys.stdin.read()
    print_duck(msg.strip())


if __name__ == '__main__':
    main()
