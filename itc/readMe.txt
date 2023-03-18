onod@LgOfficialAppSv:~/itc$ source venv/bin/activate
(venv) onod@LgOfficialAppSv:~/itc$ cd src
(venv) onod@LgOfficialAppSv:~/itc/src$ python manage.py runserver 0.0.0.0:8000
(venv) onod@LgOfficialAppSv:~/itc/src$ deactivate

ローカルPCからリモートへファイルコピー.
$ scp ~/work/css/*.* onod@20.78.246.239:~/itc/src/static_local/css/
