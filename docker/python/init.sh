echo マイグレーションを実行
python manage.py migrate
echo マイグレーションを完了

echo 親カテゴリーの追加を実行
python manage.py loaddata ./threads/fixtures/parent_category.json
echo 親カテゴリーの追加を完了

echo 子カテゴリーを追加を実行
python manage.py loaddata ./threads/fixtures/category.json
echo 子カテゴリーを追加を完了
