class SearchOption:
    def search(self, query):
        pass

class NameSearch(SearchOption):
    def search(self, query):
        results = []
        for d in data:
            if query in d['name']:
                results.append(d)
        return results

class CategorySearch(SearchOption):
    def search(self, query):
        results = []
        for d in data:
            if query == d['category']:
                results.append(d)
        return results

class Database:
    def __init__(self, data):
        self.data = data

    def search(self, search_option, query):
        return search_option.search(query)

data = [
    {'id': 1, 'name': 'John', 'category': 'A'},
    {'id': 2, 'name': 'Jane', 'category': 'B'},
    {'id': 3, 'name': 'Bob', 'category': 'A'},
    {'id': 4, 'name': 'Alice', 'category': 'C'}
]

db = Database(data)

name_search = NameSearch()
result = db.search(name_search, 'John')
print(result)

category_search = CategorySearch()
result = db.search(category_search, 'A')
print(result)
