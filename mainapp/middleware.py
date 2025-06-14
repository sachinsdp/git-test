import os
from django.conf import settings

class LoadDatabaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.db_data = self.load_file('database.txt')

    def load_file(self, filename):
        try:
            file_path = os.path.join(settings.BASE_DIR, 'productionfiles', filename)
            with open(file_path, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error loading {filename}: {e}"

    def __call__(self, request):
        request.db_data = self.db_data
        return self.get_response(request)
