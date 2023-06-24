import json
from abc import ABC, abstractmethod
from work_with_vacancy import Vacancy


class FileSaver(ABC):
    """
    Абстрактный класс для добавления, получения
    и удаления вакансий в файл
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(FileSaver):
    """
    Класс для добавления, получения
    и удаления вакансий в файл формата json
    """

    def __init__(self):
        pass

    def add_vacancy(self, vacancy):
        """Добавление вакансий в файл"""
        try:
            with open('data.json', 'r', encoding='UTF-8') as file:
                current_file = json.load(file)
        except FileNotFoundError:
            current_file = {}

        with open('data.json', 'w', encoding='UTF-8') as file:
            current_file[f'{vacancy.prefix}_{vacancy.id}'] = vacancy.json_format
            json.dump(current_file, file, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        """Получение вакансий из файла"""
        try:
            with open('data.json', 'r', encoding='UTF-8') as file:
                current_file = json.load(file)
        except FileNotFoundError:
            return []

        result = []
        for raw_vacancy in current_file.values():
            vacancy = Vacancy(**raw_vacancy)
            result.append(vacancy)

        return result

    def delete_vacancy(self, vacancy):
        """Удаление вакансии из файла"""
        try:
            with open('data.json', 'r', encoding='UTF-8') as file:
                current_file = json.load(file)
        except FileNotFoundError:
            return

        key = f'{vacancy.prefix}_{vacancy.id}'

        if key in current_file:
            del current_file[key]

        with open('data.json', 'w', encoding='UTF-8') as file:
            json.dump(current_file, file, ensure_ascii=False, indent=4)



