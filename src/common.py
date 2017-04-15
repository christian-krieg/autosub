########################################################################
# common.py -- common functions
#
# Copyright (C) 2015 Andreas Platschek <andi.platschek@gmail.com>
#                    Martin  Mosbeck    <martin.mosbeck@gmx.at>
# License GPL V2 or later (see http://www.gnu.org/licenses/gpl2.txt)
########################################################################

import sqlite3 as lite
import os
import datetime

format_string = '%Y-%m-%d %H:%M:%S'

####
# log_a_msg
####
def log_a_msg(lqueue, lname, msg, loglevel):
    """
    Put a message with a loglevel in a logqueue.
    """

    lqueue.put(dict({"msg": msg, "type": loglevel, "log_src": lname, "log_dst": "autosub"}))

####
# log_task_msg
####
def log_task_msg(lqueue, lname, msg, loglevel):
    """
    Put a task message with a loglevel in a logqueue.
    """

    lqueue.put(dict({"msg": msg, "type": loglevel, "log_src": lname, "log_dst": "task_msg"}))

####
# log_task_error
####
def log_task_error(lqueue, lname, msg, loglevel):
    """
    Put a task error message with a loglevel in a logqueue.
    """

    lqueue.put(dict({"msg": msg, "type": loglevel, "log_src": lname, "log_dst": "task_error"}))

####
# check_dir_mkdir
####
def check_dir_mkdir(directory, lqueue, lname):
    """
    Create a directory.

    Return 0 if the directory already existed, 1 if it had to be created.
    """

    if not os.path.exists(directory):
        os.mkdir(directory)
        logmsg = "Created directory: " + directory
        log_a_msg(lqueue, lname, logmsg, "DEBUG")
        return 1
    else:
        logmsg = "Directory already exists: " + directory
        log_a_msg(lqueue, lname, logmsg, "WARNING")
        return 0

####
# send_email
####
def send_email(queue, recipient, user_id, messagetype, tasknr, body, messageid):
    """
    Send Email to a user.
    """

    queue.put(dict({"recipient": recipient, "UserId": str(user_id), \
                    "message_type": messagetype, "Task": str(tasknr), \
                    "Body": body, "MessageId": messageid}))

####
# connect_to_db
####
def connect_to_db(dbname, lqueue, lname):
    """
    Connect to a sqlite database.

    Return None, None if connection failed.
    """

    try:
        con = lite.connect(dbname, 120)
    except:
        logmsg = "Failed to connect to database: " + dbname
        log_a_msg(lqueue, lname, logmsg, "ERROR")
        return None, None

    cur = con.cursor()

    return cur, con

####
# increment_db_statcounter
####
def increment_db_statcounter(semesterdb, countername, lqueue, lname):
    """
    Increment one of the statistic counters.
    """

    curs, cons = connect_to_db(semesterdb, lqueue, lname)

    data = {'Name': countername}
    #change to?: SET Value = Value + 1 WHERE ...
    sql_cmd = "UPDATE StatCounters SET Value = Value + 1 WHERE Name == :Name"
    curs.execute(sql_cmd, data)
    cons.commit()

    cons.close()

####
# get_task_starttime
####
def get_task_starttime(coursedb, tasknr, lqueue, lname):
    """
    Get the start datetime of a task.

    Return datetime, if not found return unixepoch start.
    """

    curc, conc = connect_to_db(coursedb, lqueue, lname)

    try:
        data = {'TaskNr': tasknr}
        sql_cmd = "SELECT TaskStart FROM TaskConfiguration WHERE TaskNr == :TaskNr"
        curc.execute(sql_cmd, data)
        tstart_string = str(curc.fetchone()[0])
        ret = datetime.datetime.strptime(tstart_string, format_string)
    except:
        ret = datetime.datetime(1970, 1, 1, 0, 0, 0)

    conc.close()

    return ret

####
# get_task_deadline
####
def get_task_deadline(coursedb, tasknr, lqueue, lname):
    """
    Get the deadline datetime of a task.

    Return datetime, if not found return unixepoch start.
    """

    curc, conc = connect_to_db(coursedb, lqueue, lname)
    try:
        data = {'TaskNr': tasknr}
        sql_cmd = "SELECT TaskDeadline FROM TaskConfiguration WHERE TaskNr == :TaskNr"
        curc.execute(sql_cmd, data)
        deadline_string = str(curc.fetchone()[0])
        ret = datetime.datetime.strptime(deadline_string, format_string)
    except:
        ret = datetime.datetime(1970, 1, 1, 0, 0, 0)

    conc.close()

    return ret


####
# user_set_current_task
####
def user_set_current_task(semesterdb, tasknr, user_id, lqueue, lname):
    """
    Set current task number of a user.
    """

    curs, cons = connect_to_db(semesterdb, lqueue, lname)

    data = {'TaskNr': tasknr, 'UserId': user_id}
    sql_cmd = "UPDATE Users SET CurrentTask = :TaskNr WHERE UserId == :UserId"
    curs.execute(sql_cmd, data)
    cons.commit()

    cons.close()


####
# user_get_current_task
####
def user_get_current_task(semesterdb, user_id, lqueue, lname):
    """
    Get current task number of a user
    """

    curs, cons = connect_to_db(semesterdb, lqueue, lname)

    data = {'UserId': user_id}
    sql_cmd = "SELECT CurrentTask FROM Users WHERE UserId == :UserId"
    curs.execute(sql_cmd, data)
    res = curs.fetchone()

    cons.close()

    return int(res[0])

####
# is_valid_task_nr
####
def is_valid_task_nr(coursedb, task_nr, lqueue, lname):
    """
    Check if the given task_nr is valid by looking for it's
    database entry
    """

    curc, conc = connect_to_db(coursedb, lqueue, lname)
    data = {'task_nr' : task_nr}
    sql_cmd = "SELECT TaskNr from TaskConfiguration WHERE TaskNr = :task_nr"
    curc.execute(sql_cmd, data)
    res = curc.fetchone()
    conc.close()

    return res != None

####
# get_num_tasks
####
def get_num_tasks(coursedb, lqueue, lname):
    """
    Get the configured number of tasks.
    """

    curc, conc = connect_to_db(coursedb, lqueue, lname)

    sql_cmd = "SELECT Content FROM GeneralConfig WHERE ConfigItem == 'num_tasks'"
    curc.execute(sql_cmd)
    num_tasks = int(curc.fetchone()[0])

    conc.close()

    return num_tasks
