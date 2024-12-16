from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Create the author, magazine, and article using the models
    author = Author(author_name)  # Author is created, no need to manually insert into the DB
    magazine = Magazine(magazine_name, magazine_category)  # Magazine is created, no need to manually insert into the DB
    article = Article(author, magazine, article_title)  # Article is created and inserted into the DB

    # Display results
    print("\nAuthor Details:")
    print(f"ID: {author.id}, Name: {author.name}")

    print("\nMagazine Details:")
    print(f"ID: {magazine.id}, Name: {magazine.name}, Category: {magazine.category}")

    print("\nArticle Details:")
    print(f"ID: {article.id}, Title: {article.title}, Author: {article.author.name}, Magazine: {article.magazine.name}")

if __name__ == "__main__":
    main()
