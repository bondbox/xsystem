# coding:utf-8

from typing import List
from typing import Optional
from typing import Sequence

from xarg import add_command
from xarg import argp
from xarg import commands
from xarg import run_command

from ..utils import __description__
from ..utils import __project__
from ..utils import __urlhome__
from ..utils import __version__

subs: List[add_command] = list()

try:
    from .path import add_cmd_path
    subs.append(add_cmd_path)
except Exception:
    pass


@add_command(__project__)
def add_cmd(_arg: argp):
    pass


@run_command(add_cmd, *subs)
def run_cmd(cmds: commands) -> int:
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    cmds = commands()
    cmds.version = __version__
    return cmds.run(
        root=add_cmd,
        argv=argv,
        description=__description__,
        epilog=f"For more, please visit {__urlhome__}.")
