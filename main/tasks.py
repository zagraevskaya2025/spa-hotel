from background_task import background
from django.core.mail import send_mail
from datetime import timedelta, datetime
from .models import Feedback
import time


@background(schedule=5)  # Задача выполняется через 5 секунд после постановки
def notify_admin(name, email, message):
    print(f"[Очередь] Задача поставлена: уведомление о новом отзыве от {name}")

    time.sleep(3)  # Имитация длительной обработки (например, сложной логики)

    try:
        send_mail(
            subject='Новый отзыв на сайте',
            message=f'Пользователь {name} ({email}) оставил отзыв:\n\n{message}',
            from_email='admin@spa-hotel.com',
            recipient_list=['admin@spa-hotel.com'],
            fail_silently=True,  # Не падаем, если почта не настроена
        )
        print(f"[Очередь] Задача завершена — уведомление отправлено ({name})")
    except Exception as e:
        print(f"[Очередь] Ошибка при отправке уведомления: {e}")


@background(schedule=60)  # Выполнится через 60 секунд (для теста). Можно указать repeat=86400 (раз в сутки)
def delete_old_feedbacks():
    threshold = datetime.now() - timedelta(days=30)
    deleted_count, _ = Feedback.objects.filter(created_at__lt=threshold).delete()
    print(f"[Очередь] Удалено {deleted_count} старых отзывов.")
