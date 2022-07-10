import os
import tempfile

from partitionsets.cli import main


def test_main():
    arg_tv = ['3 42 -1']
    assert main(arg_tv) == 0


def test_main_q():
    arg_tv = ['-q', '3 42 -1']
    assert main(arg_tv) == 0


def test_main_v():
    arg_tv = ['-v', '3 42 -1']
    assert main(arg_tv) == 0


def test_main_vv():
    arg_tv = ['-vv', '3 42 -1']
    assert main(arg_tv) == 0


def test_main_vvv():
    arg_tv = ['-vvv', '3 42 -1']
    assert main(arg_tv) == 0


def test_main_bell_numbers():
    arg_tv = ['-q', '-b', '3 42 -1']
    try:
        main(arg_tv)
        raise UserWarning('This should not have returned!')
    except SystemExit:
        pass


def test_main_q_json():
    arg_tv = ['-q', '-T', 'json', '3 42 -1']
    assert main(arg_tv) == 0


def test_main_q_csv():
    arg_tv = ['-q', '-T', 'csv', '3 42 -1']
    assert main(arg_tv) == 0


def test_main_q_o():
    tmp_dir = tempfile.mkdtemp()
    predictable_filename = 'myfile'
    # Ensure the file is read/write by the creator only
    save_umask = os.umask(0o0077)

    o_path = os.path.join(tmp_dir, predictable_filename)
    try:
        arg_tv = ['-q', '-o', o_path, '3 42 -1']
        assert main(arg_tv) == 0
    except IOError as e:
        raise e
    else:
        try:
            os.remove(o_path)
        except OSError:
            pass  # file already removed ...
    finally:
        os.umask(save_umask)
        os.rmdir(tmp_dir)
