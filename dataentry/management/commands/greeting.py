from typing import Any
from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help="Specifies user name")

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        name = kwargs['name']
        greetings = f"Hi {name}, Good Morning"
        self.stdout.write(self.style.SUCCESS(greetings))