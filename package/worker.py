from package.work_with_vacancy import Vacancy


class VacancyWorker:
    """Класс для фильтрации и сортировки списка вакансий"""

    def __init__(self, vacancies: list[Vacancy]):
        self.__vacancies = vacancies

    @property
    def vacancies(self):
        return self.__vacancies

    @vacancies.setter
    def vacancies(self, x):
        self.__vacancies = x
        print(f'Получилось {len(x)} вакансий')

    def filter_by_area(self, area):
        """Фильтрация вакансий по городу"""

        new_vacancies = []
        for vacancy in self.vacancies:
            if vacancy.area == area:
                new_vacancies.append(vacancy)

        self.vacancies = new_vacancies
        return self

    def filter_by_middle_salary(self, middle_salary):
        """Фильтрация вакансий по средней зарплате"""

        new_vacancies = []
        for vacancy in self.vacancies:
            if vacancy.middle_salary >= middle_salary:
                new_vacancies.append(vacancy)

        self.vacancies = new_vacancies
        return self

    def filter_by_description(self, keyword):
        """Фильтрация вакансий по ключевым словам из описания"""

        new_vacancies = []
        for vacancy in self.vacancies:
            if keyword in vacancy.description:
                new_vacancies.append(vacancy)
        self.vacancies = new_vacancies
        return self

    def sort_vacancies(self, inverse):
        """Сортировка вакансий по средней зарплате"""

        if inverse is True:
            self.vacancies.sort(key=lambda vacancy: vacancy.middle_salary)
        else:
            self.vacancies.sort(key=lambda vacancy: vacancy.middle_salary * -1)

    def get_top_vacancies(self, top_number):
        """Вывод топ-N вакансий"""

        return self.vacancies[:top_number]

