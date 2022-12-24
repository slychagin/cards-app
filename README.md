# cards-app
### Web app for managing the database of bonus cards

В качестве фронтэнда использован шаблон Bootstrap.
Бэкэнд реализован на Django Framework.

Описание возможностей и функционала вэб приложения:
- веб-приложение позволяет управлять базой данных бонусных карт (карт лояльности, кредитных карт и т.д.);
- список карт с полями: серия, номер, дата выпуска, дата окончания активности, статусж;
- поиск по этим же полям;
- просмотр профиля карты;
- активация/деактивация карты;
- удаление карты;
- реализован генератор карт, с указанием серии и количества генерируемых карт, а также срокадействия;
- после истечения срока действия, у карты проставляется статус "просрочена".

#
### Вэб приложение в работе:

#### *Общий вид приложения.* :
![CardApp](https://github.com/slychagin/cards-app/blob/master/demo_gifs/CardApp.gif)
#

#### *Генератор карт*
![CardGenerator](https://github.com/slychagin/cards-app/blob/master/demo_gifs/CardGenerator.gif)
#

#### *Админка*
![AdminPanel](https://github.com/slychagin/cards-app/blob/master/demo_gifs/AdminPanel.gif)
#

### Что использовано для создания сайта:
- Python 3, HTML, CSS, JavaScript, Bootstrap;
- Django Framework;
- SQLite.

### Вы можете запустить этот проект локально просто сделав следующее:
- `git clone https://github.com/slychagin/cards-app.git`;
- у вас должен быть установлен Python;
- установите все зависимости из файла requirements.txt;
- создайте супер пользователя `python manage.py createsuperuser` и войдите в систему;
- `python manage.py runserver`.
