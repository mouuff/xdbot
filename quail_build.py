#!/usr/bin/python3

import iquail

if not iquail.helper.OS_WINDOWS:
    raise AssertionError("This test solution is windows only")


class FrameSelectMiniOrFull(iquail.controller_tkinter.FrameBaseConfigure):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.version_selected = self.add_combobox("Which version would you like to install?",
                                                  ('English', 'French'))

    def next_pressed(self):
        print(self.version_selected.get())
        version = self.version_selected.get().lower()
        zip = "xdbot.zip" if version == "french" else "xdbot_en.zip"
        self.manager.config.set("zip_url", zip)
        self.controller.switch_to_install_frame()


iquail.run(
    solution=iquail.SolutionGitHub(iquail.ConfVar("zip_url"),
                                   "https://github.com/mouuff/xdbot"),
    installer=iquail.Installer(
        name='xdbot',
        icon='xdbot.exe',
        binary='xdbot.exe',
        publisher="xdbot",
        console=False,
        launch_with_quail=True
    ),
    builder=iquail.builder.Builder(
        iquail.builder.CmdIcon('icon.ico'),
        iquail.builder.CmdNoconsole()
    ),
    controller=iquail.ControllerTkinter(install_custom_frame=FrameSelectMiniOrFull)
)
