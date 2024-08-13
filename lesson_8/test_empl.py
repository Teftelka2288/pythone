from empl import Company


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "Tim"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = "Tim"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Tim1234", "M")
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "Tim1234"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "M"


def test_get_employee_by_id():
    name = "Tim"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Tim1", "Ml")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Tim34"
    assert get_info["lastName"] == "M12"


def test_change_employee_info():
    name = "Tim1"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Tim12", "Mak")
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "mak", "test1@mail.ru")
    assert update["id"] == id_employee
    assert update["email"] == "tes12@mail.ru"
    assert update["isActive"] == True