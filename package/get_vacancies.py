from abc import ABC, abstractmethod
import requests
from work_with_vacancy import Vacancy


class PlatformsAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_vacancies(self, keyword, count, page) -> list[Vacancy]:
        """
        Получение вакансий.

        :keyword - это поисковое ключевое слово
        :count - это кол-во элементов на странице
        :page - это номер страницы
        """


class HeadHunterAPI(PlatformsAPI):
    """
    Получение вакансий с по ключевому слову с сайта hh.ru
    Возвращение списка вакансий (списка экземпляров класса
    Vacancy)
    """

    def __init__(self):
        self.api_url = 'https://api.hh.ru'

    def get_vacancies(self, keyword, count=20, page=0):
        url = self.api_url + '/vacancies'
        params = {"per_page": count, "page": page, "text": keyword, "search_field": 'name'}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return []

        data = response.json()
        vacancies = []
        for vacancy in data['items']:

            description = vacancy['snippet']['responsibility']

            if vacancy['salary']:
                salary_from = vacancy['salary'].get('from') or 0
                salary_to = vacancy['salary'].get('to') or 0
            else:
                salary_from = 0
                salary_to = 0

            vacancies.append(
                Vacancy(
                    name=vacancy['name'],
                    url=vacancy['alternate_url'],
                    salary_from=salary_from,
                    salary_to=salary_to,
                    description=description,
                    area=vacancy['area']['name'],
                    prefix='hh',
                    id=vacancy['id']
                )
            )

        return vacancies


class SuperJobAPI(PlatformsAPI):
    """
    Получение вакансий с по ключевому слову с сайта superjob.ru
    Возвращение списка вакансий (списка экземпляров класса
    Vacancy)
    """

    def __init__(self):
        self.api_url = 'https://api.superjob.ru/2.0'
        self.headers = {"X-Api-App-Id": 'v3.r.137611194.30ada7f300d5c46ab60cacd6cf5d9390d504d0bb.eedfe8c9810e6ff07c98f616aa941ecf7e997013'}

    def get_vacancies(self, keyword, count=20, page=0):
        url = self.api_url + '/vacancies'
        params = {"count": count, "page": page, "keyword": keyword, "archive": False}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            return []

        data = response.json()
        vacancies = []
        for vacancy in data['objects']:

            vacancies.append(
                Vacancy(
                    name=vacancy['profession'],
                    url=vacancy['link'],
                    salary_from=vacancy['payment_from'],
                    salary_to=vacancy['payment_to'],
                    description=vacancy['candidat'],
                    area=vacancy['town']['title'],
                    prefix='sj',
                    id=vacancy['id']
                )
            )

        return vacancies

