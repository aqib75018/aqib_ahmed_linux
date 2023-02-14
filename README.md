# esilv_gpt_test

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
"Controle + x", "Y" for YES, "Enter" and "Enter"
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


REFAIRE QUESTION 












```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ nano script_1.sh
```

In the folder :

```
neymar
```

Then :

```
"Controle + x", "Y" for YES, "Enter" and "Enter"
```

### Question 1) b) :

```
[ec2-user@ip-172-31-34-253 linux_ex_1]$ nano script_1.sh
```

Résultat :
```
neymar
```

### Question 1) c) :

```
[ec2-user@ip-172-31-38-175 linux_ex_1]$ ls -l credentials
```

Résultat :
```
-rw-rw-r-- 1 ec2-user ec2-user 8 Feb  5 15:13 credentials
```

### Question 2) a) :

```
[ec2-user@ip-172-31-38-175 linux_ex_1]$ ls -l credentials
```

Résultat :
```
-rw-rw-r-- 1 ec2-user ec2-user 8 Feb  5 15:13 credentials
```










