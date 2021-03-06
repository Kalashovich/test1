# Git - распределеная система контроля версий.

# Это система для отслеживания и ведения истории изменения файлов, в вашем проекте.

# Репозиторий - хранилище вашего кода и истории его изменений.

# GitHub - это веб-сайт для размещения git-репозиториев и совместной разработки проектов.

# Команды Git:

# 1. git init - она создает новый гит репозиторий локально на вашем пк

# 2. git commit - как только мы достигаем определенного момента разработки , то тогда мы сохраняем и комментируем наши изменения.

# git commit -m '<коммент>'


# 3. git branch - Ветки очень выжны в git. При помощи веток несколько программистов могут работать парралельно на одном и том же проекте. При помоши команды git branch мы можем создать, просматривать или удалять ветки.

# Создание ветки:         git branch -M <название ветки>
# Просмотр всех веток:    git branch / git branch --list
# Удаление веток:         git branch -d <название ветки>

# 4. git remote add - это команда для того чтобы сказать ваш проект с удаленным репозиторием(репо в гитхаб).

# git remote add <название подключение> <ссылка на репозиторий> (ssh)

# 5. git add - когда мы создаем или изменяем файлы, при помощи мы загружаем все изменения в локлальное хранилище. 

# git add <название файла>
# git add .
# 6. git push - после коммита изменений, при помощи этой команды мы отправляем наши изменения на удаленный репозиторий 

# 7. git status - команда которая выдает нам всю информацию о наших файлах.

# 8. git checkout - команда используется для работы в команде, она помогает переключаться по веткам

# git checkout <название ветки>

# 9. git pull - команда которая используется для загрузки изменений (обновлений) из удаленного репозитория

# git pull <origin>

# #=====================================================================
# создание репозитория 

# 1. git init
# 2. git add .
# 3. git commit -m 'first commit'
# 4. git remote add origin <url>
# 5. git push origin push