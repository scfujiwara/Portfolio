import random
import tkinter as tk
from tkinter import ttk
import tkinter 
from tkinter import messagebox
from tkinter import *
import tkinter.messagebox
import keyboard
import time


#ゲーム画面の表示
root_main = tk.Tk()
root_main.geometry("850x500")
root_main.title("脳トレゲーム")
                                                                                                                                                                                    
#総合得点の初期化
totalpoint = 0

#ゲームレベルの初期化
gamelevel = 0

#設定反映値の初期化
rankoption = 0
nextquestions = 0
getpoint = 0
crearmessage = 0
uncrearmessage = 0
scoreup = 0
scoredown = 0
nextmessage = 0
endmessage = 0

#ゲーム画面の文字（タイトル）
label_gametitle = tk.Label(root_main, text = "足し算ゲーム", font = ("Helvetica",36))
label_gametitle.place(x = 275, y = 20)

#ゲーム画面の文字（+）
label_plus = tk.Label(root_main, text = "+", font = ("Helvetica",36))
label_plus.place(x = 220, y = 190)

#ゲーム画面の文字（=）
label_equal = tk.Label(root_main, text = "=", font = ("Helvetica",36))
label_equal.place(x = 370, y = 190)

#ゲーム画面の文字（点）
label_point = tk.Label(root_main, text = "点", font = ("Helvetica",36))
label_point.place(x = 700, y = 190)

#ゲーム画面の文字（レベル）
label_point = tk.Label(root_main, text = "レベル", font = ("Helvetica",20))
label_point.place(x = 590, y = 290)


#ゲーム画面の説明文_その１
label_wait = tk.Label(root_main, text = "式が出るのを待ちます（自分で入力しない）。", font = ("Helvetica",10))
label_wait.place(x = 100, y = 250)

#ゲーム画面の説明文_その２
label_enter = tk.Label(root_main, text = "答えの数字を入れたらエンターキーを押してください。", font = ("Helvetica",10))
label_enter.place(x = 420, y = 250)

#ゲーム画面のテキストボックス(左)
editbox_left = tk.Entry(width = 4,font =("Helvetica",28))
editbox_left.place(x = 120,y = 200)

#ゲーム画面のテキストボックス(右)
editbox_right = tk.Entry(width = 4,font =("Helvetica",28))
editbox_right.place(x = 270,y = 200)

#ゲーム画面のテキストボックス(回答)
editbox_answer = tk.Entry(width = 4,font =("Helvetica",28))
editbox_answer.place(x = 420,y = 200)



#設定画面の処理
def optionbtn_click():
    #設定画面のウィンドウ
    root_option = tk.Tk()
    root_option.title("設定")
    
    canvas = tk.Canvas(root_option, width=600, height=600)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    frame = ttk.Frame(canvas)
    frame.pack(fill=tk.BOTH, expand=True, anchor='w')


    #スクロールバーの設置
    scrollbar = ttk.Scrollbar(root_option, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    #ラジオボタンのラベルをリスト化
    radio_text_rankoption = ['デフォルト', '先の数字を「20未満に変える」', '先の数字も後の数字も「20未満に変える」', '先の数字を「50未満」、後の数字を「10未満」に変える','先の数字をレベルに応じて可変（数字を(z*10)に変えます）、後の数字を「10未満」に変える', '先の数字も後の数字もレベルに応じて可変']
    radio_text_nextquestion = ['デフォルト','2秒空ける','1秒空ける','0.5秒空ける','0.2秒空ける']
    radio_text_getpoint = ['デフォルト','正解メッセージを 正解！ にする','正解メッセージを 正解！、不正解メッセージを 不正解！ にする','正解メッセージを Good!、不正解メッセージを Bad! にする','正解メッセージを いいね！、不正解メッセージを 残念！ にする','任意の言葉にする']
    radio_text_scoreup = ['デフォルト','正解の加点を10点にする','正解の加点を5点にする']
    radio_text_scoredown = ['デフォルト','不正解の減点を3点にする','不正解の減点を5点にする','不正解の減点を20点にする','不正解の減点をしない']
    radio_text_nextmessage = ['デフォルト','継続メッセージを「レベルアップ！」にする','継続メッセージを「レベルが1つ上がりました」にする','継続メッセージを表示しない']
    radio_text_endmessage = ['デフォルト','終了メッセージを「ゲームを終了します」にする','終了メッセージを「お疲れ様でした」にする','終了メッセージを表示しない']
    #ラジオボタンの状態
    radio_var_rankoption = tkinter.StringVar()
    radio_var_nextquestion = tk.StringVar()
    radio_var_getpoint = tk.StringVar()
    radio_var_scoreup = tk.StringVar()
    radio_var_scoredown = tk.StringVar()
    radio_var_nextmessage = tk.StringVar()
    radio_var_endmessage = tk.StringVar()
    radio_var_rankoption = tkinter.StringVar(root_option)
    radio_var_nextquestion = tkinter.StringVar(root_option)
    radio_var_getpoint = tkinter.StringVar(root_option)
    radio_var_scoreup = tkinter.StringVar(root_option)
    radio_var_scoredown = tkinter.StringVar(root_option)
    radio_var_nextmessage = tkinter.StringVar(root_option)
    radio_var_endmessage = tkinter.StringVar(root_option)
    radio_var_rankoption.set(0)

    

    #桁数の設定
    label_rankoption = ttk.Label(frame, text = "『桁数の設定』", font = ("Helvetica",15))
    label_rankoption.pack(padx = 0, pady = 5)
    
    radio_rankoptions = []
    for i in range(len(radio_text_rankoption)):
        radio_rankoptions.append(ttk.Radiobutton(frame, value=radio_text_rankoption[i], variable=radio_var_rankoption, text = radio_text_rankoption[i]))
        radio_rankoptions[i].pack(padx=50, pady=0+ (i))

    radio_var_rankoption.set("デフォルト")

 

    #次の出題までの秒数の設定
    label_nextquestion = ttk.Label(frame, text = "『次の出題までの秒数』", font = ("Helvetica",15))
    label_nextquestion.pack(padx = 30, pady = 10)

    radio_nextquestions = []

    for i in range(len(radio_text_nextquestion)):
        radio_nextquestions.append(ttk.Radiobutton(frame, value=radio_text_nextquestion[i], variable=radio_var_nextquestion, text=radio_text_nextquestion[i]))
        radio_nextquestions[i].pack(padx=50, pady=0 + (i))

    radio_var_nextquestion.set("デフォルト")



    #1問ごとの採点
    label_getpoint = ttk.Label(frame, text = "『1問ごとの採点』", font = ("Helvetica",15))
    label_getpoint.pack(padx = 30, pady = 10)

    radio_getpoints = []

    for i in range(len(radio_text_getpoint)):
        radio_getpoints.append(ttk.Radiobutton(frame, value=radio_text_getpoint[i], variable=radio_var_getpoint, text=radio_text_getpoint[i]))
        radio_getpoints[i].pack(padx=50, pady=0 + (i))

    radio_var_getpoint.set("デフォルト")



    #正解メッセージのテキストボックス
    label_crearmessage = ttk.Label(frame, text = "『正解メッセージ』", font = ("Helvetica",10))
    label_crearmessage.pack(padx = 10, pady = 0)
    editbox_optionleft = ttk.Entry(frame,width = 12,font =("Helvetica",10))
    editbox_optionleft.pack(padx = 50,pady = 10)
    


    #不正解メッセージのテキストボックス
    label_uncrearmessage = ttk.Label(frame, text = "『不正解メッセージ』", font = ("Helvetica",10))
    label_uncrearmessage.pack(padx = 10, pady = 10)
    editbox_optionright = ttk.Entry(frame,width = 12,font =("Helvetica",10))
    editbox_optionright.pack(padx = 50,pady = 0)



    #正解時のスコアの設定
    label_scoreup = ttk.Label(frame, text = "『正解のスコアアップ』", font = ("Helvetica",15))
    label_scoreup.pack(padx = 30, pady = 10)

    radio_scoreups = []

    for i in range(len(radio_text_scoreup)):
        radio_scoreups.append(ttk.Radiobutton(frame, value=radio_text_scoreup[i], variable=radio_var_scoreup, text=radio_text_scoreup[i]))
        radio_scoreups[i].pack(padx=50, pady=0 + (i))

    radio_var_scoreup.set("デフォルト")



    #不正解時のスコアの設定
    label_scoredown = ttk.Label(frame, text = "『不正解のスコアダウン』", font = ("Helvetica",15))
    label_scoredown.pack(padx = 30, pady = 10)

    radio_scoredowns = []

    for i in range(len(radio_text_scoredown)):
        radio_scoredowns.append(ttk.Radiobutton(frame, value=radio_text_scoredown[i], variable=radio_var_scoredown, text=radio_text_scoredown[i]))
        radio_scoredowns[i].pack(padx=50, pady=0 + (i))
    
    radio_var_scoredown.set("デフォルト")
    


    #継続メッセージの設定
    label_nextmessage = ttk.Label(frame, text = "『満点処理：継続メッセージ』", font = ("Helvetica",15))
    label_nextmessage.pack(padx = 30, pady = 10)

    radio_nextmessages = []

    for i in range(len(radio_text_nextmessage)):
        radio_nextmessages.append(ttk.Radiobutton(frame, value=radio_text_nextmessage[i], variable=radio_var_nextmessage, text=radio_text_nextmessage[i]))
        radio_nextmessages[i].pack(padx=50, pady=0 + (i))
    
    radio_var_nextmessage.set("デフォルト")
    


    #終了メッセージの設定    
    label_endmessage = ttk.Label(frame, text = "『満点処理：終了メッセージ』", font = ("Helvetica",15))
    label_endmessage.pack(padx = 30, pady = 10)

    radio_endmessages = []

    for i in range(len(radio_text_endmessage)):
        radio_endmessages.append(ttk.Radiobutton(frame, value=radio_text_endmessage[i], variable=radio_var_endmessage, text=radio_text_endmessage[i]))
        radio_endmessages[i].pack(padx=50, pady=0 + (i))
    
    radio_var_endmessage.set("デフォルト")
    

    #ダミーメッセージの設定    
    label_dummy = ttk.Label(frame, text = "", font = ("Helvetica",15))
    label_dummy.pack(padx = 0, pady = 100)

    #設定の反映
    def close_window():
        global rankoption
        rankoption = radio_var_rankoption.get()
        print(f"桁数の設定:『{rankoption}』") 
        global nextquestions
        nextquestions = radio_var_nextquestion.get()
        print(f"次の出題までの秒数:『{nextquestions}』") 
        global getpoint
        getpoint = radio_var_getpoint.get()
        print(f"1問ごとの採点:『{getpoint}』") 
        global crearmessage
        global uncrearmessage
        crearmessage = editbox_optionleft.get()
        uncrearmessage = editbox_optionright.get()
        print(f"正解は{crearmessage}であり、不正解は{uncrearmessage}です。") 
        global scoreup
        scoreup = radio_var_scoreup.get()
        print(f"正解のスコアアップ:『{scoreup}』") 
        global scoredown
        scoredown = radio_var_scoredown.get()
        print(f"不正解のスコアダウン:『{scoredown}』") 
        global nextmessage
        nextmessage = radio_var_nextmessage.get()
        print(f"継続メッセージ:『{nextmessage}』")
        global endmessage
        endmessage = radio_var_endmessage.get()
        print(f"終了メッセージ:『{endmessage}』")

        #設定画面を反映して閉じる。
        root_option.destroy()
    
    #設定反映をせずに閉じる
    def cancel_window():
        root_option.destroy()


    #決定ボタン
    button_decision = tk.Button(frame,text = "OK",font =("Helvetica",28), command=close_window)
    button_decision.pack()
    button_decision.place(x = 100,y = 1300)

    #キャンセルボタン
    button_cancel = tk.Button(frame,text = "キャンセル",font =("Helvetica",28), command=cancel_window)
    button_cancel.pack()
    button_cancel.place(x = 300,y = 1300)

    frame.update_idletasks()  # フレームのサイズを更新
    canvas.config(scrollregion=canvas.bbox("all"))

    
    #画面表示
    root_option.mainloop()


#設定ボタン
button_option = tk.Button(root_main,text = "設定",fg = "#cd5c5c",command= optionbtn_click)
button_option.place(x = 810,y = 0)



#ゲーム内の処理
def startbtn_click():
    #テキストボックス内の数字の初期化
    editbox_left.delete(0, tkinter.END)
    editbox_right.delete(0, tkinter.END)
    editbox_answer.delete(0, tkinter.END)


    #ゲームレベルの配置
    global gamelevel
    gamelevel = 1

    #ゲーム画面の文字（レベル）
    label_point = tk.Label(root_main, text = gamelevel, font = ("Helvetica",20))
    label_point.place(x = 700, y = 290)

    #回答時のメッセージの設定
    global crearmessage
    global uncrearmessage

    if getpoint == "デフォルト"or getpoint == 0:
        crearmessage = "当たり！"
        uncrearmessage = "はずれ！"
    
    if getpoint == "正解メッセージを 正解！ にする":
        crearmessage = "正解！"
        uncrearmessage = "はずれ！"
    
    if getpoint == "正解メッセージを 正解！、不正解メッセージを 不正解！ にする":
        crearmessage = "正解！"
        uncrearmessage = "不正解！"

    if getpoint == "正解メッセージを Good!、不正解メッセージを Bad! にする":
        crearmessage = "Good!"
        uncrearmessage = "Bad!"
    
    if getpoint == "正解メッセージを いいね！、不正解メッセージを 残念！ にする":
        crearmessage = "いいね！"
        uncrearmessage = "残念！"

    
        


    #問題作成
    if rankoption == "デフォルト"or rankoption == 0:
        editbox_left.insert(tkinter.END,random.randint(0,9))
        editbox_right.insert(tkinter.END,random.randint(0,9))
    
    if rankoption == "先の数字を「20未満に変える」":
        editbox_left.insert(tkinter.END,random.randint(0,19))
        editbox_right.insert(tkinter.END,random.randint(0,9))
    
    if rankoption == "先の数字も後の数字も「20未満に変える」":
        editbox_left.insert(tkinter.END,random.randint(0,19))
        editbox_right.insert(tkinter.END,random.randint(0,19))
    
    if rankoption == "先の数字を「50未満」、後の数字を「10未満」に変える":
        editbox_left.insert(tkinter.END,random.randint(0,49))
        editbox_right.insert(tkinter.END,random.randint(0,9))
    
    if rankoption == "先の数字をレベルに応じて可変（数字を(z*10)に変えます）、後の数字を「10未満」に変える":
        editbox_left.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
        editbox_right.insert(tkinter.END,random.randint(0,9))

    if rankoption == "先の数字も後の数字もレベルに応じて可変":
        editbox_left.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
        editbox_right.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
    
    #得点の初期化
    global totalpoint
    totalpoint = 0
    label_point = tk.Label(root_main, text = "　　　　　　　　"+"\033", font = ("Helvetica",36))
    label_point.place(x = 550, y = 190)
    label_point = tk.Label(root_main, text = "点", font = ("Helvetica",36))
    label_point.place(x = 700, y = 190)


    

    def on_enter_press(event): 
            #ここで合計得点の変数を宣言。
            global totalpoint
            global gamelevel
            answer = 0
            if event.name == 'enter':
                #正しい答えの生成
                answer = int(editbox_answer.get())
                label_answer = tk.Label(root_main, text = "", font = ("Helvetica",36))
                left = int(editbox_left.get())
                right = int(editbox_right.get())
                Correct_answer = left + right

                label_point = tk.Label(root_main, text = "　　　　　　　　"+"\033", font = ("Helvetica",36))
                label_point.place(x = 550, y = 190)
                label_point = tk.Label(root_main, text = "点", font = ("Helvetica",36))
                label_point.place(x = 700, y = 190)
                
                #成否判定
                if answer == Correct_answer:
                    label_answer = tk.Label(root_main, text = crearmessage, font = ("Helvetica",36))
                    label_answer.place(x = 550, y = 130)
                    
                    if scoreup == "デフォルト"or scoreup == 0:
                        totalpoint += 20 

                    if scoreup == "正解の加点を10点にする":
                        totalpoint += 10
                    
                    if scoreup == "正解の加点を5点にする":
                        totalpoint += 5

                    label_point = tk.Label(root_main, text = totalpoint, font = ("Helvetica",36))
                    label_point.place(x = 550, y = 190)
                else:
                    label_answer = tk.Label(root_main, text = uncrearmessage, font = ("Helvetica",36))
                    label_answer.place(x = 550, y = 130)

                    if scoredown == "デフォルト"or scoredown == 0:
                        totalpoint -= 10 
                    
                    if scoredown == "不正解の減点を3点にする":
                        totalpoint -= 3
                    
                    if scoredown == "不正解の減点を5点にする":
                        totalpoint -= 5
                    
                    if scoredown == "不正解の減点を20点にする":
                        totalpoint -= 20
                    
                    if scoredown == "不正解の減点をしない":
                        totalpoint -= 0

                    label_point = tk.Label(root_main, text = totalpoint, font = ("Helvetica",36))
                    label_point.place(x = 550, y = 190)

                #回答後の待機時間
                if nextquestions == "2秒空ける":
                    time.sleep(2) 

                if nextquestions == "1秒空ける":
                    time.sleep(1) 

                if nextquestions == "0.5秒空ける":
                    time.sleep(0.5) 

                if nextquestions == "0.2秒空ける":
                    time.sleep(0.2) 

                if nextquestions == "デフォルト"or nextquestions == 0:
                    time.sleep(1.5) 

                label_answer = tk.Label(root_main, text = "　　　　　　　　"+"\033", font = ("Helvetica",36))
                label_answer.place(x = 550, y = 130)

                #テキストボックス内の数字の初期化
                editbox_left.delete(0, tkinter.END)
                editbox_right.delete(0, tkinter.END)
                editbox_answer.delete(0, tkinter.END)
                

                if totalpoint >= 100:
                    ret = messagebox.askyesno('クリアおめでとうございます！', 'ゲームを続けますか？')
                    if ret == True:
                        if nextmessage == "デフォルト"or nextmessage == 0:
                            messagebox.showinfo('Next Level','1ゲームクリア!')

                        if nextmessage == "継続メッセージを「レベルアップ！」にする":
                            messagebox.showinfo('Next Level','レベルアップ！')

                        if nextmessage == "継続メッセージを「レベルが1つ上がりました」にする":
                            messagebox.showinfo('Next Level','レベルが1つ上がりました')
                        
                        totalpoint = 0
                        label_point = tk.Label(root_main, text = "　　　　　　　　"+"\033", font = ("Helvetica",36))
                        label_point.place(x = 550, y = 190)
                        label_point = tk.Label(root_main, text = "点", font = ("Helvetica",36))
                        label_point.place(x = 700, y = 190)
                        gamelevel += 1
                        #ゲーム画面の文字（レベルアップ）
                        label_point = tk.Label(root_main, text = gamelevel, font = ("Helvetica",20))
                        label_point.place(x = 700, y = 290)

                        if rankoption == "デフォルト"or rankoption == 0:
                            editbox_left.insert(tkinter.END,random.randint(0,9))
                            editbox_right.insert(tkinter.END,random.randint(0,9))

                        if rankoption == "先の数字を「20未満に変える」":
                            editbox_left.insert(tkinter.END,random.randint(0,19))
                            editbox_right.insert(tkinter.END,random.randint(0,9))
                        
                        if rankoption == "先の数字も後の数字も「20未満に変える」":
                            editbox_left.insert(tkinter.END,random.randint(0,19))
                            editbox_right.insert(tkinter.END,random.randint(0,19))
                        
                        if rankoption == "先の数字を「50未満」、後の数字を「10未満」に変える":
                            editbox_left.insert(tkinter.END,random.randint(0,49))
                            editbox_right.insert(tkinter.END,random.randint(0,9))
                        
                        if rankoption == "先の数字をレベルに応じて可変（数字を(z*10)に変えます）、後の数字を「10未満」に変える":
                            editbox_left.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
                            editbox_right.insert(tkinter.END,random.randint(0,9))

                        if rankoption == "先の数字も後の数字もレベルに応じて可変":
                            editbox_left.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
                            editbox_right.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
    
                        
                        label_answer = tk.Label(root_main, text = "", font = ("Helvetica",36))
                        left = int(editbox_left.get())
                        right = int(editbox_right.get())
                        Correct_answer = left + right
                    else:
                        #ゲーム終了処理
                        if endmessage == "デフォルト"or endmessage == 0:
                            messagebox.showinfo('End Game','ゲーム終了')

                        if endmessage == "終了メッセージを「ゲームを終了します」にする":
                            messagebox.showinfo('End Game','ゲームを終了します')

                        if endmessage == "終了メッセージを「お疲れ様でした」にする":
                            messagebox.showinfo('End Game','お疲れ様でした')
                        
                        totalpoint = 0
                        label_point = tk.Label(root_main, text = "　　　　　　　　"+"\033", font = ("Helvetica",36))
                        label_point.place(x = 550, y = 190)
                        label_point = tk.Label(root_main, text = "点", font = ("Helvetica",36))
                        label_point.place(x = 700, y = 190)

                        
                
                else:
                #次の問題の作成

                    if rankoption == "デフォルト"or rankoption == 0:
                        editbox_left.insert(tkinter.END,random.randint(0,9))
                        editbox_right.insert(tkinter.END,random.randint(0,9))

                    if rankoption == "先の数字を「20未満に変える」":
                        editbox_left.insert(tkinter.END,random.randint(0,19))
                        editbox_right.insert(tkinter.END,random.randint(0,9))
    
                    if rankoption == "先の数字も後の数字も「20未満に変える」":
                        editbox_left.insert(tkinter.END,random.randint(0,19))
                        editbox_right.insert(tkinter.END,random.randint(0,19))
    
                    if rankoption == "先の数字を「50未満」、後の数字を「10未満」に変える":
                        editbox_left.insert(tkinter.END,random.randint(0,49))
                        editbox_right.insert(tkinter.END,random.randint(0,9))
    
                    if rankoption == "先の数字をレベルに応じて可変（数字を(z*10)に変えます）、後の数字を「10未満」に変える":
                        editbox_left.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
                        editbox_right.insert(tkinter.END,random.randint(0,9))

                    if rankoption == "先の数字も後の数字もレベルに応じて可変":
                        editbox_left.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
                        editbox_right.insert(tkinter.END,random.randint(0,9)*gamelevel*10)
    
                    
                    
                    label_answer = tk.Label(root_main, text = "", font = ("Helvetica",36))
                    left = int(editbox_left.get())
                    right = int(editbox_right.get())
                    Correct_answer = left + right

    keyboard.on_press(on_enter_press)
  

#ゲームスタートボタン
button_gamestart = tk.Button(root_main,text = "ここからスタート",font =("Helvetica",28),command=startbtn_click)
button_gamestart.place(x = 250,y = 300)


root_main.mainloop()