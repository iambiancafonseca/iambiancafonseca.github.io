---
title: "Bash Scripting"
date: 2025-05-24 02:40:00 +0100
categories: [Learning, Scripting]
tag: [Beginner, Bash,TryHackMe, Scripting]
description: This post introduces the basics of Bash scripting, including how to comment code, declare variables, accept arguments, use arrays and apply conditionals. It includes hands-on examples and explanations.
---

**Difficulty:** Easy  
**Subscription:** Free  
Click [here](https://tryhackme.com/room/bashscripting) to access the room

---
> **Note**: This write-up is a concise guide meant to complement the TryHackMe Bash Scripting room. It is not a comprehensive theoretical resource but rather a practical walkthrough of key concepts and tasks. For deeper explanations, refer to the room materials or other Bash documentation.

## Room Setup

Use the TryHackMe AttackBox or your own terminal.

---
## 🧩 Tasks Breakdown
### Task 2

#### ❓ What piece of code can we insert at the start of a line to comment out our code?

**Answer:** `#`

**Explanation:**  *Bash* ignores everything written on the line after the hash mark (`#`), but as for every rule there is an exception, the exception here is when the first line of the script starts with the `#!` characters (the so-called *Shebang*). The *Shebang* is what tells the operating system which interpreter to use to parse the rest of the file.


#### ❓ What will the following script output to the screen, `echo “BishBashBosh”`
**Answer:**  BishBashBosh

**Explanation:**  `echo` does exactly what it promises, it echoes your words back! ![](/assets/images/echo.gif)

### Task 3

#### ❓ What would this code return?
```bash
name="Jammy"

age=21

echo "$name is $age years old"

city="Paris"

country="France"
```
**Answer:**  Jammy is 21 years old

**Explanation:**  This code assigns values to four variables (`name=“Jammy”`, `age=21`, `city=“Paris”` and `country=“France”`). The only visible action is the echo command, which uses the name and age variables. When we run the script, these variables get replaced with their values and so we get that Jammy is 21 years old.

#### ❓ How would you print out the city to the screen?
**Answer:**  `echo $city`

**Explanation:**  Remember that the echo command behaves very similarly to the print function in *Python*.

#### ❓ How would you print out the country to the screen?
**Answer:**  `echo $country`

**Explanation:**  Exactly the same line of thought as the question above :)

### Task 4
<small>Check out the [Bonus](#bonus) section for some examples of the scripts they encouraged us to experiment with!</small>
#### ❓ How can we get the number of arguments supplied to a script?
**Answer:**  `$#`

**Explanation:**  Think of `#` as short for "how many", so `$#` gives us the total number of arguments passed to the script (the script name is not included). <ins>Friendly reminder</ins>: if you are only using `read` and nothing was passed when running the script, `$#` will be 0, as it only counts arguments passed at runtime, not interactive input collected inside the script. As an example, if you were to count the number of arguments supplied to [script 1](#code-snippet-1), you would get 3, but if you were to do the same thing for [script 2](#code-snippet-2), you would get 0.

#### ❓ How can we get the filename of our current script(aka our first argument)?
**Answer:**  `$0`

**Explanation:**  `$0` is the way and regarding its format, I found [this discussion](https://unix.stackexchange.com/questions/119929/will-0-always-include-the-path-to-the-script) very interesting. 

#### ❓ How can we get the 4th argument supplied to the script?
**Answer:**  `$4`

**Explanation:**  Example: with `./some_script.sh parameters can seem complicated`, the 4th argument would be "complicated" (wink wink)

#### ❓ If a script asks us for input how can we direct our input into a variable called ‘test’ using “read”
**Answer:**  `read test`

**Explanation:**  Check the [read manual](https://ss64.com/bash/read.html).

#### ❓ What will the output of "`echo $1 $3`" if the script was ran with “./script.sh hello hola aloha”
**Answer:**  hello aloha

**Explanation:**  `$1` and `$3` refer to the first and third arguments passed to the script, in that order. Here, that means "hello" and "aloha".


### Task 5
`cars=('honda' 'audi' 'bmw' 'tesla')`
#### ❓ What would be the command to print audi to the screen using indexing.
**Answer:**  `echo "${cars[1]}"`

**Explanation:**  In *Bash*, arrays are zero-indexed. `cars[0] = "honda"`, `cars[1] = "audi"`, `cars[2] = "bmw"`, `cars[3] = "tesla"`

#### ❓ If we wanted to remove tesla from the array how would we do so?
**Answer:**  `unset cars[3]`

**Explanation:**  Removing an item from an array is done with `unset`.

#### ❓ How could we insert a new value called toyota to replace tesla?
**Answer:**  `cars[3]='toyota'`

**Explanation:**  To change an item in the cars array at a specific position, we use `cars[index]='value'`.

### Task 6
#### ❓ What is the flag to check if we have read access to a file?
**Answer:**  `-r`

**Explanation:**  See [this](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html) list of flags and their uses.

#### ❓ What is the flag to check to see if it's a directory?
**Answer:**  `-d`

**Explanation:**  Check link above.
## Bonus
##### Code Snippet 1
> A little biography maker that takes name, age and job as parameters when you run the script, stores them in variables and prints the bio.

```bash
#!/bin/bash

name=$1
age=$2
job=$3

echo "Hi, I'm $1, I'm $2 and I'm a $3! :)"
```

##### Code Snippet 2
> Same idea as the one above, but interactive.

```bash
#!/bin/bash

echo Enter your name
read name

echo Enter your age
read age

echo Enter you job
read job

echo "Hi, I'm $name, I'm $age and I'm a $job! :)"
```

##### Code Snippet 3
> Upgrading [Code Snippet 1](#code-snippet-1) by introducing arrays. Now it loops through multiple people, storing names, ages and jobs in arrays and printing the bio for each one.

```bash
#!/bin/bash

names=('Bianca' 'Mohammed' 'Yan' 'Maria')
age=(21 17 34 25)
job=('System Dev Engineer' 'Student' 'Cook' 'Data Scientist')

for index in ${!names[@]}; do
  echo "Hi, I'm ${names[$index]}, I'm ${age[$index]} and I'm a ${job[$index]}! :)"
done
```

##### Code Snippet 4
> Building on top of [Code Snippet 2](#code-snippet-2), this script uses an if/else statement to check the user's age. If the age is under 18, it prints a message saying the user is not eligible for work. If the age is 18 or over, it asks for their job and prints a personalized message.

```bash
#!/bin/bash

echo Enter your name
read name

echo Enter your age
read age

if [ $age -lt 18 ]
then
        echo "$name, you are not eligible for work!"
else
        echo Enter your job
        read job

        echo "Hi $name, we have a vacancy for the position of $job! :)"
fi
```

## Confusion.log
#### 💭 *Bash* is a scripting language, what other languages are there?

**Answer:** Besides *Bash*, other notable scripting languages include *AWK*, *Groovy*, *Windows PowerShell*, etc. You can check out a fuller list [here](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type#Scripting_languages).

#### 💭 To `.sh` or Not to `.sh`?
**Answer:** When I was creating the [first script](#code-snippet-1), I just named it biography. No extension. No second thoughts. Then I looked around the [TryHackMe :p] room and noticed that all files were in the format file.sh and I thought “waaaaaait... why is my script working then?”. There’s a really nice [Reddit thread](https://www.reddit.com/r/linuxquestions/comments/m2vy4b/what_is_the_point_of_using_sh_for_scripts/) that answers this , but here's the TL;DR: the file extension doesn’t matter to the shell. As long as there is a valid *Shebang* line at the top (such as `#!/bin/bash`)!!! Using `.sh` is a convention, not a requirement. It helps humans know it's a shell script. Unix-like systems (Linux, macOS) don't use file extensions to determine how to run a file (unlike Windows).

## Bumps and Bruises
##### ❗️ Never leave a space between the variable name, the ”=” and the value.
```bash
# WRONG:
name = "John"
# RIGHT:
name="John"
```
##### ❗️ Never forget to give running permissions to your script.
`chmod +x your_script.sh`
##### ❗️ Quoting variables when echoing or using them avoids surprises with spaces or special characters.
`echo "$name"`

<div style="text-align: center; font-size: 1.5em; opacity: 0.6;">
  Congrats, you survived my first write-up! Any feedback is welcome! :))
</div>
![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmRvZHI0dWo3Z3Azemxxa3JraTB4bDM2ZnZzZTR1bXI1NXU3d3NweSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g9582DNuQppxC/giphy.gif)
<div style="text-align: center; font-size: 1em;">
  Thank you and see you soon!
</div>

<div style="text-align: center; font-size: 0.8em; opacity: 0.6;">
  Join the <a href="#" data-eo-form-toggle-id="bf3ab678-3118-11f0-9f74-59c668a2a47a" 
    style="color: #007acc; text-decoration: underline; cursor: pointer; opacity: 1;"
  >mailing list</a> so you never miss me confidently running a command I absolutely shouldn’t.
</div>

<script>
  if (!window.__eo_script_loaded) {
    window.__eo_script_loaded = true;
    const s = document.createElement("script");
    s.src = "https://eocampaign1.com/form/bf3ab678-3118-11f0-9f74-59c668a2a47a.js";
    s.setAttribute("data-form", "bf3ab678-3118-11f0-9f74-59c668a2a47a");
    s.async = true;
    document.body.appendChild(s);
  }
</script>