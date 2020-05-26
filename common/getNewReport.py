import os
import time
from getRootPath import root_dir


def getReport():
    reportPath = os.path.join(root_dir, "report")
    lists = os.listdir(reportPath)

    #print(lists)

    lists.sort(key=lambda fn: os.path.getmtime(reportPath + "\\" + fn))

    file_new = os.path.join(reportPath, lists[-1])
    report = file_new.split(os.sep)[-1]

    file_path = r'D:\tomcat\webapps\examples'
    commond = "copy %s %s" % (file_new, file_path)
    print(commond)
    os.popen(commond)
    time.sleep(2)
    before_rename_file = "%s\\%s" % (file_path, report)
    after_rename_file = "%s\\report.html" % file_path

    if os.path.exists(after_rename_file):
       os.remove(after_rename_file)
    os.rename(before_rename_file, after_rename_file)


if __name__ == "__main__":
    getReport()