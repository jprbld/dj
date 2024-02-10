from typing import Any
from django.core.management.base import BaseCommand, CommandParser, CommandError
# from ...models import Student
from django.apps import apps

import csv

class Command(BaseCommand):
    help = "Import data from csv file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file_path', type=str, help="Specifies csv file path")
        parser.add_argument('model_name', type=str, help="Name of the model")

    def handle(self, *args: Any, **kwargs: Any) -> str | None:

        file_path = kwargs['file_path']
        model_name = kwargs['model_name']

        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue
        
        if not model:
            raise CommandError(f"Model {model_name} not found in any app!")

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully!'))