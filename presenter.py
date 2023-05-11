from modelts import articles
def createArticle():
    article = {
        "title": input("Ввведіть назву товару:"),
        "descriptin": input("Ввведіть опис товару:"),
        "number": input("Ввведіть кількість товару:"),
        "price": input("Ввведіть ціну товару:")
    }
    return article

def workNumber():
    number = input("Введіть номер статті:")
    if number.isdigit() and 0 < int(number) <= len(articles):
        number = int(number) - 1
        return number

def workMenu():
	number = workNumber()
	if number not in None:
		while True:
			choice = input("Редагування-1,Читання-2,Видалення-3,Вихід-4:")
			if choice == "1":
				articles[number] = createArticle()
			elif choice == "2":
				print(articles[number])
			elif choice == "3":
				articles.pop(number)
			elif choice == "4":
				break
