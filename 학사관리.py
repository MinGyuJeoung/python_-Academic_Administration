Slist=[]
while True:
    print("\nMain Menu")
    print("______________________")
    print('1. 달력 출력')
    print('2. 시간표')
    print('3. 일정')
    print('4. 메모장')
    print('0. 종료')
    print("______________________")
    num=int(input("메뉴를 선택하시오: "))
    if(num==0):
        print("\n종료")
        import sys
        sys.exit()
    elif(num==1):
        print("\n1. 달력 출력\n")
        year=int(input("연도를 입력하시오: "))
        month=int(input("월을 입력하시오: "))
        import calendar
        calendar.prmonth(year,month)
    elif(num==2):
        while True:
            print("\n2. 시간표 메뉴")
            print("______________________")
            print('1. 시간표 출력')
            print('2. 학점 계산기')
            print('0. 메인 메뉴로 돌아가기')
            print("______________________")
            num=int(input("메뉴를 선택하시오: "))
            if(num==0):
                print("\n메인메뉴로 돌아가기\n")
                break
            elif(num==1):
                print("\n시간표 출력\n")
                from tkinter import*
                import tkinter.messagebox

                def InfoSecEthic1():
                    tkinter.messagebox.showinfo("시간표","과 목: 정보보호윤리\n시 간: 10:00~11:50\n교 수: 이덕규\n강의실: 1자 310")
                def Programming1():
                    tkinter.messagebox.showinfo("시간표","과 목: 컴퓨터프로그래밍2\n시 간: 15:00~15:50\n교 수: 김경배\n강의실: 1자 310")
                def InfoCommTech1():
                    tkinter.messagebox.showinfo("시간표","과 목: 정보통신개론\n시 간: 16:00~17:50\n교 수: 김한수\n강의실: 1자 303")
                def Programming2():
                    tkinter.messagebox.showinfo("시간표","과 목: 컴퓨터프로그래밍2\n시 간: 09:00~12:50\n교 수: 김경배\n강의실: 컴교실습실1")
                def InfoCommTech2():
                    tkinter.messagebox.showinfo("시간표","과 목: 정보통신개론\n시 간: 10:00~10:50\n교 수: 김한수\n강의실: 1자 212")
                def InfoSecEthic2():
                    tkinter.messagebox.showinfo("시간표","과 목: 정보보호윤리\n시 간: 09:00~09:50\n교 수: 이덕규\n강의실: 1자 312")
                def ComputationalThinking():
                    tkinter.messagebox.showinfo("시간표","과 목: 문제해결과프로그래밍\n시 간: 10:00~12:50\n교 수: 손호선\n강의실: 미래전산실습실1")
                def ThinkExpress():
                    tkinter.messagebox.showinfo("시간표","과 목: 사고와표현2-말하기\n시 간: 15:00~16:50\n교 수: 전찬희\n강의실: 1자 208")
                def English():
                    tkinter.messagebox.showinfo("시간표","과 목: 영어회화1\n시 간: 11:00~12:50\n교 수: 다니엘\n강의실:글로벌관 507")
                def exit():
                    if tkinter.messagebox.askokcancel("Quit","종료하시겠습니까?"):
                        window.destroy()

                window=Tk()
                window.title("시간표")

                mon=Label(window,text="MON")                            #가로 줄 = 요일
                tue=Label(window,text="TUE")
                wed=Label(window,text="WED")
                thu=Label(window,text="THU")
                fri=Label(window,text="FRI")
                sat=Label(window,text="SAT")
                mon.grid(row=0,column=1)
                tue.grid(row=0,column=2)
                wed.grid(row=0,column=3)
                thu.grid(row=0,column=4)
                fri.grid(row=0,column=5)
                sat.grid(row=0,column=6)

                period1=Label(window,text="1교시\n09:00")               #세로 줄 = 시간
                period2=Label(window,text="2교시\n10:00")
                period3=Label(window,text="3교시\n11:00")
                period4=Label(window,text="4교시\n12:00")
                period5=Label(window,text="5교시\n13:00")
                period6=Label(window,text="6교시\n14:00")
                period7=Label(window,text="7교시\n15:00")
                period8=Label(window,text="8교시\n16:00")
                period9=Label(window,text="9교시\n17:00")
                period1.grid(row=1,column=0)
                period2.grid(row=2,column=0)
                period3.grid(row=3,column=0)
                period4.grid(row=4,column=0)
                period5.grid(row=5,column=0)
                period6.grid(row=6,column=0)
                period7.grid(row=7,column=0)
                period8.grid(row=8,column=0)
                period9.grid(row=9,column=0)

                b1=Button(window,text="정보보호윤리\n1자 310",command=InfoSecEthic1)
                b1.grid(row=2,column=1)
                b1=Button(window,text="정보보호윤리\n1자 310",command=InfoSecEthic1)
                b1.grid(row=3,column=1)

                b2=Button(window,text="컴퓨터프로그래밍2\n1자 310",command=Programming1)
                b2.grid(row=7,column=1)

                b3=Button(window,text="정보통신개론\n1자 303",command=InfoCommTech1)
                b3.grid(row=8,column=1)
                b3=Button(window,text="정보통신개론\n1자 303",command=InfoCommTech1)
                b3.grid(row=9,column=1)

                b4=Button(window,text="컴퓨터프로그래밍2\n컴교실습실1",command=Programming2)
                b4.grid(row=1,column=2)
                b4=Button(window,text="컴퓨터프로그래밍2\n컴교실습실1",command=Programming2)
                b4.grid(row=2,column=2)
                b4=Button(window,text="컴퓨터프로그래밍2\n컴교실습실1",command=Programming2)
                b4.grid(row=3,column=2)
                b4=Button(window,text="컴퓨터프로그래밍2\n컴교실습실1",command=Programming2)
                b4.grid(row=4,column=2)

                b5=Button(window,text="정보통신개론\n1자 212",command=InfoCommTech2)
                b5.grid(row=2,column=3)

                b6=Button(window,text="정보보호윤리\n1자 312",command=InfoSecEthic2)
                b6.grid(row=1,column=4)

                b7=Button(window,text="문제해결프로그래밍\n미래전산실습실1",command=ComputationalThinking)
                b7.grid(row=2,column=4)
                b7=Button(window,text="문제해결프로그래밍\n미래전산실습실1",command=ComputationalThinking)
                b7.grid(row=3,column=4)
                b7=Button(window,text="문제해결프로그래밍\n미래전산실습실1",command=ComputationalThinking)
                b7.grid(row=4,column=4)

                b8=Button(window,text="사고와표현2-말하기\n1자 208",command=ThinkExpress)
                b8.grid(row=7,column=4)
                b8=Button(window,text="사고와표현2-말하기\n1자 208",command=ThinkExpress)
                b8.grid(row=8,column=4)

                b9=Button(window,text="영어회화1\n글 507",command=English)
                b9.grid(row=3,column=5)
                b9=Button(window,text="영어회화1\n글 507",command=English)
                b9.grid(row=4,column=5)

                b10=Button(window,text="시간표 메뉴로 돌아가기",command=exit)
                b10.grid(row=10,column=3)

                window.mainloop()

            elif(num==2):
                from tkinter import*
                import tkinter.messagebox

                def calculate():
                    s1=float(o1.get(scores.get(score)))                                                         #get()  s=점수, cr=학점
                    s2=float(o2.get(scores.get(score)))                                                         #scores.get((score))= 딕션너리에서 학점을 float으로 변환
                    s3=float(o3.get(scores.get(score)))
                    s4=float(o4.get(scores.get(score)))
                    s5=float(o5.get(scores.get(score)))
                    s6=float(o6.get(scores.get(score)))
                    s7=float(o7.get(scores.get(score)))
                    s8=float(o8.get(scores.get(score)))
                    cr1=float(e9.get())
                    cr2=float(e10.get())
                    cr3=float(e11.get())
                    cr4=float(e12.get())
                    cr5=float(e13.get())
                    cr6=float(e14.get())
                    cr7=float(e15.get())
                    cr8=float(e16.get())

                    scr=s1*cr1+s2*cr2+s3*cr3+s4*cr4+s5*cr5+s6*cr6+s7*cr7+s8*cr8                                 #totalAverage= 총평점
                    crSum=cr1+cr2+cr3+cr4+cr5+cr6+cr7+cr8                                                       #scr= 총점
                    totalAverage=scr/crSum                                                                      #crSum= 총학점, 이수학점
                    e17.insert(0,str(totalAverage))
                    e19.insert(0,str(crSum))
                def exit():
                    if tkinter.messagebox.askokcancel("Quit","종료하시겠습니까?"):
                        window.destroy()

                    #if chk.get()==1: 체크됨          #문제점: 체크된 과목만 전공평점, 전공이수를 계산 or 체크되지 않은 과목의 점수는 0
                                                      #해결방안: 전체의 값을 배열로 만들어야 한다.

                window= Tk()
                window.title("학점계산기")

                l1=Label(window,text="과목")
                l2=Label(window,text="점수")
                l3=Label(window,text="학점")
                l4=Label(window,text="전공")
                l1.grid(row=0,column=0)
                l2.grid(row=0,column=1)
                l3.grid(row=0,column=2)
                l4.grid(row=0,column=3)

                e1=Entry(window)                                                                                 #과목
                e2=Entry(window)
                e3=Entry(window)
                e4=Entry(window)
                e5=Entry(window)
                e6=Entry(window)
                e7=Entry(window)
                e8=Entry(window)
                e1.grid(row=1,column=0)
                e2.grid(row=2,column=0)
                e3.grid(row=3,column=0)
                e4.grid(row=4,column=0)
                e5.grid(row=5,column=0)
                e6.grid(row=6,column=0)
                e7.grid(row=7,column=0)
                e8.grid(row=8,column=0)

                                                                                                                     #점수
                scores={'A+':4.5,'A':4.0,'B+':3.5,'B':3.0,'C+':2.5,'C':2.0,'D+':1.5,'D':1.0,'F':0}               #딕셔너리
                score=StringVar()
                score.set(None)                                                                                  #문제점: 하나의 값을 입력하면 모든 값이 입력된다. 
                                                                                                                     # select() 함수 구현 ==> 학점 목록에 값을 할당 
                o1=OptionMenu(window,score,*scores)                                                              #예 1-A+ 2-A 3-B+ ...
                o2=OptionMenu(window,score,*scores)                                                              #select.select_by_value('1')
                o3=OptionMenu(window,score,*scores)
                o4=OptionMenu(window,score,*scores)
                o5=OptionMenu(window,score,*scores)
                o6=OptionMenu(window,score,*scores)
                o7=OptionMenu(window,score,*scores)
                o8=OptionMenu(window,score,*scores)
                o1.grid(row=1,column=1)
                o2.grid(row=2,column=1)
                o3.grid(row=3,column=1)
                o4.grid(row=4,column=1)
                o5.grid(row=5,column=1)
                o6.grid(row=6,column=1)
                o7.grid(row=7,column=1)
                o8.grid(row=8,column=1)

                e9=Entry(window)                                                                                   #학점
                e10=Entry(window)
                e11=Entry(window)
                e12=Entry(window)
                e13=Entry(window)
                e14=Entry(window)
                e15=Entry(window)
                e16=Entry(window)
                e9.grid(row=1,column=2)
                e10.grid(row=2,column=2)
                e11.grid(row=3,column=2)
                e12.grid(row=4,column=2)
                e13.grid(row=5,column=2)
                e14.grid(row=6,column=2)
                e15.grid(row=7,column=2)
                e16.grid(row=8,column=2)

                chk=IntVar()
                c1=Checkbutton(window,variable=chk)                                                                 #전공
                c2=Checkbutton(window,variable=chk)
                c3=Checkbutton(window,variable=chk)
                c4=Checkbutton(window,variable=chk)
                c5=Checkbutton(window,variable=chk)
                c6=Checkbutton(window,variable=chk)
                c7=Checkbutton(window,variable=chk)
                c8=Checkbutton(window,variable=chk)
                c1.grid(row=1,column=3)
                c2.grid(row=2,column=3)
                c3.grid(row=3,column=3)
                c4.grid(row=4,column=3)
                c5.grid(row=5,column=3)
                c6.grid(row=6,column=3)
                c7.grid(row=7,column=3)
                c8.grid(row=8,column=3)

                l5=Label(window,text="총평점")                                                                     #계산 결과
                l6=Label(window,text="전공평점")
                l7=Label(window,text="이수학점")
                l8=Label(window,text="전공이수")
                l5.grid(row=11,column=0)
                l6.grid(row=11,column=1)
                l7.grid(row=11,column=2)
                l8.grid(row=11,column=3)

                e17=Entry(window)
                e18=Entry(window)
                e19=Entry(window)
                e20=Entry(window)
                e17.grid(row=12,column=0)
                e18.grid(row=12,column=1)
                e19.grid(row=12,column=2)
                e20.grid(row=12,column=3)

                b1=Button(window,text="시간표 메뉴로 돌아가기",command=exit)                                        #돌아가기 버튼
                b2=Button(window,text="계산",command=calculate)                                                     #계산 버튼
                b1.grid(row=13,column=2)
                b2.grid(row=10,column=2)

                window.mainloop()

                
            else:
                print("\n%d는없는 번호입니다.\n"%num)
                
    elif(num==3):
        while True:
            print("\n3. 일정 메뉴")
            print("______________________")
            print('1. 최근 일정')
            print('2. 일정 추가')
            print('3. 일정 삭제')
            print('4. 일정 변경')
            print('0. 메인 메뉴로 돌아가기')
            print("______________________")
            num=int(input("메뉴를 선택하시오: "))
            if(num==0):
                print("\n메인메뉴로 돌아가기\n")
                break
            elif(num==1):
                if not Slist:
                    print("\n저장된 값이 없음\n")
                else:
                    print(schedule,end="\n \n")
            elif(num==2):
                schedule=str(input("\n일정을 입력하시오: "))
                Slist.append(schedule)
                print("\n%s 추가합니다.\n"%schedule)
            elif(num==3):
                schedule=str(input("\n일정을 입력하시오: "))
                Slist.pop(schedule)
                print("\n%s 삭제합니다.\n"%schedule)
            elif(num==4):
                schedule=str(input("\n일정을 입력하시오: "))
                Slist[num]=schedule
                print("\n%d를 %s로 변경합니다.\n"%(num,schedule))
            else:
                print("\n%d는없는 번호입니다.\n"%num)
                
    elif(num==4):
        print("\n4. 메모장\n")
        from tkinter import*
        import tkinter.messagebox
        import tkinter.filedialog

        def open():
            file=tkinter.filedialog.askopenfile(parent=window, mode='r')
            if file !=None:
                lines = file.read()
                text.insert('1.0',lines)                            #1.0은 1번째 행, 0번째 글자를 의미한다.
                file.close()

        def save():
            file = tkinter.filedialog.asksaveasfile(parent=window, mode='w')
            if file !=None:
                lines = text.get('1.0', END+'-1c')                  #Text 위젯에 입력된 내용을 얻을때 사용한다.
                file.write(lines)                                   #맨끝에서 한 문자만 제거하라는 의미
                file.close()

        def exit():
            if tkinter.messagebox.askokcancel("Quit","종료하시겠습니까?"):
                window.destroy()

        def about():
            label=tkinter.messagebox.showinfo("About","201711424 정민규")

        window= Tk()
        window.title("메모장")
        text = Text(window, height=30, width=80)
        text.pack()

        menu = Menu(window)
        window.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="파일",menu=filemenu)
        filemenu.add_command(label="열기",command=open)
        filemenu.add_command(label="저장하기",command=save)
        filemenu.add_command(label="메인 메뉴로 돌아가기",command=exit)
        helpmenu=Menu(menu)
        menu.add_cascade(label="도움말", menu=helpmenu)
        helpmenu.add_command(label="프로그램 정보", command=about)

        window.mainloop()    
        
    else:
        print("\n%d 는 없는 번호입니다.\n"%num)
