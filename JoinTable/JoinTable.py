################################
#Created by Szymon Stanczyk
#Date: 18.12.2019

#login: castrona_testapp
#passoword: testapps
################################

import pymysql
import subprocess
import tkinter as tk

HEIGHT = 400
WIDTH = 300

def join(username, password, var1, var2, var3, var4, var5, var6, var7, var8, var9,
         var10, var11, var12,var13, var14, var15, var16, var20, var90, varAll):

    try:
                            #("hostname", "username", "password", "database_name")
        con = pymysql.connect('s19.zbpma.pl', username, password, 'castrona_szysta')
        accept = "Login correct"
        nazwa2.config(text=accept, bg="green")

    except:
        ex = "Wrong user or password"
        nazwa2.config(text=ex, bg="red")


########################################################################################################################
    def makeSQL():
            list =[var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16, var20, var90, varAll]

            index = [[] for x in range(list.count(1))]

            table = []

            while 1 in list:
                table.append(list.index(1))
                list.remove(1)
                if 1 in list:
                    table.append(list.index(1))
                    list.remove(1)

            while len(index) is 1:
                index[0] = table[0]
                break
            while len(index) is 2:
                index[0] = table[0]
                index[1] = table[1] + 1
                break
            while len(index) is 3:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                break
            while len(index) is 4:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                break
            while len(index) is 5:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                break
            while len(index) is 6:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                break
            while len(index) is 7:

                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                break
            while len(index) is 8:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                break
            while len(index) is 9:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                break
            while len(index) is 11:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                break
            while len(index) is 12:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                index[11] = table[11] + 11
                break
            while len(index) is 13:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                index[11] = table[11] + 11
                index[12] = table[12] + 12
                break
            while len(index) is 14:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                index[11] = table[11] + 11
                index[12] = table[12] + 12
                index[13] = table[13] + 13
                break
            while len(index) is 15:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                index[11] = table[11] + 11
                index[12] = table[12] + 12
                index[13] = table[13] + 13
                index[14] = table[14] + 14
                break
            while len(index) is 16:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                index[11] = table[11] + 11
                index[12] = table[12] + 12
                index[14] = table[14] + 14
                index[13] = table[13] + 13
                index[15] = table[15] + 15
                break
            while len(index) is 17:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                index[11] = table[11] + 11
                index[12] = table[12] + 12
                index[14] = table[14] + 14
                index[13] = table[13] + 13
                index[15] = table[15] + 15
                index[16] = table[16] + 16
                break
            while len(index) is 18:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                index[11] = table[11] + 11
                index[12] = table[12] + 12
                index[14] = table[14] + 14
                index[13] = table[13] + 13
                index[15] = table[15] + 15
                index[16] = table[16] + 16
                index[17] = table[17] + 17
                break
            while len(index) is 18:
                index[0] = table[0]
                index[1] = table[1] + 1
                index[2] = table[2] + 2
                index[3] = table[3] + 3
                index[4] = table[4] + 4
                index[5] = table[5] + 5
                index[6] = table[6] + 6
                index[7] = table[7] + 7
                index[8] = table[8] + 8
                index[9] = table[9] + 9
                index[10] = table[10] + 10
                index[11] = table[11] + 11
                index[12] = table[12] + 12
                index[14] = table[14] + 14
                index[13] = table[13] + 13
                index[15] = table[15] + 15
                index[16] = table[16] + 16
                index[17] = table[17] + 17
                index[18] = table[18] + 18
                break

            condition = []

            if 0 in index[0:len(index)]:
                condition1 = 'TITLE = "I01"'
                condition.append(condition1)
            if 1 in index[0:len(index)]:
                condition2 = 'TITLE = "I02"'
                condition.append(condition2)
            if 2 in index[0:len(index)]:
                condition3 = 'TITLE = "I03"'
                condition.append(condition3)
            if 3 in index[0:len(index)]:
                condition4 = 'TITLE = "I04"'
                condition.append(condition4)
            if 4 in index[0:len(index)]:
                condition5 = 'TITLE = "I05"'
                condition.append(condition5)
            if 5 in index[0:len(index)]:
                condition6 = 'TITLE = "I06"'
                condition.append(condition6)
            if 6 in index[0:len(index)]:
                condition7 = 'TITLE = "I07"'
                condition.append(condition7)
            if 7 in index[0:len(index)]:
                condition8 = 'TITLE = "I08"'
                condition.append(condition8)
            if 8 in index[0:len(index)]:
                condition9 = 'TITLE = "I09"'
                condition.append(condition9)
            if 9 in index[0:len(index)]:
                condition10 = 'TITLE = "I10"'
                condition.append(condition10)
            if 10 in index[0:len(index)]:
                condition11 = 'TITLE = "I11"'
                condition.append(condition11)
            if 11 in index[0:len(index)]:
                condition12 = 'TITLE = "I12"'
                condition.append(condition12)
            if 12 in index[0:len(index)]:
                condition13 = 'TITLE = "I13"'
                condition.append(condition13)
            if 13 in index[0:len(index)]:
                condition14 = 'TITLE = "I14"'
                condition.append(condition14)
            if 14 in index[0:len(index)]:
                condition15 = 'TITLE = "I15"'
                condition.append(condition15)
            if 15 in index[0:len(index)]:
                condition16 = 'TITLE = "I16"'
                condition.append(condition16)
            if 16 in index[0:len(index)]:
                condition20 = 'TITLE = "I20"'
                condition.append(condition20)
            if 17 in index[0:len(index)]:
                condition90 = 'TITLE = "I90"'
                condition.append(condition90)
            if 18 in index[0:len(index)]:
                conditionAll = 'TITLE = "I01" OR TITLE = "I02" OR TITLE = "I03" OR TITLE = "I04" OR TITLE = "I05" OR TITLE = "I06" OR TITLE = "I07" OR TITLE = "I08" OR TITLE = "I09" OR TITLE = "I10" OR TITLE = "I11" OR TITLE = "I12" OR TITLE = "I13" OR TITLE = "I14" OR TITLE = "I15" OR TITLE = "I16" OR TITLE = "I20" OR TITLE = "I90"'
                condition.append(conditionAll)

            warunki = str(condition[0:len(index)])
            warunki2 = warunki.replace(',', ' OR')
            warunki3 = warunki2.replace('[', '')
            warunki4 = warunki3.replace(']', '')
            FinishCondition = warunki4.replace("'", '')

            global FinishCondition

    makeSQL()

########################################################################################################################
    try:
        SQL = "SELECT lithology.NAME, holes.X, holes.Y, lithology.symbol, holes.TITLE FROM holes, lithology where holes.ID = lithology.ID AND (" + str(FinishCondition) +")"

        with con:
            cur = con.cursor()
            cur.execute(SQL)
            rows = cur.fetchall()
            desc = cur.description
            headers = "{0} {1} {2} {3} {4}\n".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0])
            import time
            localtime = time.asctime(time.localtime(time.time()))
            time = localtime.split()
            savefile = "join_" + str(time[3].replace(":", "_")) + ".txt"
            file = open(savefile, "a")
            file.write(headers)
            for row in rows:
                joinTable = "{0} {1} {2} {3} {4}\n".format(row[0], row[1], row[2], row[3], row[4])
                file.write(joinTable)
            file.close()
        correctscript = "Correct"
        nazwa3.config(text=correctscript, bg="green")
    except:
        uncorrectScript = "Error"
        nazwa3.config(text=uncorrectScript, bg="red")


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frameText = tk.Frame(root, bd=5)
frameText.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')

nazwa2 = tk.Label(frameText)
nazwa2.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg = '#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.9, anchor='n')

nazwa = tk.Label(frame, text="User:")
nazwa.place(relx=0, rely=0, relwidth=0.5, relheight=0.1)

username = tk.Entry(frame, font=('Tahoma',12))
username.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1)

haslo = tk.Label(frame, text="Password:")
haslo.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.1)

password = tk.Entry(frame, show="*", font=('Tahoma',12))
password.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.1)

var1 = tk.IntVar()
check = tk.Checkbutton(frame, text="I01", variable=var1)
check.place(relx=0, rely=0.2, relwidth=0.33, relheight=0.1)

var2 = tk.IntVar()
check = tk.Checkbutton(frame, text="I02", variable=var2)
check.place(relx=0.335, rely=0.2, relwidth=0.33, relheight=0.1)

var3 = tk.IntVar()
check = tk.Checkbutton(frame, text="I03", variable=var3)
check.place(relx=0.67, rely=0.2, relwidth=0.33, relheight=0.1)

var4 = tk.IntVar()
check = tk.Checkbutton(frame, text="I04", variable=var4)
check.place(relx=0, rely=0.3, relwidth=0.33, relheight=0.1)

var5 = tk.IntVar()
check = tk.Checkbutton(frame, text="I05", variable=var5)
check.place(relx=0.335, rely=0.3, relwidth=0.33, relheight=0.1)

var6 = tk.IntVar()
check = tk.Checkbutton(frame, text="I06", variable=var6)
check.place(relx=0.67, rely=0.3, relwidth=0.33, relheight=0.1)

var7 = tk.IntVar()
check = tk.Checkbutton(frame, text="I07", variable=var7)
check.place(relx=0, rely=0.4, relwidth=0.33, relheight=0.1)

var8 = tk.IntVar()
check = tk.Checkbutton(frame, text="I08", variable=var8)
check.place(relx=0.335, rely=0.4, relwidth=0.33, relheight=0.1)

var9 = tk.IntVar()
check = tk.Checkbutton(frame, text="I09", variable=var9)
check.place(relx=0.67, rely=0.4, relwidth=0.33, relheight=0.1)

var10 = tk.IntVar()
check = tk.Checkbutton(frame, text="I10", variable=var10)
check.place(relx=0, rely=0.5, relwidth=0.33, relheight=0.1)

var11 = tk.IntVar()
check = tk.Checkbutton(frame, text="I11", variable=var11)
check.place(relx=0.335, rely=0.5, relwidth=0.33, relheight=0.1)

var12 = tk.IntVar()
check = tk.Checkbutton(frame, text="I12", variable=var12)
check.place(relx=0.67, rely=0.5, relwidth=0.33, relheight=0.1)

var13 = tk.IntVar()
check = tk.Checkbutton(frame, text="I13", variable=var13)
check.place(relx=0, rely=0.6, relwidth=0.33, relheight=0.1)

var14 = tk.IntVar()
check = tk.Checkbutton(frame, text="I14", variable=var14)
check.place(relx=0.335, rely=0.6, relwidth=0.33, relheight=0.1)

var15 = tk.IntVar()
check = tk.Checkbutton(frame, text="I15", variable=var15)
check.place(relx=0.67, rely=0.6, relwidth=0.33, relheight=0.1)

var16 = tk.IntVar()
check = tk.Checkbutton(frame, text="I16", variable=var16)
check.place(relx=0, rely=0.7, relwidth=0.33, relheight=0.1)

var20 = tk.IntVar()
check = tk.Checkbutton(frame, text="I20", variable=var20)
check.place(relx=0.335, rely=0.7, relwidth=0.33, relheight=0.1)

var90 = tk.IntVar()
check = tk.Checkbutton(frame, text="I90", variable=var90)
check.place(relx=0.67, rely=0.7, relwidth=0.33, relheight=0.1)

varAll = tk.IntVar()
check = tk.Checkbutton(frame, text="wszystkie", variable=(varAll))
check.place(relx=0, rely=0.8, relwidth=0.33, relheight=0.1)

nazwa3 = tk.Label(frame, text="sukces")
nazwa3.place(relx=0.5, rely=0.81, relwidth=0.5, relheight=0.09)

button = tk.Button(frame, text="Join tabels", font=('Tahoma',10), command=lambda: join(username.get(), password.get(), var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get(), var10.get(), \
var11.get(), var12.get(), var13.get(), var14.get(), var15.get(), var16.get(), var20.get(), var90.get(), varAll.get()))
button.place(relx=0.35, rely=0.9, relheight=0.1, relwidth=0.3)

root.mainloop()