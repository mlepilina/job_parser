
class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, name, url, salary_from, salary_to, description, area, prefix, id):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.area = area
        self.prefix = prefix
        self.id = id

    def __repr__(self):
        return f'{self.name} {self.url} {self.salary_from} {self.salary_to} {self.description} {self.area} {self.prefix} {self.id}'

    def __str__(self):
        return f'{self.name} {self.url} {self.salary_from} {self.salary_to} {self.description} {self.area} {self.prefix} {self.id}'

    def __gt__(self, other):
        """Сравнение средней зарплаты (больше)"""
        return self.middle_salary > other.middle_salary

    def __lt__(self, other):
        """Сравнение средней зарплаты (меньше)"""
        return self.middle_salary < other.middle_salary

    @property
    def middle_salary(self):
        """Метод, возвращающий среднюю зарплату"""
        if self.salary_from and self.salary_to:
            middle_salary = (self.salary_from + self.salary_to) // 2
            return middle_salary
        return self.salary_to or self.salary_from

    @property
    def json_format(self):
        """Метод, возвращающий данные по вакансии в формате json"""
        return {
            'name': self.name,
            'url': self.url,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'description': self.description,
            'area': self.area,
            'prefix': self.prefix,
            'id': self.id
        }

