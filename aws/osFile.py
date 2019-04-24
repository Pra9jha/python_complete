import os
import docker

# print(os.name)
# print(os.getcwd())



# os.chdir("/Users/praveen/Desktop")

# for i in os.listdir():
#     if i=="docker-compose.yml":
#        print(dir(os.stat(i)))


# print(dir(os.walk("/Users/praveen/Desktop")))
# for a,b,c in os.walk("/Users/praveen/Desktop"):
#     print(a)
#     print(b)
#     print(c)

#
# print(os.environ.get('Home'.upper()))
# location=os.path.join(os.environ.get("HOME"),'.aws')
# location=os.path.join(location,'credentials')
# print(location)
# print("is the location folder     "+str(os.path.isdir(location)))
# print("is the location file     "+str(os.path.isfile(location)))
# print(os.path.splitext(location))
#
# with open(location,'r') as o:
#     info=o.read()
#     print(info)

# print(os.getcwd())
# os.chdir("/Users/praveen/Desktop/nginx")
# for i in range(1,11):
#     os.mkdir("test folder "+str(i),777 )

# dir=os.listdir(os.getcwd())
# for i in dir:
#     print(i)



# import glob
# print(glob.glob("test*"))
# for i in glob.glob("test*"):
#     os.rmdir(i)
# print(glob.glob("test*"))

full_name=os.path.dirname(os.getcwd())
print(full_name)




#
#
# print(os.path.isfile("docker-compose.yml"))
# print(os.path.isdir("nginx"))



# print(os.path.split("/Users/praveen/Desktop/nginx/docker-compose.yml"))


# import subprocess
#
# '''here it simply worked as a os.system comman dreturned o '''
# value=subprocess.call("date")
# print("Date  is "+str(value))
# '''here it will return the otput of the command   '''
# value=subprocess.check_output("date")
# print("Date is:: " + str(value))



import subprocess
# subprocess.check_call(["sh","-c",])

# task=os.popen("lsof -i tcp:3002").read()
# print(task)
# list=task.split("\n")
# for i in range(1,len(list)):
#  print(list[i])


# images=os.popen("docker images").read()
# # print(typ)
# lst=images.split("\n")
# for i in range(1,len(lst)):
#  print(lst[i])


# ENV_INIT_DIRECTORY= os.environ.get('ENV_INIT_DIRECTORY', 'Engagedly/super-admin')
# print(ENV_INIT_DIRECTORY)
# KILL_PROCESS_TIMEOUT = int(os.environ.get('KILL_PROCESS_TIMEOUT', 5))
# print(KILL_PROCESS_TIMEOUT)


# a=False
# while not a:
#  print("prashant")
# for name, value in os.environ.items():
#  print(name)
#  print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
#  print(value)
#
# import argparse
# class SomeClass:
#  def testParser(self,arg1,arg2):
#   print(arg1)
#   print(arg2)
#
#
# parser = argparse.ArgumentParser(description='Initialize the system.')
# parser.add_argument('name',type=str)
# parser.add_argument('sname',type=str)
# args = parser.parse_args()
# # print(args.name , args.sname)
# # print(args)
# s=SomeClass
# s.testParser(args.name,args.sname)
#

os.system("/etc/init.d/nginx start")
os.system("resque-pool --environment=development")
