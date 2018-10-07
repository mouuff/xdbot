#!/usr/bin/python3

import quail

if not quail.helper.OS_WINDOWS:
    raise AssertionError("This test solution is windows only")

quail.run(
    solution=quail.SolutionGitHub("xdbot.zip", "https://github.com/mouuff/xdbot"),
    installer=quail.Installer(
        name='xdbot',
        icon='xdbot.exe',
        binary='xdbot.exe',
        publisher="xdbot",
        console=False,
        launch_with_quail=True
    ),
    builder=quail.builder.Builder(
        quail.builder.CmdIcon('icon.ico'),
        quail.builder.CmdNoconsole()
    ),
    controller=quail.ControllerTkinter()
)
