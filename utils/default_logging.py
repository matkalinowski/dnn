import logging
import os.path
from datetime import datetime

from config.structure import project_structure
_logging_dir = project_structure['logging_dir']


def configure_default_logging(name):
    _today = datetime.today().strftime('%Y-%m-%d')

    _logging_dir.mkdir(exist_ok=True)
    _log_file = f'{_today}.log'
    _pid = os.getpid()

    _file_handler = logging.FileHandler(_logging_dir / _log_file)
    _file_handler.setLevel(logging.DEBUG)
    _file_form = f'%(asctime)s: %(name)s: %(levelname)s: PID[{_pid}]: %(message)s'
    _file_handler.setFormatter(logging.Formatter(_file_form))

    _console_handler = logging.StreamHandler()
    _console_handler.setLevel(logging.DEBUG)
    _console_form = f'%(asctime)s: %(name)s: %(message)s'
    _console_handler.setFormatter(logging.Formatter(_console_form))

    _log = logging.getLogger(name)
    _log.setLevel(logging.DEBUG)
    _log.addHandler(_file_handler)
    _log.addHandler(_console_handler)

    return _log
