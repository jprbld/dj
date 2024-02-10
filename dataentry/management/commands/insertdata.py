from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from ...models import Student

class Command(BaseCommand):
    help = 'Insert data to database'

    # def add_arguments(self, parser: CommandParser) -> None:
    #     parser.add_argument('name', type=str, help="Specifies user name")

    def handle(self, *args: Any, **kwargs: Any) -> str | None:

        dataset = [
            {'roll_no': 1002, 'name': 'Sushi', 'age': 21},
            {'roll_no': 1003, 'name': 'John', 'age': 22},
            {'roll_no': 1004, 'name': 'Mike', 'age': 23},
            {'roll_no': 1005, 'name': 'Josh', 'age': 32},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(**data)
            else:
                self.stdout.write(self.style.WARNING(f"Student with roll number {roll_no} already exists"))


        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))