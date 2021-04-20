import os
import sys

class Utils:

    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    @staticmethod
    def human_readable_size(num, decimal_places=2):
        for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
            if abs(num) < 1024.0:
                return "%3.1f %sB" % (num, unit)
            num /= 1024.0
        return "%.1f %sB" % (num, 'Yi')

    @staticmethod
    def normalize_filename(filename):
        realFileName, extension = os.path.splitext(os.path.basename(filename))
        realFileName = realFileName.replace(' ', '_')
        return f'{realFileName}{extension}'
