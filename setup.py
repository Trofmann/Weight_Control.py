from cx_Freeze import setup, Executable

executables = [Executable('main.py', base='Win32GUI', targetName='Weight Control')]

includes = ['pygame', 'app_data', 'app_settings', 'button', 'dialog_window', 'drawer', 'entry_pole', 'functions',
            'datetime', 'graphs', 'matplotlib', 'sys']
include_files = ['data.txt']

options = {
    'build_exe': {
        'includes': includes,
        'build_exe': 'Weight Control',
        'include_files': include_files
    }
}

setup(name='Weight control',
      version='1.0.0',
      description='My app',
      executables=executables,
      options=options)
