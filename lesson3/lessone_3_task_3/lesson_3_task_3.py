from address import Address
from mailing import Mailing

to_address = Address ("23456", "Нижний Новгород", "Ленина", "12", "10")
from_address = Address("65432", "Москва", "Гоголя", "4", "11")
mailing = Mailing(to_address, from_address, 300,"test123")

print(f"Отправление {mailing.track} из {mailing.frome_address.index}, {mailing.frome_address.city},"
      f" {mailing.frome_address.street}, {mailing.frome_address.house} - {mailing.frome_address.apartment} "
      f" в {mailing.to_address.index},{mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")