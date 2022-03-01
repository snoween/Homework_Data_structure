class Book:
    'Showing the information of the book'
    
    #Create the constructor with 4 variables
    def __init__(self, 書名, 作者, 出版社, 年份):
        self.書名 = 書名
        self.作者 = 作者
        self.出版社 = 出版社
        self.年份 = 年份
    
    #Display the information of the book
    def info(self):
        return ('書名:{}\n作者:{}\n出版社:{}\n年份:{}'.format(self.書名, self.作者, self.出版社, self.年份))