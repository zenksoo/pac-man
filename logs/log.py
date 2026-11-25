from typing import TextIO
import sys

class Log:
    ERROR   = 1
    WARNING = 2
    NORMAL  = 3

    # this two boolean values will be changed from the game config
    # so if show logs is true: then i will to display logs on terminal
    # and if save logs is true: then i will to save logs to files
    # the player can see the logs and i can to debug the game :)))))
    show_logs: bool = False
    save_logs: bool = False

    logs_file: str = ".log"

    @classmethod
    def _render_logs(cls, log_file: TextIO, log_msg: str, log_type: int) -> None:
        if (log_type == cls.ERROR):
            log_file.write("\033[31m[Error] \033[39m")
        elif (log_type == cls.WARNING):
            log_file.write("\033[33m[Warrning] \033[39m")
        elif (log_type == cls.NORMAL):
            log_file.write("\033[32m[Noraml] \033[39m")

        log_file.write(log_msg)
        if (log_msg[-1] != "\n"):
            log_file.write("\n")

    @classmethod
    def _tty_logs(cls, log_msg: str, log_type: int) -> None:
        # log_type: there is tree type of logs 1 error and 2 warnings and 3 normal
        if (cls.show_logs):
            if log_type == cls.ERROR:
                sys.stderr.write("\033[31m[Error] \033[39m")
                sys.stderr.write(log_msg)
            elif log_type == cls.WARNING:
                sys.stderr.write("\033[33m[Warrning] \033[39m")
                sys.stderr.write(log_msg)
            else:
                sys.stdout.write("\033[32m[Noraml] \033[39m")
                sys.stdout.write(log_msg)
            if (log_msg[-1] != "\n"):
                    sys.stderr.write("\n")

    @classmethod
    def _file_logs(cls, log_msg: str, log_type: int) -> None:
        if (cls.save_logs):
            with open(cls.logs_file, '+a') as f:
                if log_type == cls.ERROR:
                    f.write("[Error] ")
                elif log_type == cls.WARNING:
                    f.write("[Warning] ")
                else:
                    f.write("[Normal] ")

                f.write(log_msg)
                f.write("\n")

    @classmethod
    def _unpermited_logs(cls, log_msg: str, log_type: str) -> None:
        if log_type == cls.ERROR:
            sys.stderr.write("\033[31m[Error] \033[39m")
            sys.stderr.write(log_msg)
        elif log_type == cls.WARNING:
            sys.stderr.write("\033[33m[Warrning] \033[39m")
            sys.stderr.write(log_msg)
        if (log_msg[-1] != "\n"):
            sys.stderr.write("\n")
