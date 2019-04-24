import os
for i in os.walk("/Users/praveen/Engagedly"):
   if i[0].count("pids"):
       os.chdir(i[0])
       if len(os.popen("ls").read())>0:
            os.system("rm server.pid")
            os.system("rm resque-pool.pid")

        