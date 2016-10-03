
from partitionsets.cli import main


def test_main():
    arg_tv = [
        '3 42 -1'
    ]
    assert main(arg_tv) == 0


def test_main_q():
    arg_tv = [
        '-q',
        '3 42 -1'
    ]
    assert main(arg_tv) == 0


def test_main_v():
    arg_tv = [
        '-v',
        '3 42 -1'
    ]
    assert main(arg_tv) == 0


def test_main_vv():
    arg_tv = [
        '-vv',
        '3 42 -1'
    ]
    assert main(arg_tv) == 0


def test_main_vvv():
    arg_tv = [
        '-vvv',
        '3 42 -1'
    ]
    assert main(arg_tv) == 0


def test_main_bell_numbers():
    arg_tv = [
        '-q',
        '-b',
        '3 42 -1'
    ]
    try:
        main(arg_tv)
        raise UserWarning("This should not have returned!")
    except SystemExit:
        pass
