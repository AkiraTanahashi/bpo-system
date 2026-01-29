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
