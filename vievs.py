from modelts import articles
from presenter import createArticle,workNumber,workMenu



while True:
    choice = input("1 створити товар,2 переглянути товари,3 робота,4 вийти:")
    if choice == "1":
        article = createArticle()
        articles.append(article)
    elif choice == "2":
       print(articles)
    elif choice == "4":
        break
    elif choice == "3":
        workNumber()
        workMenu()
       



