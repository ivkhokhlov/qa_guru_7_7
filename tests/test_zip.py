import os
import zipfile

from conftest import RESOURCES_DIR


def test_zip_file_list():
    NEW_ZIP_PATH = os.path.join(RESOURCES_DIR, 'resources.zip')
    with zipfile.ZipFile(NEW_ZIP_PATH) as zip_file:
        filenames = [f.filename for f in zip_file.filelist]

    assert filenames == ['docs-pytest-org-en-latest.pdf', 'file_example_XLS_10.xls', 'file_example_XLSX_50.xlsx']
