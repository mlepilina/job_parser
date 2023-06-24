from get_vacancies import HeadHunterAPI, SuperJobAPI
from package.work_with_file import JSONSaver
from package.worker import VacancyWorker


def parsing_vacancies(parser: HeadHunterAPI | SuperJobAPI, keyword: str) -> None:
    """Функция, которая парсит вакансии с сайта по ключевому слову и сохраняет в файл json"""
    vacancies = parser.get_vacancies(keyword=keyword, count=100)
    for vacancy in vacancies:
        json_saver = JSONSaver()
        json_saver.add_vacancy(vacancy)


def ask_questions(question_1, question_2) -> str | None:
    """
    Функция, взаимодействующая с пользователем,
    задает вопросы о необходимости фильтрации и сортировки вакансий
    """

    answer = input(f'{question_1} (введите да/нет) \n')
    while answer.lower() not in ['да', 'yes', 'нет', 'no']:
        answer = input('Введено некорректное значение. Введите "да" или "нет" \n')

    if answer.lower() in ['нет', 'no']:
        return
    answer = input(f'{question_2} \n')
    while not answer:
        answer = input(f'{question_2} \n')

    return answer


def main():
    platform_answer = input('С какой платформы вы хотите получить вакансии?\n'
                            'HeadHunter - введите 1,\n'
                            'SuperJob - введите 2,\n'
                            'и HeadHunter, и SuperJob - введите 3\n')

    while platform_answer not in ['1', '2', '3']:
        platform_answer = input('Введено некорректное значение. Введите данные числом от 1 до 3.\n')

    keyword_answer = input('По какому ключевому слову вести поиск вакансии?\n')

    while not keyword_answer:
        keyword_answer = input('По какому ключевому слову вести поиск вакансии?\n')

    if platform_answer == '1':
        parsing_vacancies(HeadHunterAPI(), keyword_answer)
    elif platform_answer == '2':
        parsing_vacancies(SuperJobAPI(), keyword_answer)
    else:
        parsing_vacancies(HeadHunterAPI(), keyword_answer)
        parsing_vacancies(SuperJobAPI(), keyword_answer)

    print('Найденные вакансии сохренены в файле "data.json"\n')

    json_saver = JSONSaver()
    worker = VacancyWorker(json_saver.get_vacancies())

    area_answer = ask_questions('Отфильтровать вакансии по нужному городу?', 'Введите город')
    if area_answer:
        worker.filter_by_area(area_answer)

    salary_answer = ask_questions('Отфильтровать вакансии по средней зарплате?', 'Введите необходимую среднюю зарплату')
    if salary_answer:
        worker.filter_by_middle_salary(int(salary_answer))

    descript_answer = ask_questions('Отфильтровать вакансии по ключевым словам в описании?', 'Введите ключевые слова через пробел')
    if descript_answer:
        for word in descript_answer.split():
            worker.filter_by_description(word)

    sort_answer = ask_questions(
        'Отсортировать вакансии по зарплате?',
        'Введите "1" для сортировки по возрастанию или "2" для сортировки по убыванию'
    )
    if sort_answer == '1':
        worker.sort_vacancies(inverse=True)
    elif sort_answer == '2':
        worker.sort_vacancies(inverse=False)

    top_answer = ask_questions('Желаете вывести топ вакансий?', 'Сколько вакансий вывести? Введите данные числом')
    if not top_answer:
        vacancies = worker.vacancies
    else:
        vacancies = worker.get_top_vacancies(int(top_answer))

    for vacancy in vacancies:
        print(vacancy)


if __name__ == '__main__':
    main()

