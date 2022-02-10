# Приложение для расчета NPV с учетом заданного графика затрат и доходов по годам

### Instalation 📋

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### Environments

_django-environ_

например .envexample

### Issues🔧

_python GUI/main.py работает без проблем но pyinstaller не пропускает
архива .env и этих модулей в сборке,_
_должен читать больше документацию_

Первая попытка

```
import environ
root = environ.Path(**file**) - 2
env = environ.Env()
environ.Env.read_env(os.path.join(root, '.env'))
IP = env.str('IP', default='127.0.0.1')
PORT = env.str('PORT', default='8000')
```
Вторая попытка

```
from pathlib import Path
from dotenv import load_dotenv
env_path = Path(**file**).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
IP = os.environ.get('IP')
PORT = os.environ.get('PORT')
```
