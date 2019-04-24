import os ,ast

whoami=os.popen("whoami").read()
location="/Users/"+whoami
location=location.strip()
location=location+"/.aws"
cmd="cp credentials "+location
os.system(cmd)

login=os.popen("aws ecr get-login --no-include-email --region ap-south-1").read()
os.system(login)
read=os.popen("aws ecr describe-repositories").read()
read=ast.literal_eval(read)
for i in read["repositories"]:
    for j in i:
       if j=='repositoryUri':
           image=i[j]
           os.system("docker pull "+image)


try:
  with open("path.txt" ,'r') as r :
      pwd=r.read()
except:
    with open("path.txt", 'w') as w:
        pwd = input("Enter the location of all Services by doing pwd in that directory ::>>\t")
        w.write(pwd)

for i in os.walk(pwd):
   if i[0].count("pids"):
       os.chdir(i[0])
       if len(os.popen("ls").read())>0:
            os.system("rm server.pid")


# os.chdir(pwd)
# os.system("docker-compose -f dockerexp.yml up")

# os.chdir("/Users/praveen/Engagedly")
# os.system("cat EngagedlyData.out | docker exec -i docker-postgres psql -U postgres")
