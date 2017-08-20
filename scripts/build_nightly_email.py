#!/home/tom/.virtualenvs/nightlyrenpy/bin/python

from email.mime.text import MIMEText
import smtplib

import os
import sys
import subprocess

os.chdir(os.path.dirname(sys.argv[0]))


def build_nightly():

    with open("/tmp/build_nightly.txt", "w+") as f:
        rv = subprocess.call([ "./build_nightly.sh" ], stdout=f, stderr=f)

        f.seek(max(f.tell() - 1000, 0))
        output = f.read()

    print(output)

    msg = MIMEText(output)

    msg["Subject"] = "Build Ren'Py Nightly: {}".format(rv)
    msg["To"] = "pytom@bishoujo.us"
    msg["From"] = "nightly@renpy.org"

    s = smtplib.SMTP('localhost')
    s.sendmail("nightly@renpy.org", [ 'pytom@bishoujo.us' ], msg.as_string())
    s.quit()


if __name__ == "__main__":
    build_nightly()
