LINUX


# TD 1 


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


# TD 2

## Exercice 1 :


### Question 1) :
```
sudo apt update && sudo apt upgrade
```




