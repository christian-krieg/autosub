########################################################################
# worker.py -- runs the actual tests of task results
#
# Copyright (C) 2015 Andreas Platschek <andi.platschek@gmail.com>
#                    Martin  Mosbeck   <martin.mosbeck@gmx.at>
# License GPL V2 or later (see http://www.gnu.org/licenses/gpl2.txt)
########################################################################

import threading
import os
import common
import sqlite3 as lite

class worker (threading.Thread):
   def __init__(self, threadID, name, job_queue, sender_queue, logger_queue):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.job_queue = job_queue
      self.sender_queue = sender_queue
      self.logger_queue = logger_queue

   ####
   # log_a_msg()
   ####
   def log_a_msg(self, msg, loglevel):
         self.logger_queue.put(dict({"msg": msg, "type": loglevel, "loggername": self.name}))

   ####
   #  connect_to_db()
   ####
   def connect_to_db(self, dbname):
      # connect to sqlite database ...
      try:
         con = lite.connect(dbname)
      except:
         logmsg = "Failed to connect to database: " + dbname
         self.log_a_msg(logmsg, "ERROR")

      cur = con.cursor()
      return cur, con
   ####
   #  get_taskParameters
   #
   #  look up the taskParmeters, that were generated from the generator for
   #  a indididual task
   ####
   def get_taskParameters(self, curs, cons, UserId, TaskNr):
      sql_cmd="SELECT TaskParameters FROM UserTasks WHERE TaskNr == "+str(TaskNr)+" AND UserId== "+str(UserId)
      curs.execute(sql_cmd)
      taskParameters = curs.fetchone()[0]
      return taskParameters

   ####
   # thread code for the worker thread.
   ####
   def run(self):
      logmsg = "Starting " + self.name
      self.log_a_msg(logmsg, "INFO")

      while True:
         nextjob = self.job_queue.get(True)
         if nextjob:
             TaskNr=nextjob.get('taskNr')
             UserId=nextjob.get('UserId')
             UserEmail=nextjob.get('UserEmail')
             MessageId=nextjob.get('MessageId')

             logmsg = self.name + ": got a new job: " + str(TaskNr) + "from the user with id: " + str(UserId)
             self.log_a_msg(logmsg, "INFO")

             # check if there is a test executable configured in the database -- if not fall back on static
             # test script.
             curc, conc = self.connect_to_db('course.db')
             sql_cmd="SELECT TestExecutable FROM TaskConfiguration WHERE TaskNr == "+str(TaskNr)
             curc.execute(sql_cmd);
             testname = curc.fetchone();
    
             if str(testname[0]) != 'None':
                sql_cmd="SELECT PathToTask FROM TaskConfiguration WHERE TaskNr == "+str(TaskNr)
                curc.execute(sql_cmd);
                path = curc.fetchone();
                scriptpath = str(path[0]) + "/" + str(testname[0])
             else:
                scriptpath = "tasks/task" + str(TaskNr) + "/./tests.sh"
             conc.close()  
             
             
             # get the taskParameters
             curs, cons = self.connect_to_db('semester.db')
             taskParameters= self.get_taskParameters(curs,cons,UserId,TaskNr)
             cons.close()
             
             # run the test script
             logmsg = "Running test script: " + scriptpath 
             self.log_a_msg(logmsg, "INFO")
             command = ""+scriptpath+" " + str(UserId) + " " + str(TaskNr) + " " + str(taskParameters) +" >> autosub.stdout 2>>autosub.stderr"
             test_res = os.system(command)

             if test_res:

                logmsg = "Test failed! User: " + str(UserId) + " Task: " + str(TaskNr)
                logmsg = logmsg + "return value:" + str(test_res)
                self.log_a_msg(logmsg, "INFO")

                common.send_email(self.sender_queue, str(UserEmail), str(UserId), "Failed", str(TaskNr), "", str(MessageId))

                if test_res == 512: # Need to read up on this but os.system() returns 
                                    # 256 when the script returns 1 and 512 when the script returns 2!
                   logmsg = "SecAlert: This test failed due to probable attack by user!"
                   self.log_a_msg(logmsg, "INFO")

                   common.send_email(self.sender_queue, str(UserEmail), str(UserId), "SecAlert", str(TaskNr), "", str(MessageId))

             else:

                logmsg = "Test succeeded! User: " + str(UserId) + " Task: " + str(TaskNr)
                self.log_a_msg(logmsg, "INFO")

                common.send_email(self.sender_queue, str(UserEmail), str(UserId), "Success", str(TaskNr), "", "")
                common.send_email(self.sender_queue, str(UserEmail), str(UserId), "Task", str(int(TaskNr)+1), "", str(MessageId))
