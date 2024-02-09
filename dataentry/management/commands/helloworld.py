from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints hello world"

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        self.stdout.write('Hello World')