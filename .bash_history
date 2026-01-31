python3 -m venv venv
source venv/bin/activate
pip install django google-cloud-firestore google-auth
django-admin startproject config .
python manage.py startapp core
source /home/sundersan0807/venv/bin/activate
python manage.py runserver 8080
python manage.py migrate
python manage.py runserver 8080
gcloud config get-value project
gcloud config set project project-f577b35b-633d-4af8-904
python manage.py runserver 8080
mkdir -p core/templates/core
python manage.py runserver 8080
mkdir -p core/templates/registration
python manage.py createsuperuser
python manage.py runserver 8080
manage.py run
python manage.py runserver 8080
python debug_wp.py
gcloud auth application-default login
python manage.py runserver
pnthon manage.py runserver
python manage.py runserver
# .gitignoreファイルを作成（DB、仮想環境、キャッシュを除外）
echo "db.sqlite3" > .gitignore
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".DS_Store" >> .gitignore
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
git config --global user.name "AkiraTanahashi"
git config --global user.email "sundersan0807@gmail.com"
git init
git add .
git commit -m "ログイン機能の実装完了"
gh auth login
gh repo create bpo-system --public --source=. --remote=origin --push
git reset HEAD~1
echo ".cache/" >> .gitignore
git add .
git commit -m "不要なキャッシュを除外して保存"
git push origin master
git rm -r --cached .
git add .
git commit -m "重いファイルを除外して再コミット"
git push -f origin master
git rm --cached -r .cache/
.cache/
*.log
__pycache__/
*.pyc
db.sqlite3
.env
git reset --soft HEAD~1
# 直前のコミットを取り消す（ファイルの中身はそのまま保持）
git reset --soft HEAD~1
# .cache を除外した状態で、再度すべてをステージング
git add .
# 再度コミット
git commit -m "Initial commit excluding heavy cache files"
# プッシュ
git push origin master
rm -rf .git
git init
git add .
git commit -m "初期設定完了"
git branch -M master
git remote add origin https://github.com/AkiraTanahashi/bpo-system.git
git push -f origin master
git reset
echo ".config/" >> .gitignore
git add .
git commit -m "初期設定完了"
git push -f origin master
rm -rf .git
echo ".config/" >> .gitignore
echo ".cache/" >> .gitignore
git init
git reset --hard origin/master
git clean -fd
python manage.py runserver
python manage.py startapp clients
python manage.py makemigrations clients
python manage.py migrate
python manage.py startapp documents
python manage.py startapp bpo_docs
python manage.py makemigrations bpo_docs
python manage.py migrate
git add .
git commit -m "ドキュメント管理機能（bpo_docs）を追加"
git push origin master
python manage.py runserver
git add .
git commit -m "管理画面にクライアント管理機能を追加"
git push origin master
python manage.py runserver
mkdir locale
python manage.py runserver
sudo apt-get update
sudo apt-get install gettext -y
# 英語（en）のメッセージファイルを作成
python manage.py makemessages -l en
python manage.py makemessages -l en --ignore=venv --ignore=gopath --ignore=.cache
python manage.py compilemessages
python manage.py runserver
# 辞書ファイルに新しい項目を追加（以前のデータは消えませんので安心してください）
python manage.py makemessages -l en --ignore=venv --ignore=gopath --ignore=.cache
python manage.py compilemessages
# 1. 全ての変更をステージング（荷造り）
git add .
# 2. コミット（記録）
# メッセージ：「多言語対応（英語化）の実装と辞書ファイルの更新」
git commit -m "多言語対応（英語化）の実装と辞書ファイルの更新"
# 3. プッシュ（送信）
git push origin master
source /home/sundersan0807/venv/bin/activate
python manage.py startapp masters
python manage.py startapp logs
python manage.py makemigrations masters
python manage.py migrate
python manage.py makemessages -l en --ignore=venv --ignore=gopath --ignore=.cache
python manage.py compilemessages
python manage.py makemigrations logs
python manage.py migrate
pyhon manage.py runserver
python manage.py runserver
pip install google-cloud-firestore
pip install djangorestframework markdown django-filter
python manage.py runserver
