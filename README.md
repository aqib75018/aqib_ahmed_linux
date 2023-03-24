LINUX


# TD 1_1 LINUX FONDAMENTAL


## Exercice 1 :

### Question 1 :

```
[ec2-user@ip-172-31-46-245 ~]$ pwd
```

Résultat :

```
/home/ec2-user
```

### Question 2 :

```
[ec2-user@ip-172-31-46-245 ~]$ ls
```

Résultat :

```
ls        lsattr    lsblk     lscpu     lsinitrd  lsipc     lslocks   lslogins  lsmcli    lsmd      lsmem     lsmod     lsns      lsof      lspci
```

### Question 3 :

```
[ec2-user@ip-172-31-46-245 ~]$ pwd
```

Résultat :

```
/home/ec2-user
```

### Question 4 :

```
[ec2-user@ip-172-31-46-245 lib]$ cd /home/ec2-user
[ec2-user@ip-172-31-46-245 ~]$ mkdir test
[ec2-user@ip-172-31-46-245 ~]$ ls
```

Résultat :

```
test
```

### Question 5 :

```
[ec2-user@ip-172-31-34-253 ~]$ cd ..
[ec2-user@ip-172-31-34-253 home]$ ls
```

Résultat :

```
ec2-user
```


### Question 6 :

```
[ec2-user@ip-172-31-34-253 home]$ cd ..
[ec2-user@ip-172-31-34-253 /]$ ls
```

Résultat :

```
bin  boot  dev  etc  home  lib  lib64  local  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```


### Question 7 :

```
[ec2-user@ip-172-31-34-253 /]$ cd home
[ec2-user@ip-172-31-34-253 home]$ pwd
```

Résultat :

```
/home
```


### Question 8 :

```
[ec2-user@ip-172-31-34-253 ~]$ cd ..
```

Résultat :

```
[ec2-user@ip-172-31-34-253 home]$ 
```

### Question 9 :

```
[ec2-user@ip-172-31-34-253 home]$ cd
[ec2-user@ip-172-31-34-253 ~]$ pwd
```

Résultat :

```
/home/ec2-user
```

 ### Question 10 :

```
[ec2-user@ip-172-31-34-253 ~]$ mkdir test1
[ec2-user@ip-172-31-34-253 ~]$ ls
```

Résultat :

```
test  test1
```

 ### Question 11 :

```
[ec2-user@ip-172-31-34-253 ~]$ cd test
[ec2-user@ip-172-31-34-253 test]$ pwd
```

Résultat :

```
/home/ec2-user/test
```


 ### Question 12 :

```
[ec2-user@ip-172-31-34-253 test]$ pwd
```

Résultat :

```
/home/ec2-user/test
```


## Exercice 2 :

### Question 1 :

```
[ec2-user@ip-172-31-34-253 test]$ cd
```

 ### Question 2 :

```
[ec2-user@ip-172-31-34-253 ~]$ pwd
```

Résultat :

```
/home/ec2-user
```


 ### Question 3 :

```
[ec2-user@ip-172-31-34-253 ~]$ mkdir linux_ex_1
```


 ### Question 4 :

```
[ec2-user@ip-172-31-34-253 ~]$ cd linux_ex_1
```

Résultat :

```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ 
```

 ### Question 5 :

```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ touch aqib_ahmed.txt
[ec2-user@ip-172-31-34-253 linux_ex_1]$ ls
```

Résultat :

```
aqib_ahmed.txt 
```

 ### Question 6 :

```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ mkdir notes
```

 ### Question 7 :

```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ mv aqib_ahmed.txt /home/ec2-user/linux_ex_1/notes
```

 ### Question 8 :

```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ cd notes
[ec2-user@ip-172-31-34-253 notes]$ mv aqib_ahmed.txt aqib_ahmed_2023.txt
```

 ### Question 9 :

```
[ec2-user@ip-172-31-34-253 notes]$ cd ..
[ec2-user@ip-172-31-34-253 linux_ex_1]$ cp -R notes notes_2022
```


 ### Question 10 :

```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ rm -rfv notes 
```

Résultat :

```
removed ‘notes/aqib_ahmed_2023.txt’
removed directory: ‘notes’
```


```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ ls
```

Résultat :

```
notes_2022 
```


## Exercice 3 :

### Question 1 :

```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ nano script_1.sh
```

### Question 2 :

```
Script running please wait ...
Done.
```

### Question 3 :

```
"Controle + x", "Y" for YES, "Enter" 
```

 ### Question 4 :

```
[ec2-user@ip-172-31-38-175 linux_ex_1]$ cat script_1.sh
```

Résultat :

```
Script running please wait ...
Done.

```

 ### Question 5 :

```
[ec2-user@ip-172-31-38-175 linux_ex_1]$ chmod +x script_1.sh
[ec2-user@ip-172-31-38-175 linux_ex_1]$ ./script_1.sh 
```

Résultat :

```
notes_2022/  script_1.sh 
```







## Exercice 4:1 :


### Question 1) a) :
```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ nano credentials
We wrote in the file "neymar"
ctrl+x then "Y" then enter
```

### Question 1) b) :
```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ cat credentials
```
Résultat :
```
neymar
```

### Question 1) c) :
```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ ls -l credentials
```
Résultat :
```
-rw-rw-r-- 1 ec2-user ec2-user 8 Feb 21 20:47 credentials
```

### Question 2) a) :
```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ chmod a=r credentials
[ec2-user@ip-172-31-46-16 linux_ex_1]$ ls -l credentials
```
Résultat :
```
-r--r--r-- 1 ec2-user ec2-user 8 Feb 21 20:47 credentials
```

### Question 2) b) :
```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ nano credentials
[ec2-user@ip-172-31-46-16 linux_ex_1]$ cat credentials
```
Résultat :
```
neymar 
meilleur joueur du psg
```

### Question 3) a) :

```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ chmod a+rw credentials
[ec2-user@ip-172-31-46-16 linux_ex_1]$ ls -l credentials
```
Résultat :
```
-rw-rw-rw- 1 ec2-user ec2-user 33 Feb 21 21:09 credentials
```

### Question 3) b) :

```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ nano credentials
```

### Question 3) c) :

```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ cat credentials
```


### Question 1) a) :

```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ chmod u+x credentials
[ec2-user@ip-172-31-46-16 linux_ex_1]$ ls -l credentials
```
Résultat :
```
-rwxrw-rw- 1 ec2-user ec2-user 41 Feb 21 22:35 credentials
```

### Question 2) a) :

```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ chmod o-r credentials
[ec2-user@ip-172-31-46-16 linux_ex_1]$ ls -l credentials
```
Résultat :
```
-rwxrw--w- 1 ec2-user ec2-user 45 Feb 21 22:38 credentials
```


## Exercice 4:2 :


### Question 1) :
```
[ec2-user@ip-172-31-46-16 linux_ex_1]$ cd /
```

### Question 2) a) :
```
[ec2-user@ip-172-31-46-16 /]$ sudo nano .private_file
Then we wrote inside "verratti" and crtl+x + Y + Enter
```
Résultat :
```
-rwxrw--w- 1 ec2-user ec2-user 45 Feb 21 22:38 credentials
```

### Question 2) b) :
```
[ec2-user@ip-172-31-46-16 /]$ cat .private_file
```
Résultat :
```
verrati
```

### Question 2) c) :
```
[ec2-user@ip-172-31-46-16 /]$ ls -a
```
Résultat :
```
.  ..  .autorelabel  bin  boot  dev  etc  home  lib  lib64  local  media  mnt  opt  .private_file  proc  root  run  sbin  srv  sys  tmp  usr  var
```

### Question 3) a) :

We can' write in the file 

### Question 3) b) :

We can' write in the file 


### Question 4) a) :
```
[ec2-user@ip-172-31-46-16 /]$ sudo nano .private_file
```

### Question 4) b) :
```
[ec2-user@ip-172-31-46-16 /]$ cat .private_file
```

### Question 5) a) :
```
[ec2-user@ip-172-31-46-16 /]$ sudo chmod a+rwx .private_file
```

### Question 5) b) :
```
[ec2-user@ip-172-31-46-16 /]$ cat .private_file
```


## Exercice 4:3 :


### Question 1) :
```
[ec2-user@ip-172-31-46-16 /]$ chmod 666 .private_file
```
Résultat :
```

```

### Question 2) :
```
[ec2-user@ip-172-31-46-16 /]$ chown $USER .private_file
```
Résultat :
```

```


## Exercice 4:4 :


### Question 1) :
```
[ec2-user@ip-172-31-46-16 /]$ sudo apt update
```

### Question 2) :
```
[ec2-user@ip-172-31-46-16 /]$ sudo apt upgrade
```

### Question 3) :
```
[ec2-user@ip-172-31-46-16 /]$ sudo apt install cmatrix
```

### Question 4) :
```
[ec2-user@ip-172-31-46-16 /]$ cmatrix 
```

### Question 5) :
```
[ec2-user@ip-172-31-46-16 /]$ CTRL + C
```

### Question 6) :
```
[ec2-user@ip-172-31-46-16 /]$ sudo apt install tmux
```

### Question 7) :
```
[ec2-user@ip-172-31-46-16 /]$ tmux
```

### Question 8) :
```
echo "Hello session 0"
```

### Question 9) :
```
cmatrix
```

### Question 10) :
```
Ctrl + B + D
```

### Question 11) :
```
Ctrl + B + %
```

### Question 12) :

### Question 13) :

### Question 14) :
```
tmux list-sessions
```

### Question 15) :
```
tmux attach-session -t session0
```

### Question 16) :

### Question 17) :

### Question 18) :

### Question 19) :
```
Here are the links : https://gist.github.com/mzmonsour/8791835
```

### Question 20) :
```
tmux kill-session -a
```

### Question 21) :
```
tmux list-sessions
```


## Exercice 4:5 :


### Question 1) :
```
cmatrix -h
```

### Question 2) :
```
cmatrix -C white
```

### Question 3) :
```
cmatrix -s 5
```

### Question 4) :
```
CTRL + C
```

### Question 5) :
```
cmatrix -s 5 -C blue
```

### Question 6) :
```
man cmatrix
```

### Question 7) :
```
tmux -h
```

### Question 8) :
```
man tmux
```


# TD 1_2 LINUX TOOLS

## Exercice 1 :


### Question 1) :
```
sudo apt update && sudo apt upgrade
```

### Question 2) :
```
lsb_release -a
top
htop
nproc
lscpu | grep 'Cache'
df -h
lsblk
lsusb
hostname
```

## Exercice 2 :


```
x="piri pimpin"                                          # Question 1
```
```
echo $x                                                  # Question 2
```
```
x="$x piri pimpin"                                       # Question 3
```
```
mkdir my_programs && cd my_programs                      # Question 4
```
```
echo "echo pilou pilou" > pilou                          # Question 5
```
```
bash pilou                                               # Question 6
```
```
chmod +x pilou                                           # Question 7
```
```
./pilou                                                  # Question 8
```
```
echo $PATH                                               # Question 9
```
```
export PATH="$PATH:$(pwd)"                               # Question 10
```
```
export PATH                                              # Question 11
```
```
cd ~                                                     # Question 12
```
```
pilou                                                    # Question 13
```
```
echo 'export PATH="$PATH:$(pwd)"' >> ~/.profile          # Question 14
```
```
bash                                                     # Question 15
pilou

```

## Exercice 3 :

```
touch say_hello.sh                                  # Question 1
date +"%c - Hello" >> hellos.txt                    
```
```
chmod +x say_hello.sh                               # Question 2
```
```
crontab -e                                          # Question 3
* * * * * /home/ec2-user/my_programs/say_hello.sh

systemctl status cron
```



## Exercice 4 :

```
mkdir hash_checksum                                  # Question 1
```
```
cd hash_checksum                                     # Question 2
touch .sensible_addresses .sensible_passwords       
```
```

ls                                                   # Question 3
```
```
echo '#!/bin/bash' > gentle_script.sh                # Question 4
echo 'echo "Have a good day"' >> gentle_script.sh
chmod +x gentle_script.sh
```
```
./gentle_script.sh                                   # Question 5
```
```
sha256sum gentle_script.sh > log_sha                 # Question 6
```
```
echo 'rm -f .sensible*' >> gentle_script.sh          # Question 7
```
```
sha256sum gentle_script.sh >> log_sha                # Question 8
```
```
./gentle_script.sh                                   # Question 9
```
```
ls                                                   # Question 10
```
```
cat log_shat                                         # Question 12
```



## Exercice 5 :

```
sudo apt-get install qpdf                                  # Question 1
```
```
mkdir compress && cd compress                              # Question 2
```
```
echo "Hello" > hello                                       # Question 3
```
```
zlib-flate -compress -level 1 < hello > hello.deflate && echo "hello $(wc -c < hello.deflate)" >> log_compress     # Question 4
```
```
yes Hello | head -1000 > hello_multiple                    # Question 5
```
```
zlib-flate -compress -level 1 < hello_multiple > hello_multiple.deflate && echo "hello_multiple $(wc -c < hello_multiple.deflate)" >> log_compress # 6                           
```
```
for i in $(seq 1 1000); do echo "Hello $i"; done > hello_multiple_i                     # Question 7
```
```
zlib-flate -compress -level 1 < hello_multiple_i > hello_multiple_i.deflate && echo "hello_multiple_i $(wc -c < hello_multiple_i.deflate)" >> log_compress
```
```
cat log_compress                                           # Question 9
```


# TD 2_1 LINUX GREP


## Exercice 1 :


```
ls -l /                                                                # Question 1
```
```
ls -l / | grep bin                                                     # Question 2
```
```
ls -l / | grep bin | awk '{print $5}'                                  # Question 3
```
```
ls -ld /bin | awk '{print $6, $7, $8}'                                 # Question 4
```
```
ls -ld /bin | awk '{split($6,month,"-"); print $7"-"month[2]"-"$6}'    # Question 5
```

## Exercice 2 :


```
curl https://en.wikipedia.org/wiki/List_of_cyberattacks > cyberattacks.txt                     # Question 1
```
```
grep "meta" cyberattacks.txt                                                                   # Question 2
```
```
grep -oP "meta \K\w+" cyberattacks.txt                                                         # Question 3
```
```
grep -oP "meta \K\w+" cyberattacks.txt | grep -oP "\w+"                                         # Question 4
```
```
cat cyberattacks.txt | grep -P -A1 'mw-content-text' | grep -v 'mw-content-text'                # Question 5
```
```
cat cyberattacks.txt | grep -oP '<title>\K.*(?= - Wikipedia</title>)'                           # Question 6
cat cyberattacks.txt | grep -oP '(?<=<span class="mw-headline" id=").*(?=">)' | grep -v 'toc'
```


# TD 2_3 LINUX API 


## Exercice 1.1 :

```
curl https://opendomesday.org/api/1.0/county/
curl https://opendomesday.org/api/1.0/place/2346/
curl https://opendomesday.org/api/1.0/manor/181/
```

## Exercice 1.2 :

```
curl -s 'https://opendomesday.org/api/1.0/county/' | jq '.[] | select(.name == "Derbyshire") | .places[]'
```

## Exercice 1.3 :

```
derbyshire_place_ids=$(curl -s 'https://opendomesday.org/api/1.0/county/' | jq '.[] | select(.name == "Derbyshire") | .places[]')
for id in $derbyshire_place_ids; do
  curl -s "https://opendomesday.org/api/1.0/place/${id}/" | jq '.manors[]'
done
```

## Exercice 1.4 :

```
echo "Manor ID,Geld,Ploughs" > derbyshire_manors.csv
for id in $derbyshire_place_ids; do
  place_data=$(curl -s "https://opendomesday.org/api/1.0/place/${id}/")
  manor_ids=$(echo "$place_data" | jq '.manors[]')
  for manor_id in $manor_ids; do
    manor_data=$(curl -s "https://opendomesday.org/api/1.0/manor/${manor_id}/")
    geld=$(echo "$manor_data" | jq '.geld')
    ploughs=$(echo "$manor_data" | jq '.ploughs')
    echo "${manor_id},${geld},${ploughs}" >> derbyshire_manors.csv
  done
done
```

## Exercice 1.5 :

```
awk -F, 'NR>1 {sum += $2} END {print sum}' derbyshire_manors.csv
```



# TD 3 GIT LOCAL : 



## Exercice 1 :

```
git --version                                                # Question 1
```

```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"       # Question 2
```

```
git config --list                                            # Question 3   
```

## Exercice 2 :

```
git init                                  # Question 1
```
```
ls -a                                     # Question 2
```
```
git status                                # Question 3                                   
```
```
echo "# Test repository" > readme.md      # Question 4
```
```
git status                                # Question 5
```
```
git add readme.md                         # Question 6                                   
```
```
git status                                # Question 7
```
```
git commit -m "Add readme.md file"        # Question 8
```
```
git status                                # Question 9   
```
```
git log                                   # Question 10   
```


## Exercice 3 :

```
touch main.py                              # Question 1
touch functions.py                          
```
```
git status                                 # Question 2
```
```
git add main.py                            # Question 3                                   
```
```
git status.                                # Question 4
```
```
git commit -m "Add main.py file"           # Question 5
```
```
git status                                 # Question 6                                   
```
```
git add functions.py
git commit -m "Add functions.py file"      # Question 7
```
```
git status                                 # Question 8
```
```
git log                                    # Question 9                                   
```



## Exercice 4 :

```
touch requirements.txt .gitignore .private                      # Question 1                        
```
```
git status                                                      # Question 2
```
```
git add .                                                       # Question 3                                   
```
```
git status                                                      # Question 4
```
```
git commit -m "Add requirements.txt, .gitignore, and .private"  # Question 5
```
```
git status                                                      # Question 6                                   
```
```
git log --oneline                                               # Question 7
```


## Exercice 5 :

```
touch temp.ipynb                       # Exercice 1                         
```
```
git status                             # Question 2
```
```
echo "temp.ipynb" >> .gitignore        # Question 3                                   
```
```
git status                             # Question 4
```
```
touch temp.aux temp.log                # Question 5
```
```
git status                             # Question 6                                   
```
```
echo "temp.*" > .gitignore             # Question 7
```
```
git status                             # Question 8
```
```
echo ".private/" >> .git/info/exclude  # Question 9                                   
```



## Exercice 6 :

```
echo "Dépositoire Git" >> readme.md             # Exercice 1                         
```
```
git add readme.md                               # Question 2
```
```
git diff --staged                               # Question 3                                   
```
```
git commit -m "mise à jour readme.md "          # Question 4
```
```
git diff                                        # Question 5
```
```
git diff                                        # Question 6                                   
```
```
echo "Dépositoire exercice Git" >> readme.md    # Question 7
```
```
git diff                                        # Question 8
```

## Exercice 7 :


```
rm -rf *                                     # Question 1
```
```
git checkout .                               # Question 2
```
```
cd ..                                        # Question 3
cp -R projet_git autre_projet_git
cd projet_git                                     
```
```
cd ..                                        # Question 4
rm -rf projet_git
cp -R autre_projet_git projet_git
cd projet_git                         
```
```
git restore --staged readme.md               # Question 5
```
```
git commit -a -m "Commit changes directly"   # Question 6
```
```
git log                                      # Question 7
```
```
git checkout HEAD~2                          # Question 8
```
```
git reflog                                   # Question 9
```
```
git checkout HEAD@{1}                        # Question 10
```
```
git revert HEAD~1                            # Question 11
```
```
ls                                           # Question 12
```
```
git log                                      # Question 13
```
```
git reset HEAD~2                             # Question 14
```
```
git log                                      # Question 15
```
```
git reset HEAD~2                             # Question 16
```


## Exercice 8 :


```
git config --global alias.s status                                        # Question 1
```
```
git config --global alias.co checkout                                     # Question 2
```
```
git config --global alias.b branch                                        # Question 3                                     
```
```
git config --global alias.ci commit                                       # Question 4                        
```
```
git config --global alias.dog "log --all --decorate --oneline --graph"    # Question 5
```
```
git config --global alias.dag "log --all --decorate --graph"              # Question 6
```
```
git config --global alias.list "diff-tree --no-commit-id --name-only -r"  # Question 7
```
```
git config --global alias.unstage "reset HEAD --"                         # Question 8
```
```
git config --global alias.last "log -1 HEAD"                              # Question 9
```


## Exercice 9 :


```
mkdir hashing_example                                  # Question 1
cd hashing_example
```
```
echo "Hello World" > hello_world.txt                   # Question 2
```
```
wc -c hello_world.txt                                  # Question 3                                     
```
```
cat hello_world.txt                                    # Question 4                        
```
```
sha1sum hello_world.txt                                # Question 5
```
```
git hash-object hello_world.txt                        # Question 6
```
```
echo -en "blob 11\0Hello World" > hello_world_git.txt  # Question 7
```
```
sha1sum hello_world_git.txt                            # Question 8
```


## Exercice 10 :


```
cd ..                                                                           # Question 1
rm -rf git_repository
mkdir git_repository
cd git_repository
git init
```
```
cp ../hashing_example/hello_world.txt .                                          # Question 2
cp ../hashing_example/hello_world_git.txt .
git status                             
```
```
find .git/objects                                                                # Question 3                                   
```
```
sha1=$(sha1sum hello_world_git.txt | awk '{print $1}')                           # Question 4
mkdir -p .git/objects/${sha1:0:2}                     
```
```
install using package manager                                                     # Question 5
```
```
zlib-flate -compress < hello_world_git.txt > .git/objects/${sha1:0:2}/${sha1:2}   # Question 6
```
```
git cat-file -t $sha1                                                             # Question 7
git cat-file -s $sha1
git cat-file -p $sha1                   
```
```
cd ..                                                                             # Question 8
cp -R git_repository git_repository_2
rm -rf git_repository
mkdir git_repository
cd git_repository_2
git init
```
```
cp ../hashing_example/hello_world.txt .                                            # Question 9
git add hello_world.txt
git hash-object hello_world.txt```
```
```
for i in {1..100}; do echo "Hello Mister $i" >> hello_mister.txt; done             # Question 10
```
```
git add hello_mister.txt                                                           # Question 11
new_file_size=$(git ls-files --stage hello_mister.txt | awk
```


# TD 4 GIT BRANCHES : 



## Exercice 1 :

```
git clone <repository URL>                                        
cd <repository name>
```

## Exercice 2 :

```
git checkout -b <your name>                                               
touch <your name>.txt
git add <your name>.txt
git commit -m "Added <your name>.txt file"
git push -u origin <your name>
```


## Exercice 3 :

```
git checkout master
git merge <your name>
git push origin master
```



## Exercice 4 :

```
git checkout <your name>
nano README.md
git add README.md
git commit -m "Edited README.md file"
git checkout master
git pull origin master
git merge <your name>
git add README.md
git commit -m "Resolved merge conflicts"
git push origin master
```


## Exercice 5 :

```
git checkout master
git pull origin master
cat README.md
git checkout <your name>
git merge master
git commit -m "Merged changes from master branch"
git push origin <your name>
```

## Exercice 6 :

```
git branch -d <your name>
git push origin --delete <your name>

```




## Exercice 7 :
```
git checkout master
git pull origin master
git checkout -b <your name>
nano README.md
# Git interactive rebase
## Changing Multiple Commit Messages

To modify a commit that is farther back in your history, you can use interactive rebase. This will allow you to modify any commit message, combine multiple commits into one, or split a commit into multiple commits.

My Name

git add README.md
git commit -m "Clear the whole file, removing all text."
git add README.md
git commit -m "Add a title line 'Git interactive rebase'."
git add README.md
git commit -m "Copy the first paragraph from https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History."
git add README.md
git commit -m "Add the second paragraph from the same page."
git add README.md
git commit -m "Add the first and second paragraphs from the 'Changing Multiple Commit Messages' section in the same page."
git add README.md
git commit -m "Remove the second paragraph from the file."
git add README.md
git commit -m "Add the missing title 'Changing Multiple Commit Messages'."
git add README.md
git commit -m "Add a final line with my name or alias."

git rebase -i HEAD~8

git push -u origin <your name>



```




