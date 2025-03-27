from flask_migrate import Migrate
from app import db, app

def upgrade():
    with app.app_context():
        # Добавляем новые колонки
        db.engine.execute('ALTER TABLE feedback ADD COLUMN email VARCHAR(120) NOT NULL DEFAULT ""')
        db.engine.execute('ALTER TABLE feedback ADD COLUMN rating INTEGER NOT NULL DEFAULT 5')

def downgrade():
    with app.app_context():
        # Удаляем добавленные колонки
        db.engine.execute('ALTER TABLE feedback DROP COLUMN email')
        db.engine.execute('ALTER TABLE feedback DROP COLUMN rating') 