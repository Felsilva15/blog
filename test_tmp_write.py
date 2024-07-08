# test_tmp_write.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    test_file_path = os.path.join(BASE_DIR, 'db', 'test_write.txt')
    with open(test_file_path, 'w') as f:
        f.write('Test write to db directory')
    print(f'Successfully wrote to {test_file_path}')
except Exception as e:
    print(f'Failed to write to db directory: {e}')
