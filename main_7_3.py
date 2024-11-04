class WordsFinder:
    def __init__(self, *args): #'file1.txt, file2.txt', 'file3.txt', ...
        self.file_names = ()
        for x in args:
            self.file_names += (x,)
        self.all_words = {}

    def get_all_words(self):
        excepted = (',', '.', '=', '!', '?', ';', ':', ' - ')
        for file_name in self.file_names:
            with  open(file_name, encoding='utf-8') as file:
                file_new = file.read()
                arr = []
                for ex in excepted:
                    if not file_new.find(ex) == -1:
                        file_new = file_new.replace(ex, '')
                arr.extend(file_new.lower().split())
                self.all_words.update({file_name: arr})
        return self.all_words

    def find(self, word):
        dic = {}
        for elem in self.all_words.items():
            for i, item in enumerate(elem[1]):
                if item == word.lower():
                    dic.update({elem[0] : i + 1})
                    break #забыл сначала, поэтому показал номер последнего слова и почему словарь при этом не
                    # размножился? Догадываюсь, что из-за нахождения в цикле, но всё же
        return dic

    def count(self, word):
        dic = {}
        for elem in self.all_words.items():
            counter = 0
            for item in elem[1]:
                if item == word.lower():
                    counter += 1
            dic.update({elem[0]: counter})
        return dic

my_finder = WordsFinder('test_file.txt', 'test_file2.txt') #второй файл сделал просто 'text text text'
print(my_finder.get_all_words())
print(my_finder.find('TEXT')) #{'test_file.txt': 3, 'test_file2.txt': 1}
print(my_finder.count('teXT')) #{'test_file.txt': 4, 'test_file2.txt': 3}