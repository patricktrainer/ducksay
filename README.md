# :duck: ducksay


`ducksay` prints a duck and a message to the terminal. It is inspired by `cowsay`. 

### How to install

```
git clone git@github.com:patricktrainer/ducksay.git
cd ducksay
pip install -e .
```

### How to use

Simply pipe any string to `ducksay`.
```bash
$ echo "quack!" | ducksay
```

You can pipe duckdb results to `ducksay`!

```bash
$ duckdb :memory: "select 'quack!' as msg" | ducksay

┌─────────┐
│   msg   │
│ varchar │
├─────────┤
│ quack!  │
└─────────┘
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
```
