

class Contact:
    def __int__(self, name='Noname', surname='Nosurname', cell_number='0-000-000-00-00'):
        self.name = name
        self.surname = surname
        self.cell_number = cell_number

    def __str__(self):
        return self.name

    def check_valid_data(self):
        pass

    def get_contact_value(self):
        return [self.name, self.surname, self.cell_number]
