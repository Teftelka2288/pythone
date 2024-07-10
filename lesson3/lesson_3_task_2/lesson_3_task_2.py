from smartpfone import Smartpfone
catalog = []
phone1 = Smartpfone("Xiaomi", "Mi 14", "+79961583694")
phone2 = Smartpfone("Xiaomi", "Redmi 12 Pro", "+79967568547")
phone3 = Smartpfone("Xiaomi", "Redmi 4A", "+77785632586")
phone4 = Smartpfone("Xiaomi", "12x", "+79520251225")
phone5 = Smartpfone("Xiaomi", "Redmi 9T", "+79964567893")
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}" )