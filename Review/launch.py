import subprocess
import os
import webbrowser

def launch_review():
    webbrowser.open("http://localhost:5006/AssesmentReview", new=1,autoraise=True)
    call_list = ["bokeh", "serve",os.path.join(os.path.dirname(__file__),"AssesmentReview.py")]
    print(call_list)
    subprocess.call(call_list)

if __name__ == '__main__':
    launch_review()