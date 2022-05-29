import re
import sys
import os


class Depend:
    @staticmethod
    def get_ql_path():
        if re.search('/ql/data/', sys.path[0]):
            return '/ql/data/'
        else:
            return '/ql/'

    @staticmethod
    def get_env(env, default=None):
        if env in os.environ and os.environ[env]:
            if os.environ[env] in ["True", "False"]:
                return False if os.environ[env] == "False" else True
            elif os.environ[env].isdigit():
                return int(os.environ[env])
            else:
                return os.environ[env]
        else:
            if default:
                return default
            else:
                return None

    @staticmethod
    def str2list(string):
        if string and string != "":
            if re.search(",", string):
                return string.split(",")
            else:
                return [string]
        else:
            return []

    @staticmethod
    def not2append(addlist, appended):
        for i in addlist:
            if i not in appended:
                appended.append(i)
        return appended

    def only_check(self, pyname):
        only_path = self.get_ql_path() + pyname + '_by_keven1024'
        result = "☺当前脚本目录为: " + str(os.path.abspath(__file__)) + "\n"
        if os.path.exists(only_path):
            with open(only_path, 'r') as f:
                if f.read(2048) != os.path.abspath(__file__):
                    result += "🙄检测到其他同类型的青龙日志分析脚本存在，拒绝运行!\n"
                    exit(0)
                else:
                    result += "😁脚本唯一性检测通过，继续运行!\n"
        else:
            with open(only_path, "w") as f:
                f.writelines(os.path.abspath(__file__))
                result += "🙄检测到第一次运行，已写入唯一性检测文件，如无特殊情况请勿删除\n"
        return result
