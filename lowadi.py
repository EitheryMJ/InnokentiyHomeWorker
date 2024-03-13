import os
import random
from datetime import datetime
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from os import getenv
from selenium.webdriver.common.keys import Keys


def newDR():
    chromeOptions = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  # normal - full_load
    chromeOptions.add_argument("--single-process")
    chromeOptions.headless = False
    driver = uc.Chrome(options=chromeOptions, desired_capabilities=caps)
    return (driver)


def check_ufo(current_url):

    good_ufo = {'vieillissement': 'очки роста'}
    bad_ufo = {'pomme': 'яблоко', 'carotte': 'морковь', 'classique': 'седло', 'mash': 'комбикорм',
               'equus': 'экю'}
    try:
        if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]'):
            icon = driver.find_element(By.XPATH, '/html/body/div[1]/img').get_attribute('src')

            for bad_key in bad_ufo:
                if bad_key in icon:
                    print(f"НЛО: {bad_ufo[bad_key]}, надо скипнуть")
                    driver.get(current_url)

            for good_key in good_ufo:
                if good_key in icon:
                    print(f"НЛО: {good_ufo[good_key]}, надо брать")
                    driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').click()
                    driver.find_element(By.XPATH, '//*[@id="agi-10972849001709751854"]').click()
                    driver.find_element(By.XPATH, '/html/body/div[12]/aside/div[2]/button/span/span').click()


    except:
        pass


def login_lowadi():
    now = datetime.now().strftime('%H:%M:%S')
    print(f'{now}: Логинимся на lowadi.com')
    url = 'https://www.lowadi.com'

    driver.get(url)

    try:
        print('Принимаем cookie')
        driver.find_element(By.XPATH, '/html/body/aside/div/article/div/div[2]/div/div/div[3]/form/button').click()
    except:
        print('Принять cookie не просили')

    try:

        print(f'Начинаем!')
        driver.find_element(By.XPATH, '/html/body/div[7]/header/nav/div/strong').click()
        time.sleep(2)
        print(f'Вводим логин..')
        login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
        time.sleep(1)
        print(f'Вводим пароль..')
        password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
        time.sleep(1)
        print(f'Входим')
        connect = driver.find_element(By.XPATH, '/html/body/div[7]/header/nav/div/div/form/button/span/span/span').click()
        driver.find_element(By.XPATH, '/html/body/div[7]/header/nav/div/div/form/button/span/span/span').click()

    except:

        url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=20378769'
        driver.get(url)

        print(f'Пробуем зайти заново')
        time.sleep(60)
        print(f'Вводим логин..')
        login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
        time.sleep(1)
        print(f'Вводим пароль..')
        password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
        time.sleep(1)
        print(f'Входим')
        connect = driver.find_element(By.XPATH,
                                      '/html/body/div[7]/main/section/section/aside/form/button').click()
        time.sleep(60)


def milk_horse(age, name, n):
    print(f'№{n} Молочный жеребенок: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonAllaiter"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    next_hourse = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
    ).click()


def fourrage_horse(age, name, n):
    print(f'№{n} Жеребенок на фураже: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(1)
    choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[9]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)

    try:
        next_hourse = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
        ).click()

    except:
        next_hourse = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
        ).click()


def young_horse(age, name, n):
    print(f'№{n} Молодая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(1)
    choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[11]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(1)
    next_hourse = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
    ).click()


def old_horse(age, name, n):
    print(f'№{n} Взрослая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(1)
    try:
        if 'недостаточный вес' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[21]').click()
            time.sleep(1)
        else:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[13]').click()
    except:
        choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[13]').click()
        time.sleep(1)

    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(1)


def female_horse(current_url):
    try:

        not_ready = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-body-content"]/div[1]/table/tbody/tr[1]/td'
        ).text
        print(not_ready)
        try:
            next_hourse = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
            ).click()
        except:
            next_hourse = driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
            ).click()

        return 0

    except:

        if driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Случить кобылу':

            print('Нужна случка, идем на брачный рынок..')
            check_ufo(current_url)
            driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').click()
            time.sleep(1)
            master = driver.find_element(By.XPATH, '//*[@id="breeder"]').send_keys('Kolgotki')
            time.sleep(1)
            get_offers = driver.find_element(By.XPATH,
                                             '/html/body/div[7]/main/section/section/form/button[1]/span/span').click()
            time.sleep(1)
            price_sort = driver.find_element(By.XPATH, '//*[@id="table-0"]/thead/tr/td[6]/a').click()
            time.sleep(1)
            get_mating = driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[8]/a').click()
            time.sleep(1)

            if 'Kolgotki' in driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[2]').text:

                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

            print('Кобыла успешно провела случку')
            try:
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()
            except:
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()

            return 1

        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Эхография':

            print('Кобыла уже беременна')
            try:
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()
            except:
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()

            return 0


def male_horse():
    mating = 25
    num = 0
    try:
        for i in range(5):
            energie = int(driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[2]'
                '/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
            ).text)
            if energie - mating >= 20:
                create_mating = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
                ).click()
                time.sleep(1)
                open_mating = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/ul/li[1]/input'
                ).click()
                choice_equus = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select'
                ).click()
                time.sleep(2)
                lower_price = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[2]'
                ).click()
                time.sleep(1)
                complete = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span'
                ).click()
                time.sleep(5)

                num += 1

        print(f'Конь предложил случек: {num}')
        try:
            next_hourse = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
            ).click()

            return num

        except:
            next_hourse = driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
            ).click()

            return num

    except:
        print('error male_horse')

        return 0


def childbirth(current_url):
    check_ufo(current_url)
    sex = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/img'
    ).get_attribute('alt')
    gen_potential = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[2]/tbody/tr[1]/td[2]/span').text
    print(f'Родился жеребенок! Пол: {sex}, ГП: {gen_potential}')

    if sex == 'male':

        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(f'Пуля {gen_potential}')

    elif sex == 'femelle':

        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(f'Вишня {gen_potential}')
    profile = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[1]'
    ).click()
    time.sleep(1)
    farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]').click()
    time.sleep(2)
    get_farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]/select/option[2]'
    ).click()
    time.sleep(1)
    complete = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/button'
    ).click()
    time.sleep(1)
    return_to_mother = driver.get(current_url)

    return 1


def get_stable():
    try:
        print('Лошадь нуждается в стойле, ищем подходящий КСК..')
        find_stable = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[4]/div/div[1]'
            '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
        ).click()
        time.sleep(1)
        two_mouth = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/table/thead/tr/td[6]/span[2]/span/span[9]/a'
        ).click()
        time.sleep(1)
        low_price_stable = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/table/tbody/tr[1]/td[10]/button/span/span/span/span'
        )
        low_price_stable.click()
        alert = driver.switch_to.alert
        alert.accept()
        print(f'Стойло найдено за {low_price_stable.text}, продолжаем')

        return 1

    except:

        return 0


def death_horse():
    try:
        death = driver.find_element(
            By.XPATH,
            '//*[@id="page-contents"]/section/div/div/div[1]/h1'
        ).text
        if 'умер' in death:
            paradise = driver.find_element(
                By.XPATH,
                '//*[@id="page-contents"]/section/div/div/div[1]/div[2]/a'
            ).click()
            print('Ваша лошадь умерла и отправилась в рай, аминь')

            return 1

    except:

        return 0


def work_horse():
    print('Начинаем гонять лошадулек')
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=20378769'
    driver.get(url)
    children = 0
    get_mating = 0
    post_mating = 0
    stable = 0
    n = 1
    time.sleep(60)
    current_url = ''

    while driver.find_element(
            By.XPATH,
            '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
    ).get_attribute('href') != 'https://www.lowadi.com/elevage/chevaux/cheval?id=19637945':

        try:
            dead = death_horse()

            if dead == 1:
                driver.get(current_url)
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()

            current_url = driver.find_element(
                By.XPATH,
                '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
            ).get_attribute('href')
            age = driver.find_element(
                By.XPATH,
                '//*[@id="characteristics-body-content"]/table/tbody/tr[1]/td[2]'
            ).text.split()
            name = driver.find_element(
                By.XPATH,
                '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
            ).text
            check_ufo(current_url)

            try:

                if 'Зарегистрируйте свою лошадь' in driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[1]'
                    '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
                ).text:

                    stable += get_stable()
                    time.sleep(30)

            except:

                pass

            if (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                fourrage_horse(age, name, n)

            elif 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                milk_horse(age, name, n)

            elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                    ['Возраст:', '2', 'года', '4', 'мес.']:
                young_horse(age, name, n)

            elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                    ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                try:
                    if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                        print('Ваша кобыла скоро родит!')
                        call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                        time.sleep(1)
                        children += childbirth(current_url)
                except:
                    pass

                old_horse(age, name, n)

                if 'кобыла' in driver.find_element(
                        By.XPATH,
                        '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text:
                    get_mating += female_horse(current_url)
                elif 'конь' in driver.find_element(
                        By.XPATH,
                        '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text:
                    post_mating += male_horse()

        except:
            print('Некакая error при уходе за лошадью')
            next_hourse = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
            ).click()

        n += 1
        print('-' * 50)
    now = datetime.now().strftime('%d.%m %H:%M')
    print(f'{now} прогон окончен.\nРодилось жеребят: {children}\nПринято случек: {get_mating}\n'
          f'Предложено случек: {post_mating}\nКуплено стойл: {stable}')
    driver.quit()


try:
    print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
    driver = newDR()
    driver.set_window_size(1900, 1000)
except:
    time.sleep(30)
    driver = newDR()
    driver.set_window_size(1900, 1000)

login_lowadi()
time.sleep(5)
work_horse()





