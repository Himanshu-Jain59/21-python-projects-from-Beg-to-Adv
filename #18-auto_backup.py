import os
import shutil
import datetime
import schedule
import time


source = "C:/Users/hp/Pictures/Saved Pictures"
dest = "C:/Users/hp/Pictures/Backups"
def do_backup(source,dest):
    today = datetime.date.today()
    dest_dir=os.path.join(dest,str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"copied to {dest_dir}")
    except FileExistsError:
        print("folder already exists in",dest)

def call():
    do_backup(source,dest)

schedule.every().day.at("23:33").do(call)


while(True):
    schedule.run_pending()
    time.sleep(60)