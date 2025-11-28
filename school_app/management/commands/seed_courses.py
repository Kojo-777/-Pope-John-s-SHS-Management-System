from django.core.management.base import BaseCommand
from school_app.models import Department, Course


class Command(BaseCommand):
    help = 'Seed default courses'

    def handle(self, *args, **options):
        items = [
            ('General Science', 'SCI-GEN', 'Science'),
            ('General Arts', 'ART-GEN', 'Arts'),
            ('Business', 'BUS-GEN', 'Business'),
            ('Visual Arts', 'VIS-ART', 'Visual Arts'),
        ]
        for name, code, dept_name in items:
            dept, _ = Department.objects.get_or_create(name=dept_name)
            Course.objects.get_or_create(
                code=code,
                defaults={
                    'name': name,
                    'department': dept,
                    'course_type': 'SHS',
                    'duration': '3 years',
                    'description': name,
                },
            )

