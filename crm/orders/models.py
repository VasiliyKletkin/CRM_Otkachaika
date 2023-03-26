from clients.models import Address
from companies.models import Company
from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices
from model_utils.fields import MonitorField, StatusField
import random

User = get_user_model()

class Order(models.Model):
    CONFIRMATION = 'CONFIRMATION'
    CONFIRMED = 'CONFIRMED'
    INPROGRESS = 'INPROGRESS'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

    STATUS = Choices(
        (CONFIRMATION, 'Подтверждение'),
        (CONFIRMED, 'Подтвержден'),
        (INPROGRESS, 'Выполняется'),
        (COMPLETED, 'Выполнен'),
        (CANCELED, 'Отменен'),
    )

    CASH = "CASH"
    CREDIT_CARD = "CREDIT_CARD"
    ONLINE_TRANSFER = "ONLINE_TRANSFER"

    TYPES_PAYMENT = Choices(
        (CASH, 'Наличные'),
        (CREDIT_CARD, 'Картой'),
        (ONLINE_TRANSFER, 'Онлайн перевод'),
    )

    status = StatusField("Статус", default=CONFIRMED)
    driver = models.ForeignKey(User, verbose_name="Водитель", on_delete=models.PROTECT, null=True, blank=True, related_name='orders')
    address = models.ForeignKey(Address, verbose_name="Адрес", on_delete=models.PROTECT, null=True, blank=True, related_name='orders')
    dispatcher = models.ForeignKey(User, verbose_name="Диспетчер", on_delete=models.PROTECT, related_name='created_orders')
    description = models.TextField("Описание", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    type_payment = models.CharField("Тип оплаты", max_length=20, choices=TYPES_PAYMENT, default=ONLINE_TRANSFER)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_planned = models.DateTimeField("Планируемая дата выполнения", null=True, blank=True)
    date_started = MonitorField("Дата начала выполнения", monitor='status', when=[INPROGRESS], null=True, blank=True, default=None)
    date_completed = MonitorField("Дата выполнения", monitor='status', when=[COMPLETED], null=True, blank=True, default=None)
    company = models.ForeignKey(Company, verbose_name="Компания", on_delete=models.PROTECT, related_name='orders')
    is_sent = models.BooleanField("Отправлен водителю", default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order id:{self.id} {self.address} {self.price} - {self.get_status_display()}'

class OrderRequest(Order):
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        proxy = True

    def __str__(self):
        return f'Order reqiest id:{self.id} {self.address} {self.price} - {self.get_status_display()}'
    
    def save(self, *args, **kwargs):
        if not self.company:
            companies = Company.objects.filter(city=self.address.city, subscriptions__is_active=True)
            self.company = random.choice(companies)
        return super().save(*args, **kwargs)