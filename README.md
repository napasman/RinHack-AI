<h4>Реализованная функциональность</h4>
<ul>
    <li>Функционал 1; Анализ трафика с помощью нейросети</li>
    <li>Функционал 2; Веб-сервис, позволяющий получать этот трафик в реальном времени</li>
    <li>Функционал 3; Отправка сообщений на почту при обнаружении вредоносного трафика</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Киллерфича-1; Архитектура, позволяющая легко масштабировать приложение</li>
 <li>Киллерфича-2; Использование связки моделей для распознавания вредносного трафика</li>
<li>Киллерфича-3; UoW, DI</li>
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Falcon Web Framework</li>
	<li>PostgreSQL, SQLAlchemy, Alembic</li>
    <li>Scikit-learn</li>
	<li>React + TypeScript + Vite</li>
	<li>Git.</li>
	<li>SMTP</li>
  
 </ul>
<h4>Демо</h4>
<p>Демо сервиса доступно по адресу: https://drive.google.com/drive/folders/1t4RWQrJN8P0yfC_VflBSiuj0JDo5jYpv </p>




СРЕДА ЗАПУСКА
------------
1) разработка и тестирование проводились на windows 10;
2) требуется node.js;
3) требуется установить список зависимостей из requirements.txt;
4) требуется установленная СУБД PostgreSQL;

УСТАНОВКА frontend
------------
### Установить node.js и добавить в PATH

Перейти в директорию frontend
~~~
npm i

npm run dev
~~~

УСТАНОВКА backend
------------
### Установить виртуальное окружение (предварительно установив Python)
~~~
python -m venv venv
~~~

### Установка зависимостей

Выполните 
~~~
pip install -r req.txt
~~~
### Переменные окружения
В файле .env необходимо указать переменные окружения:
~~~
SOURCE_PROVIDER=env
DATABASE_CONNECTION_STRING=postgresql+asyncpg://postgres:postgres@localhost:5432/rinhack
API_GATEWAY_BASE_URL=http://localhost:3000
SMTP_LOGIN="зарегистрированная почта с доступом к SMTP"
SMTP_PASSWORD="зарегистрированная почта с доступом к SMTP"
~~~
### База данных

Необходимо создать пустую базу данных, предварительно прописав путь к подключению.
Установка
На Windows 10:
С помощью графического клиента, либо
Открыть powershell и установить chocolatey
~~~
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
~~~
В командной строке:
~~~
choco install postgresql
~~~
Проверить версию:
~~~
psql --version
~~~
Создать БД:
~~~
psql -U postgres
CREATE DATABASE rinhack;
\q
~~~

### Выполнение миграций

Для выполнения миграций в консоли выполнить следующие команды: 
~~~
alembic revision --autogenerate
alembic upgrade head
~~~
и согласитесь с запросом

### Запуск сервера
~~~
uvicorn modules.api_gateway.interfaces.api.asgi:build_asgi --reload --host 0.0.0.0 --port 3000
~~~


