import os
import sys
import hashlib


class DuplicateFileHandler:
    def __init__(self):
        self.file_type = None
        self.args = sys.argv
        self.root_dir = None
        self.sorting = None
        self.size_file_dict = None
        self.duplicate_check = None
        self.size_hash_file_dict = None
        self.files_to_delete = None
        self.num_file = None
        self.main()

    def check_args(self):
        if len(self.args) == 1:
            print("Directory is not specified")
            exit()
        else:
            self.root_dir = self.args[1]

    def enter_file_type(self):
        print("Enter file format:")
        self.file_type = "." + input()
        print()

    def sorting_options(self):
        print("Size sorting options:")
        print("1. Descending")
        print("2. Ascending")
        while True:
            print()
            print("Enter a sorting option:")
            self.sorting = int(input())
            if self.sorting > 2 or self.sorting < 1:
                print("Wrong option")
            else:
                break

    def get_file_size(self):
        file_size_dic = {}
        for root, _, files in os.walk(self.root_dir):
            for name in files:
                if self.file_type == "." or self.file_type == ". ":
                    size = os.path.getsize(root + "/" + name)
                    file = os.path.join(root, name)
                    if file_size_dic.get(size) is None:
                        file_size_dic.update({size: [file]})
                    else:
                        file_size_dic.update({size: [*file_size_dic.get(size), file]})
                elif self.file_type in os.path.splitext(name):
                    size = os.path.getsize(root + "/" + name)
                    file = os.path.join(root, name)
                    if file_size_dic.get(size) is None:
                        file_size_dic.update({size: [file]})
                    else:
                        file_size_dic.update({size: [*file_size_dic.get(size), file]})
        self.size_file_dict = file_size_dic

    def print_files(self):
        sizes = list(self.size_file_dict.keys())
        if self.sorting == 1:
            sizes = sorted(sizes, reverse=True)
        elif self.sorting == 2:
            sizes = sorted(sizes)
        for size in sizes:
            print()
            print(str(size) + " bytes")
            for file in self.size_file_dict.get(size):
                print(file)

    def ask_duplicates(self):
        print()
        print("Check for duplicates?")
        while True:
            answer = input()
            if answer == "yes":
                self.duplicate_check = answer
                break
            elif answer == "no":
                exit()
            else:
                print("Wrong option")

    def get_hash(self):
        sizes = list(self.size_file_dict.keys())
        if self.sorting == 1:
            sizes = sorted(sizes, reverse=True)
        elif self.sorting == 2:
            sizes = sorted(sizes)
        size_hash_file_dic = {}
        for size in sizes:
            for file in self.size_file_dict.get(size):
                with open(file, 'rb') as file_rb:
                    file_hash = hashlib.md5(file_rb.read()).hexdigest()
                    if size_hash_file_dic.get(size) is None:
                        hash_file = {file_hash: [file]}
                        size_hash_file_dic.update({size: hash_file})
                    elif size_hash_file_dic.get(size).get(file_hash) is None:
                        size_hash_file_dic.get(size).update({file_hash: [file]})
                    else:
                        size_hash_file = [*size_hash_file_dic.get(size).get(file_hash), file]
                        size_hash_file_dic.get(size).update({file_hash: size_hash_file})

        self.size_hash_file_dict = size_hash_file_dic

    def print_hash(self):
        sizes = list(self.size_file_dict.keys())
        if self.sorting == 1:
            sizes = sorted(sizes, reverse=True)
        elif self.sorting == 2:
            sizes = sorted(sizes)
        counter = 1
        num_file = {}
        for size in sizes:
            print()
            print(str(size) + " bytes")
            for hash_value in self.size_hash_file_dict.get(size):
                if len(self.size_hash_file_dict.get(size).get(hash_value)) > 1:
                    print(f'Hash: {hash_value}')
                    for file in self.size_hash_file_dict.get(size).get(hash_value):
                        print(f'{counter}. {file}')
                        num_file.update({counter: file})
                        counter += 1
        self.num_file = num_file

    def ask_delete_file(self):
        print()
        print("Delete files?")
        while True:
            delete_files = input()
            if delete_files == "yes":
                break
            elif delete_files == "no":
                exit()
            else:
                print()
                print("Wrong option")
        print()
        while True:
            try:
                print("Enter file numbers to delete:")
                self.files_to_delete = [int(x) for x in input().split()]
                if len(self.files_to_delete) == 0:
                    print()
                    print("Wrong format")
                    continue
                for value in self.files_to_delete:
                    if value > len(self.num_file.keys()):
                        print()
                        print("Wrong format")
                        continue
                break
            except ValueError:
                print()
                print("Wrong format")

    def delete_files(self):
        freed_space = 0
        for value in self.files_to_delete:
            file = self.num_file.get(value)
            freed_space += os.path.getsize(file)
            os.remove(file)
        print(f"Total freed up space: {freed_space} bytes")

    def main(self):
        self.check_args()
        self.enter_file_type()
        self.sorting_options()
        self.get_file_size()
        self.print_files()
        self.ask_duplicates()
        self.get_hash()
        self.print_hash()
        self.ask_delete_file()
        self.delete_files()


DuplicateFileHandler()
