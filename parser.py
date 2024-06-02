from bs4 import BeautifulSoup
import requests


def htmlThief(url, defence=True):
    session = requests.Session

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    response = requests.post(url, verify=defence, headers=headers)

    soup = 0
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

    return soup


def infoThief(contTarget, contName, contClass_name, tg_name, tg_class):

    needed = []
    container_element = contTarget.findAll(contName, class_=contClass_name)

    for i in container_element:
        if i:

            movie_title_element = i.find(tg_name, class_=tg_class)

            if movie_title_element:
                needed.append(movie_title_element.get_text(strip=True))

    return needed


# def parserF():
#
#     map = {}
#
#     login_url = 'https://www.imdb.com/chart/top/'
#     session = requests.Session()
#
#     # Отправка POST-запроса для авторизации
#
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
#     response = requests.post(login_url, headers=headers)
#
#     # Проверка успешности авторизации
#     if response.status_code == 200:
#         print("Авторизация прошла успешно!")
#         html_content = response.text
#
#         soup = BeautifulSoup(html_content, 'html.parser')
#
#         container_element = soup.findAll('li', class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')
#         #container_element = soup.find('li', class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')
#
#         for i in container_element:
#             if i:
#
#                 movie_title_element = i.find('h3', class_='ipc-title__text')
#
#                 if movie_title_element:
#                     movie_title = movie_title_element.get_text(strip=True)
#                     movie_title = movie_title.split(' ', 1)[1]
#
#                 else:
#                     print("Элемент с названием фильма не найден")
#
#                 movie_rating_element = i.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
#
#                 if movie_rating_element:
#                     movie_rating = movie_rating_element.get_text(strip=True)
#                     movie_rating = movie_rating[:movie_rating.find("(")]
#
#             map[movie_title] = movie_rating
#
#
#     else:
#         print("Ошибка при авторизации:", response.status_code)
#
#     return map

def lab():

    map = {}
    body = htmlThief('https://www.imdb.com/chart/top/')

    firstSed = infoThief(body, 'li', 'ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent',
                      'h3', 'ipc-title__text')

    secondSed = infoThief(body, 'li', 'ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent',
                       'span', 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')


    for i in range(max(len(firstSed), len(secondSed))):
        first = firstSed[i].split(' ', 1)[1]
        second = secondSed[i][:secondSed[i].find("(")]

        map[first] = second
        print(f"Title - {first}, rating - {second}")

    return map

lab()