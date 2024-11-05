import os
from datetime import datetime

file = ''
filepath = ''
filesize = 0
formatted_time = 0
parent_dir = ''
count = 0
print('Текущая директория:', os.getcwd())
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if os.path.isfile(file):
        # if not file in ('.gitignore', 'misc.xml', 'modules.xml', 'module_7_1.iml', 'workspace.xml',
        #                 'profiles_settings.xml', 'pyvenv.cfg', 'distutils-precedence.pth', 'pip-23.2.1.virtualenv',
        #                 'setuptools-68.2.0.virtualenv', 'wheel-0.41.2.virtualenv', '_virtualenv.pth',
        #                 '_virtualenv.py', 'py.typed', '__init__.py', '__main__.py', '__pip-runner__.py',
        #                 'build_env.py', 'cache.py', 'configuration.py', 'exceptions.py', 'pyproject.py',
        #                 'self_outdated_check.py', 'wheel_builder.py', 'autocompletion.py', 'base_command.py',
        #                 'cmdoptions.py', 'command_context.py', 'main_parser.py', 'parser.py', 'progress_bars.py'):
        # хорошо, что я довольно быстро перестал пытаться
            filepath = os.stat(file).st_nlink
            filetime = os.stat(file).st_dev
            formatted_time = os.stat(file).st_mtime
            formatted_time = datetime.fromtimestamp(formatted_time)
            filesize = os.stat(file).st_ctime
            parent_dir = os.stat(file).st_uid

            print(f'Обнаружен файл: {file}, Количество жёстких ссылок: {filepath}, Размер: {filesize} байт, '
                  f'Время изменения: {formatted_time}, Идентификатор пользователя: {parent_dir}')
        else:
            count += 1
print('Количество не обработанных файлов:', count) #844