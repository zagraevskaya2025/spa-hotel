from app import db, User, app

with app.app_context():
    # Проверяем, есть ли уже администратор
    admin = User.query.filter_by(username="admin").first()

    if not admin:
        # Создание пользователя-администратора
        admin = User(username="admin", is_admin=True)
        admin.set_password("password")  # Установите пароль

        db.session.add(admin)
        db.session.commit()

        print(" Администратор успешно добавлен!")
    else:
        print(" Администратор уже существует.")
