
from partitionsets.cli import main


def test_main():
    arg_tv = [
        '-q',
        '3 42 -1'
    ]
    assert main(arg_tv) == 0
