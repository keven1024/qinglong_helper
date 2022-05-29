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

    def only_check(self):
        only_path = self.get_ql_path() + self.pyname + '_by_keven1024'
        if os.path.exists(only_path):
            with open(only_path, 'r') as f:
                if f.read(2048) != os.path.abspath(__file__):
                    print("🙄检测到其他同类型的青龙日志分析脚本存在，拒绝运行!")
                    exit(0)
                else:
                    print("😁脚本唯一性检测通过，继续运行!")
        else:
            with open(only_path, "w") as f:
                print("🙄检测到第一次运行，已写入唯一性检测文件，如无特殊情况请勿删除")
                f.writelines(os.path.abspath(__file__))
