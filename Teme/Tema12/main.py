'''1. Implementarea unei aplicatii de gestionare a unui abonament de streaming. Avand implementarea clasei
 StreamingService, implementati:
 - o clasa BankAccount (owner: str, iban: str, balance: int default 0) cu functii specifice unui cont
 (deposit, withdraw, show_balance)
 - o clasa StreamingServicePaymentProxy (provider: str, subscription_price: int, subscription_expiration_date:
 datetime, account: BankAccount) care sa implementeze un design pattern potrivit si sa faca handling asupra abonamentului,
 permitand vizualizarea unui show numai in cazul in care abonamentul este inca activ sau, in caz contrar, daca in contul
 bancar mai sunt suficiente fonduri pentru a finanta inca o luna (caz in care se retrage suma din cont si se prelungeste
 abonamentul cu 30 de zile)
 - o clasa AuthorizedAccount (authorized_person: BankAccount, observable: BankAccount) care sa implementeze un design pattern
 potrivit pentru a desemna o persoana imputernicita asupra contului bancar, aceasta fiind notificata asupra oricarei operatiuni
  de retragere sau depunere de bani din cont cu un mesaj sugestiv, de ex: ">Notification from account nr <....>
  (owner <....>): <mesajul tranzactiei>"

Pasi sugerati pentru testarea programului:
 1) instantierea unui BankAccount (preferabil cu 0 lei)
 2) instantierea unui BankAccount de imputernicit
 3) instantierea unui AuthorizedAccount al imputernicit catre contul initial
 4) instantierea unui StreamingServicePaymentProxy legat la primul cont (preferabil cu abonamentul expirat)
 5) apel catre watching_a_show(show_name) (daca abonamentul e expirat si contul nu are bani, ar trebui sa va afiseze un mesaj
 sugestiv)
 6) depunere bani in cont (pe langa depunerea in sine, persoana imputernicita ar trebui sa primeasca un mesaj de notificare
 despre operatiune)
 7) apel catre watching_a_show (pe langa mesajul despre show-ul urmarit, acum ar trebui sa primim un mesaj de succes cu privire
  la tranzactia din cont si unul cu privire la actualizarea abonamentului, cat si unul cu notificarea imputernicitului)
'''

from datetime import datetime, timedelta


class StreamingService:
    def __init__(self, provider):
        self.provider = provider

    def watching_a_show(self, show):
        print(f"You are now watching {show} on {self.provider}")


class BankAccount:
    def __init__(self, owner, iban, balance=0):
        self.owner = owner
        self.iban = iban
        self.balance = balance
        self._observers = []

    def __str__(self):
        return f"{self.owner}, at date&time: {datetime.now().isoformat()} you have in your account nr {self.iban} the amount: {self.balance}RON"

    def show_balance(self):
        print(self.__str__())

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

            message = f"Transaction succeeded: {amount}RON has been withdrawn from your account."
            print(message)
            self.notify_observers(message)

            return True

        else:
            message = f"Transaction failed: Insufficient funds."
            print(message)
            self.notify_observers(message)

            return False

    def deposit(self, amount):
        self.balance += amount

        message = f"Transaction succeeded: {amount}RON has been deposited into your account."
        print(message)
        self.notify_observers(message)

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for obs in self._observers:
            obs.notify(self, message)


class StreamingServicePaymentProxy:
    def __init__(self, provider, subscription_price, expiration_date, account):
        self.streaming_service = StreamingService(provider)
        self.subscription_price = subscription_price
        self.subscription_expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        self.account = account

    def watching_a_show(self, show):
        if self.subscription_expiration_date > datetime.now():
            self.streaming_service.watching_a_show(show)
        else:
            if self.account.withdraw(self.subscription_price):
                self.subscription_expiration_date += timedelta(days=30)
                print(
                    f"Your subscription have been updated. New expiration date is: {self.subscription_expiration_date}")
                self.streaming_service.watching_a_show(show)
            else:
                print(
                    f"Your subscription expired and you dont have sufficient funds. Please fund your account and try again..")


class AuthorizedAccount:
    def __init__(self, authorized_person, observable):
        self.authorized_person = authorized_person
        observable.register_observer(self)

    def notify(self, observable, message):
        print(f">Notification from account nr {observable.iban} (owner {observable.owner}): {message}")


gheorghitza = BankAccount("Gheorghitza", "RORON1234WXYZ")
gheorghitza.show_balance()

ionel = BankAccount("Ionel", "RORON1111AAAA", 5000)
authorized_account = AuthorizedAccount(ionel, gheorghitza)

streaming_service = StreamingServicePaymentProxy("Netflix", 60, "2022-10-20", gheorghitza)
streaming_service.watching_a_show("Peaky Blinders")

gheorghitza.deposit(1000)
gheorghitza.show_balance()

streaming_service.watching_a_show("Peaky Blinders")
