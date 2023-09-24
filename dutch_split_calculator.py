class Person:
    def __init__(self, name):
        self.name = name


class People:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def count_people(self):
        return len(self.people)


class Transaction:
    def __init__(self, person, amount, desc):
        self.person = person
        self.amount = amount
        self.desc = desc


class Transactions:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_total_amount(self):
        return sum(i.amount for i in self.transactions)

    def get_total_amount_by_person(self, person):
        return sum(i.amount for i in self.transactions if i.person == person)

def main():
    yoichi = Person(name = "yoichi")
    tuuri = Person(name = "tuuri")
    hosshi = Person(name = "hosshi")
    yan = Person(name = "yan")
    drew = Person(name = "drew")

    people = People()
    people.add_person(yoichi)
    people.add_person(tuuri)
    people.add_person(hosshi)
    people.add_person(yan)
    people.add_person(drew)

    lunch = Transaction(person = yoichi, amount = 1200, desc = "lunch")
    dinner = Transaction(person = tuuri, amount = 2400, desc = "dinner")
    movie = Transaction(person = yan, amount = 9800, desc = "movie")

    transactions = Transactions()
    transactions.add_transaction(lunch)
    transactions.add_transaction(dinner)
    transactions.add_transaction(movie)

    total_amount = transactions.get_total_amount()
    print(total_amount)

    amount_by_people = {}
    for p in people.people:
        amount_by_people[p.name] = transactions.get_total_amount_by_person(p)

    print(amount_by_people)


    people_count = people.count_people()
    amount_per_person = total_amount / people_count
    print(amount_per_person)

    amount_to_pay = {}
    for p in people.people:
        amount_to_pay[p.name] = amount_per_person - transactions.get_total_amount_by_person(p)

    print(amount_to_pay)

    print(sum(amount_to_pay[i] for i in amount_to_pay))


if __name__ == "__main__":
    main()