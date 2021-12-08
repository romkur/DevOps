# Task 1
man 1 awk > awk_man_sect_with_env_var.txt

#Task 2
        #!/bin/bash


        touch ../task2.txt 2>> err.log
        if [ $? -eq 1 ]
        then
            echo 'Error'

        fi
        
#Task 2.2
        #!/bin/bash

        file=../task2.txt

        if [ -e "$file" ]; then
            echo "Sorry, can't create it, file already exists"
                else
                touch ../task2.txt 2> /dev/null && echo "File has been created" || echo "Your don't have permissions"

        fi
    
#Task 3.1-3.3

    //3.1-3.2
    echo /home/student/ > task3_1
    #!/bin/bash

    path="$(cat task3_1)"

    echo -n "Directories -"; ls -d "${path}"/*/ | wc -l
    echo -n "Files -"; ls -l "${path}" | grep ^- | wc -l
    
    
    
    // 3.3
    #!/bin/bash

    while read y
    do
    echo "$y"
    echo -n "Directories -"; ls -d "${y}"/* | wc -l
    echo -n "Files -"; ls -l "${y}" | grep ^- | wc -l
    done < paths.txt

#Task4 

sudo yum install tmux 
//С этим все понятно, потыкал, удобно)
