class Article:
    all = []
    def __init__(self, author, magazine, title):

        if not isinstance(title, str):
            raise TypeError("Title must be of type string")

        if not (5 <= len(title) <=50 ):
            raise ValueError("Title must be between 5 and 50 characters")
        
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(value, "_title"):
            raise AttributeError("Can not set the title after instantiation")
        self._title = value
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type string")
        if (len(name) == 0):
            raise ValueError("Name must be longer than 0 characters")
        
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("Can not set the author's name after instantation")

        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list ({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        if new_article not in Article.all:
            Article.all.append(new_article)
        return new_article

    def topic_areas(self):
        topics = [magazine.category for magazine in self.magazines()]
        return topics if topics else None

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be of type string")
        if not(2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("Category must be of type string")
        if (len(category) == 0):
            raise ValueError("Category must be longer than 0 characters")

        self._name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")

        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be of type string")
        if (len(value) == 0):
            raise ValueError("Category must be longer than 0 characters")
        
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list ({article.author for article in self.articles()})

    def article_titles(self):
        titlelist = [article.title for article in self.articles()]
        return titlelist if titlelist else None
    def contributing_authors(self):
        author_article_counts = {}

        for article in self.articles():
            author = article.author
            if author not in author_article_counts:
                author_article_counts[author] = 0
            author_article_counts[author] += 1

        contributing_author_list = [author for author, count in author_article_counts.items() if count > 2]
        return contributing_author_list if contributing_author_list else None