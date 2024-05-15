def hello(name, lang):
    greetings={
        "English": "Hello",
        "German": "Hallo",
        "Spanish": "Hola"
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == '__main__' :
    import argparse
    print("Entered")
    parser = argparse.ArgumentParser(
        description="Provides personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Name of the person to greet" 
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English","Spanish","German"],
        help= "Language for greetings."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
