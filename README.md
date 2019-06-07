# *Newlance*

## Запуск проекта

### *Venv*

Создание *venv'а*:

```bash
$ python3 -m venv django_venv
```

Если получаем ошибку:
*"The virtual environment was not created successfully because ensurepip is not available... "*

Нужно дополнительно установить:

```bash
sudo apt-get install python3-venv
```

Вход в *venv*:

```bash
$ source django_venv/bin/activate
```

Для выхода из виртуального окружения *venv* наберите:

```bash
deactivate
```

Установка *django*:

```bash
(django_venv) ~$ python3 -m pip install --upgrade pip
(django_venv) ~$ pip install django
```

Скопируйте проект:

```bash
git clone https://gitlab.informatics.ru/AlSerP/freelance
```

Загрузите необходимые библиотеки:

```bash
pip3 install -r requirements.txt
```

Создайте миграции:

```bash
python manage.py makemigrations
```

Примените миграции:

```bash
python manage.py migrate
```

Запустите фикстуру:

```bash
python manage.py loaddata FreelanceApp/fixtures/base.json
```

Запустите проект из консоли:

```bash
(django_venv) ~/djangoProject $ python manage.py runserver
```

По умолчание проект запускается по адресу <localhost:8000>

ТЗ <https://docs.google.com/document/d/1bfd3Uk3oNw72QqMon3-SS6Lylj7LegFyG0e0AlN9eVQ/edit>
