from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import os, re, cohere, threading, json
from tkinter import messagebox
from ui_adaptive1 import Ui_MainWindow_Start
from ui_adaptive2 import Ui_MainWindow_Main


api_key = 'Zf5HgFaPWLIoFPvzVi0hDhrCSOSjWRzAawiEDiV5'
co = cohere.Client(api_key)
button_style = '''
    QPushButton {
        background-color: green;      
        color: black;                 
        border-radius: 5px;           
        border: 1px solid lightgray;  
    }
'''
progress = [0, [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

def generate(prompt, max_t):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=max_t,
        temperature=0.75
    )
    return response.generations[0].text

def generation(name, age, course):
    text = f'''Привіт, мене звати {name}, мені, {age} і я хочу вчити {course}. 
    Напиши мені план курсу для вивчення {course} на 5 днів. 
    Практика повинна ТІЛЬКИ бути у вигляді тестів з відповідями а, б, в
    Пиши по зразку:

    **День 1: <Тема дня>**
    - <план для вивчення теми>
    Практика:
    - <тести>

    Пиши строго по цьому зразку, бо мені треба використовувати твою відповідь і важливий кожен символ'''
    result = generate(text, 3000)
    with open("data/course.txt", 'w', encoding='utf-8') as file:
        file.write(result)

def check_answer(question, answer):
    text = f'''Перевір тести на предмет загального виконання.
    завдання: {question}, 
    відповідь: {answer}
    Відповідай тільки 'так' або 'ні' обов'язково малими літерами без крапки. якщо ні то поясни'''
    check = generate(text, 100)
    print(check)
    return check

def check_progress():
    if all(progress[i][0] == 1 for i in range(1, 6)):
        return 1

def show_success():
    if messagebox.showinfo("Вітаємо!", "Ви успішно завершили курс!"):
        exit()

def start_course():
    with open("data/progress.json", "w") as file:
        json.dump(progress, file)
    app = QApplication([])
    ex1 = Widget1()
    ex1.show()
    app.exec_()

def continue_course():
    with open("data/progress.json", "r") as file:
        global progress 
        progress= json.load(file)
    app = QApplication([])
    ex2 = Widget2()
    ex2.show()
    app.exec_()
    

def read_course():
    with open("data/course.txt", 'r', encoding='utf-8') as file:
        data = file.read()
    
    pattern = r'\*\*(День \d+: .+?)\*\*\n- (.+?)(?=\n\*\*День \d+: |$)'

    matches = re.findall(pattern, data, re.DOTALL)

# Форматування результату
    course = []
    for match in matches:
        day, content = match
        practical = re.findall(r'Практика:\n(.+?)(?=\n\*\*День \d+: |$)', content, re.DOTALL)
        #print(practical)
        practical_text = practical[0] if practical else "Без практики"
        #print(practical_text)
        course.append({
            "theme": day[8:],
            "theory": content.strip().split("\nПрактика:")[0],
            "practical": practical_text.strip()
        })
    return course

class Widget2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_Main()
        self.ui.setupUi(self)
        self.ui.btn_day_1.clicked.connect(self.btn_1_day)
        self.ui.btn_day_2.clicked.connect(self.btn_2_day)
        self.ui.btn_day_3.clicked.connect(self.btn_3_day)
        self.ui.btn_day_4.clicked.connect(self.btn_4_day)
        self.ui.btn_day_5.clicked.connect(self.btn_5_day)
        self.ui.btn_send.clicked.connect(self.btn_send)
        self.course = read_course()
        self.btn_1_day()
        if progress[0] == 1:
            if progress[1][0] == 1:
                self.ui.btn_day_1.setStyleSheet(button_style)
            if progress[2][0] == 1:
                self.ui.btn_day_2.setStyleSheet(button_style)
            if progress[3][0] == 1:
                self.ui.btn_day_3.setStyleSheet(button_style)
            if progress[4][0] == 1:
                self.ui.btn_day_4.setStyleSheet(button_style)
            if progress[5][0] == 1:
                self.ui.btn_day_5.setStyleSheet(button_style)
        else:
            with open("data/progress.json", "w") as file:
                json.dump([0, [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], file)
            print()


    def btn_1_day(self):
        self.ui.lb_num_day.setText("День: 1")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(self.course[0]['theme'])
        self.ui.tb_theory.setText(self.course[0]['theory'])
        self.ui.tb_task.setText(self.course[0]['practical'])
        if progress[1][0] == 1:
            self.ui.te_answer.setText(progress[1][1])

    def btn_2_day(self):
        self.ui.lb_num_day.setText("День: 2")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(self.course[1]['theme'])
        self.ui.tb_theory.setText(self.course[1]['theory'])
        self.ui.tb_task.setText(self.course[1]['practical'])
        if progress[2][0] == 1:
            self.ui.te_answer.setText(progress[2][1])
    
    def btn_3_day(self):
        self.ui.lb_num_day.setText("День: 3")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(self.course[2]['theme'])
        self.ui.tb_theory.setText(self.course[2]['theory'])
        self.ui.tb_task.setText(self.course[2]['practical'])
        if progress[3][0] == 1:
            self.ui.te_answer.setText(progress[3][1])
    
    def btn_4_day(self):
        self.ui.lb_num_day.setText("День: 4")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(self.course[3]['theme'])
        self.ui.tb_theory.setText(self.course[3]['theory'])
        self.ui.tb_task.setText(self.course[3]['practical'])
        if progress[4][0] == 1:
            self.ui.te_answer.setText(progress[4][1])
    
    def btn_5_day(self):
        self.ui.lb_num_day.setText("День: 5")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(self.course[4]['theme'])
        self.ui.tb_theory.setText(self.course[4]['theory'])
        self.ui.tb_task.setText(self.course[4]['practical'])
        if progress[5][0] == 1:
            self.ui.te_answer.setText(progress[5][1])

    def btn_send(self):
        progress[0] = 1
        if self.ui.lb_num_day.text() == "День: 1":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(self.course[0]['practical'], answer)
                if check == "так" or check == "Так":
                    self.ui.btn_day_1.setStyleSheet(button_style)
                    progress[1][0] = 1
                    progress[1][1] = answer
        elif self.ui.lb_num_day.text() == "День: 2":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(self.course[1]['practical'], answer)
                if check == "так" or check == "Так":
                    self.ui.btn_day_2.setStyleSheet(button_style)
                    progress[2][0] = 1
                    progress[2][1] = answer
        elif self.ui.lb_num_day.text() == "День: 3":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(self.course[2]['practical'], answer)
                if check == "так" or check == "Так":
                    self.ui.btn_day_3.setStyleSheet(button_style)
                    progress[3][0] = 1
                    progress[3][1] = answer
        elif self.ui.lb_num_day.text() == "День: 4":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(self.course[3]['practical'], answer)
                if check == "так" or check == "Так":
                    self.ui.btn_day_4.setStyleSheet(button_style)
                    progress[4][0] = 1
                    progress[4][1] = answer
        elif self.ui.lb_num_day.text() == "День: 5":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(self.course[4]['practical'], answer)
                if check == "так" or check == "Так":
                    self.ui.btn_day_5.setStyleSheet(button_style)
                    progress[5][0] = 1
                    progress[5][1] = answer
        with open("data/progress.json", "w") as file:
            json.dump(progress, file)
        if check_progress():
            show_success()


class Widget1(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_Start()
        self.ui.setupUi(self)
        self.ui.btn_start.clicked.connect(self.press_btn_start)
        self.ui.lb_in_name.hide()
        self.ui.lb_in_age.hide()
        self.ui.lb_in_course.hide()
        self.ui.le_name.hide()
        self.ui.le_age.hide()
        self.ui.le_course.hide()
        self.timer = QTimer()
        self.loading_text = "               Зачекайте, Ваш курс створюється"
        self.dots = 0

    def press_btn_start(self):
        if self.ui.btn_start.text() == "Розпочати":
            self.ui.btn_start.setText("Згенерувати")
            self.ui.lb_text1.hide()
            self.ui.lb_text2.hide()
            self.ui.lb_text3.hide()
            self.ui.lb_in_name.show()
            self.ui.lb_in_age.show()
            self.ui.lb_in_course.show()
            self.ui.le_name.show()
            self.ui.le_age.show()
            self.ui.le_course.show()
        elif self.ui.btn_start.text() == "Згенерувати":
            if self.ui.le_name.text() and self.ui.le_age.text() and self.ui.le_course.text():
                self.ui.btn_start.hide()
                name = self.ui.le_name.text()
                age = self.ui.le_age.text()
                course = self.ui.le_corse.text()
                self.ui.lb_in_name.hide()
                self.ui.lb_in_age.hide()
                self.ui.lb_in_course.hide()
                self.ui.le_name.hide()
                self.ui.le_age.hide()
                self.ui.le_course.hide()
                self.ui.lb_text2.show()
                self.ui.lb_text2.setText("")
                self.start_loading()
                threading.Thread(target=self.run_generation, args=(name, age, course)).start()
            else:
                messagebox.showwarning("!", "Будь ласка, введіть дані.")
        else:
            self.close()
            self.open_next_window()
                
    def run_generation(self, name, age, course):
        # Зняти коментарі
        generation(name, age, course)
        self.stop_loading() 

    def stop_loading(self):
        self.timer.stop() 
        self.ui.lb_text2.setText("                    Курс успішно згенеровано!")
        self.ui.btn_start.setText("Вчитися!")
        self.ui.btn_start.show()

    def start_loading(self):
        self.timer.timeout.connect(self.update_loading_text)
        self.timer.start(500)  

    def update_loading_text(self):
        self.dots = (self.dots + 1) % 4  
        self.ui.lb_text2.setText(self.loading_text + "." * self.dots)
    
    def open_next_window(self):
        self.next_window = Widget2()
        self.next_window.show()
# основна програма
if os.path.exists("data/course.txt"):
    with open("data/progress.json", "r") as file: 
        progress= json.load(file)
    if check_progress():
        start_course()
    else:
        reply = messagebox.askquestion("", "У вас є згенерований курс, бажаєте продовжити?")
        if reply == 'yes':
            continue_course()
        else:
            start_course()
else:
    start_course()