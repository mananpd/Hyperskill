class Formatter:

    def __init__(self):
        self.text = ""
        self.formats = {'plain': self.plain,
                        'bold': self.bold,
                        'italic': self.italic,
                        'header': self.header,
                        'link': self.link,
                        'inline-code': self.inline_code,
                        'new-line': self.new_line,
                        'unordered-list': self.unordered,
                        'ordered-list': self.ordered}

    def plain(self):
        self.text = self.text + input("Text: ")
        print(self.text)

    def bold(self):
        self.text = self.text + "**" + input("Text: ") + "**"
        print(self.text)

    def italic(self):
        self.text = self.text + "*" + input("Text: ") + "*"
        print(self.text)

    def header(self):
        while True:
            level = int(input("Level: "))
            if not 0 < level < 7:
                print("The level should be within the range of 1 to 6")
                continue
            else:
                break
        self.text = self.text + ("#" * level) + " " + input("Text: ") + "\n"
        print(self.text)

    def link(self):
        label = input("Label: ")
        url = input("URL: ")
        self.text = self.text + f"[{label}]({url})"
        print(self.text)

    def inline_code(self):
        self.text = self.text + "`" + input("Text: ") + "`"
        print(self.text)

    def new_line(self):
        self.text = self.text + "\n"
        print(self.text)

    def ordered(self):
        while True:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            else:
                print("The number of rows should be greater than zero")
        for i in range(rows):
            self.text = self.text + f'{i + 1}. ' + input(f'Row #{i + 1}: ') + '\n'
        print(self.text)

    def unordered(self):
        while True:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            else:
                print("The number of rows should be greater than zero")
        list_elements = []
        for i in range(rows):
            self.text = self.text + f'* ' + input(f'Row #{i + 1}: ') + '\n'
        print(self.text)

    def choose(self):
        command = input("Choose a formatter: ")
        if command == '!help':
            print("Available formatters: plain bold italic header link inline-code new-line")
            print("Special commands: !help !done")
        elif command == "!done":
            with open("output.md", "w") as file:
                file.write(self.text)
            exit()
        elif command not in self.formats:
            print("Unknown formatting type or command")
        else:
            self.formats[command]()

    def main(self):
        while True:
            self.choose()


formatter = Formatter()
formatter.main()
