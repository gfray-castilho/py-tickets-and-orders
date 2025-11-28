from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth import get_user_model
from db.models import Order, Ticket, MovieSession

def create_order(tickets: list[dict], username: str, date=None) -> Order:
    with transaction.atomic():
        # 1. pegar o usuário
        user = User.objects.get(username=username)

        # 2. criar o order
        order = Order.objects.create(user=user)

        # 3. se veio uma data, aplicar
        if date is not None:
            order.created_at = date
            order.save()

        # 4. criar cada ticket
        for t in tickets:
            Ticket.objects.create(
                row=t["row"],
                seat=t["seat"],
                movie_session=MovieSession.objects.get(id=t["movie_session"]),
                order=order,
            )

        return order



def get_orders(username:str | None = None):
    query_set = Order.objects.all()

    if username is not None:
        query_set = query_set.filter(user__username=username)

    return query_set