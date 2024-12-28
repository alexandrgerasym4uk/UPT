from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import os, re, cohere, threading, json, sys, webbrowser, requests
from tkinter import messagebox
from ui_adaptive1 import Ui_MainWindow_Start
from ui_adaptive2 import Ui_MainWindow_Main

"""Необхідні дані для роботи"""
url = "https://dashboard.cohere.com/api-keys"
green_style = """
    QPushButton {
        background-color: green;      
        color: black;                 
        border-radius: 5px;           
        border: 1px solid lightgray;  
    }
"""

red_style = """
    QPushButton {
        background-color: red;      
        color: black;                 
        border-radius: 5px;           
        border: 1px solid lightgray;  
    }
"""


"""Функції програми"""


def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False


def generate(prompt, max_t):
    print("start")
    with open("data/key.json", "r") as key:
        global api_key
        api_key = json.load(key)
    co = cohere.Client(api_key)
    response = co.generate(
        model="command-xlarge-nightly",
        prompt=prompt,
        max_tokens=max_t,
        temperature=0.75,
    )
    return response.generations[0].text


def generation(name, age, course):
    text = f"""Привіт, мене звати {name}, мені, {age} і я хочу вчити {course}. 
    Напиши мені план курсу для вивчення {course} на 5 днів. 
    Практика повинна ТІЛЬКИ бути у вигляді тестів з відповідями а, б, в
    Пиши по зразку:

    **День 1: <Тема дня>**
    - <план для вивчення теми>
    Практика:
    - <тести>

    **День 2: <Тема дня>**
    - <план для вивчення теми>
    Практика:
    - <тести>

    **День 3: <Тема дня>**
    - <план для вивчення теми>
    Практика:
    - <тести>

    **День 4: <Тема дня>**
    - <план для вивчення теми>
    Практика:
    - <тести>

    **День 5: <Тема дня>**
    - <план для вивчення теми>
    Практика:
    - <тести>
    
    Пиши строго по цьому зразку, бо мені треба використовувати твою відповідь і важливий кожен символ"""
    result = generate(text, 3000)
    with open("data/course.txt", "w", encoding="utf-8") as file:
        file.write(result)


def check_answer(question, answer):
    text = f"""
    {question}, 
    {answer}
    Перевір загальне виконання тестів. Якщо половина тестів правильна то відповідай '+' 
    Відповідай тільки '+' або '-' обов'язково малими літерами без крапки. якщо ні то поясни"""
    check = generate(text, 100)
    print(check)
    return check


def check_progress():
    if all(progress[i][0] == 1 for i in range(1, 6)):
        return 1


def show_success():
    if messagebox.showinfo("Вітаємо!", "Ви успішно завершили курс!"):
        exit()


def read_course():
    with open("data/course.txt", "r", encoding="utf-8") as file:
        data = file.read()
    pattern = r"\*\*(День \d+: .+?)\*\*\n- (.+?)(?=\n\*\*День \d+: |$)"
    matches = re.findall(pattern, data, re.DOTALL)
    course = []
    for match in matches:
        day, content = match
        practical = re.findall(
            r"Практика:\n(.+?)(?=\n\*\*День \d+: |$)", content, re.DOTALL
        )
        practical_text = practical[0] if practical else "Без практики"
        course.append(
            {
                "theme": day[8:],
                "theory": content.strip().split("\nПрактика:")[0],
                "practical": practical_text.strip(),
            }
        )
    return course


def continue_course():
    global course
    course = read_course()
    with open("data/progress.json", "r") as file:
        global progress
        progress = json.load(file)
    if check_progress():
        show_success()
    with open("data/days.json", "r") as file:
        global days_theory
        days_theory = json.load(file)
    if not days_theory:
        print("догенерувати")


def generate_theory(index, theory):
    text = f"""{theory} 
    напиши детальну інформацію по кожному пункту
    не використовуй форматування тексту, пиши все простим текстом"""
    res = generate(text, 1000)
    results[index] = res


def generation_theory():
    course = read_course()
    global results
    results = [None] * 5
    threads = []
    for i in range(5):
        theo = course[i]["theory"]
        thread = threading.Thread(target=generate_theory, args=(i, theo))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    with open("data/days.json", "w") as file:
        json.dump(results, file)
    print("Результати є")


"""Класи для інтерфейсу"""


class Widget1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_Start()
        self.ui.setupUi(self)
        if not os.path.exists("data/key.json"):
            os.makedirs("data")
            self.ui.lb_text1.hide()
            self.ui.lb_text2.hide()
            self.ui.lb_text3.hide()
            self.ui.btn_continue.hide()
            self.ui.btn_start.hide()
            self.ui.lb_in_name.hide()
            self.ui.le_name.hide()
            self.ui.lb_in_age.hide()
            self.ui.le_age.hide()
            self.ui.lb_in_course.hide()
            self.ui.le_course.hide()

            self.ui.lb_text_key.show()
            self.ui.btn_key_get.show()
            self.ui.btn_key_get.clicked.connect(self.press_btn_get_key)
            self.ui.lb_in_key.show()
            self.ui.le_key.show()
            self.ui.btn_key.show()
            self.ui.btn_key.clicked.connect(self.press_btn_key)
        else:
            self.start_win()
            with open("data/key.json", "r") as key:
                global api_key
                api_key = json.load(key)
                global co
                co = cohere.Client(api_key)
        self.timer = QTimer()
        self.loading_text = "               Зачекайте, Ваш курс створюється"
        self.dots = 0

    def start_win(self):
        self.ui.lb_text_key.hide()
        self.ui.btn_key_get.hide()
        self.ui.lb_in_key.hide()
        self.ui.le_key.hide()
        self.ui.btn_key.hide()

        self.ui.lb_text1.show()
        self.ui.lb_text2.show()
        self.ui.lb_text3.show()
        self.ui.btn_start.show()
        self.ui.btn_start.clicked.connect(self.press_btn_start)
        if os.path.exists("data/course.txt"):
            self.ui.btn_continue.show()
            self.ui.btn_continue.clicked.connect(self.open_next_window)
        else:
            self.ui.btn_continue.hide()
        self.ui.lb_in_name.hide()
        self.ui.lb_in_age.hide()
        self.ui.lb_in_course.hide()
        self.ui.le_name.hide()
        self.ui.le_age.hide()
        self.ui.le_course.hide()

    def press_btn_get_key(self):
        webbrowser.open(url)

    def press_btn_key(self):
        api_key = self.ui.le_key.text()
        if api_key:
            with open("data/key.json", "w") as key:
                json.dump(api_key, key)
            global co
            co = cohere.Client(api_key)
            self.start_win()
        else:
            messagebox.showwarning("!", "Будь ласка, введіть дані.")

    def press_btn_start(self):
        if self.ui.btn_start.text() == "Розпочати":
            self.ui.btn_continue.hide()
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
            if (
                self.ui.le_name.text()
                and self.ui.le_age.text()
                and self.ui.le_course.text()
            ):
                self.ui.btn_start.hide()
                name = self.ui.le_name.text()
                age = self.ui.le_age.text()
                course = self.ui.le_course.text()
                self.ui.lb_in_name.hide()
                self.ui.lb_in_age.hide()
                self.ui.lb_in_course.hide()
                self.ui.le_name.hide()
                self.ui.le_age.hide()
                self.ui.le_course.hide()
                self.ui.lb_text2.show()
                self.ui.lb_text2.setText("")
                with open("data/progress.json", "w") as file:
                    json.dump([0, [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], file)
                with open("data/days.json", "w") as file:
                    json.dump([], file)
                self.start_loading()
                threading.Thread(
                    target=self.run_generation, args=(name, age, course)
                ).start()
            else:
                messagebox.showwarning("!", "Будь ласка, введіть дані.")
        else:
            self.close()
            self.open_next_window()

    def run_generation(self, name, age, course):
        # Зняти коментарі
        generation(name, age, course)
        generation_theory()
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
        self.close()
        continue_course()
        self.next_window = Widget2()
        self.next_window.show()


class Widget2(QMainWindow):
    def __init__(self):
        super().__init__()
        print(course)
        self.ui = Ui_MainWindow_Main()
        self.ui.setupUi(self)
        self.ui.btn_day_1.clicked.connect(self.btn_1_day)
        self.ui.btn_day_2.clicked.connect(self.btn_2_day)
        self.ui.btn_day_3.clicked.connect(self.btn_3_day)
        self.ui.btn_day_4.clicked.connect(self.btn_4_day)
        self.ui.btn_day_5.clicked.connect(self.btn_5_day)
        self.ui.btn_send.clicked.connect(self.btn_send)
        self.btn_1_day()
        if progress[0] == 1:
            if progress[1][0] == 1:
                self.ui.btn_day_1.setStyleSheet(green_style)
            if progress[2][0] == 1:
                self.ui.btn_day_2.setStyleSheet(green_style)
            if progress[3][0] == 1:
                self.ui.btn_day_3.setStyleSheet(green_style)
            if progress[4][0] == 1:
                self.ui.btn_day_4.setStyleSheet(green_style)
            if progress[5][0] == 1:
                self.ui.btn_day_5.setStyleSheet(green_style)

    def btn_1_day(self):
        self.ui.lb_num_day.setText("День: 1")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(course[0]["theme"])
        self.ui.tb_task.setText(course[0]["practical"])
        if days_theory[0]:
            self.ui.tb_theory.setText(days_theory[0])
        else:
            self.ui.tb_theory.setText(course[0]["theory"])

        if progress[1][0] == 1:
            self.ui.te_answer.setText(progress[1][1])

    def btn_2_day(self):
        self.ui.lb_num_day.setText("День: 2")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(course[1]["theme"])
        self.ui.tb_task.setText(course[1]["practical"])
        if days_theory[1]:
            self.ui.tb_theory.setText(days_theory[1])
        else:
            self.ui.tb_theory.setText(course[1]["theory"])
        if progress[2][0] == 1:
            self.ui.te_answer.setText(progress[2][1])

    def btn_3_day(self):
        self.ui.lb_num_day.setText("День: 3")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(course[2]["theme"])
        self.ui.tb_task.setText(course[2]["practical"])
        if days_theory[2]:
            self.ui.tb_theory.setText(days_theory[2])
        else:
            self.ui.tb_theory.setText(course[2]["theory"])
        if progress[3][0] == 1:
            self.ui.te_answer.setText(progress[3][1])

    def btn_4_day(self):
        self.ui.lb_num_day.setText("День: 4")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(course[3]["theme"])
        self.ui.tb_task.setText(course[3]["practical"])
        if days_theory[3]:
            self.ui.tb_theory.setText(days_theory[3])
        else:
            self.ui.tb_theory.setText(course[3]["theory"])
        if progress[4][0] == 1:
            self.ui.te_answer.setText(progress[4][1])

    def btn_5_day(self):
        self.ui.lb_num_day.setText("День: 5")
        self.ui.te_answer.setText("Відповідь:")
        self.ui.lb_text1.setText(course[4]["theme"])
        self.ui.tb_task.setText(course[4]["practical"])
        if days_theory[4]:
            self.ui.tb_theory.setText(days_theory[4])
        else:
            self.ui.tb_theory.setText(course[4]["theory"])
        if progress[5][0] == 1:
            self.ui.te_answer.setText(progress[5][1])

    def btn_send(self):
        progress[0] = 1
        if self.ui.lb_num_day.text() == "День: 1":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(course[0]["practical"], answer)
                if "+" in check:
                    self.ui.btn_day_1.setStyleSheet(green_style)
                    progress[1][0] = 1
                    progress[1][1] = answer
                else:
                    self.ui.btn_day_1.setStyleSheet(red_style)
        elif self.ui.lb_num_day.text() == "День: 2":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(course[1]["practical"], answer)
                if "+" in check:
                    self.ui.btn_day_2.setStyleSheet(green_style)
                    progress[2][0] = 1
                    progress[2][1] = answer
                else:
                    self.ui.btn_day_2.setStyleSheet(red_style)
        elif self.ui.lb_num_day.text() == "День: 3":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(course[2]["practical"], answer)
                if "+" in check:
                    self.ui.btn_day_3.setStyleSheet(green_style)
                    progress[3][0] = 1
                    progress[3][1] = answer
                else:
                    self.ui.btn_day_3.setStyleSheet(red_style)
        elif self.ui.lb_num_day.text() == "День: 4":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(course[3]["practical"], answer)
                if "+" in check:
                    self.ui.btn_day_4.setStyleSheet(green_style)
                    progress[4][0] = 1
                    progress[4][1] = answer
                else:
                    self.ui.btn_day_4.setStyleSheet(red_style)
        elif self.ui.lb_num_day.text() == "День: 5":
            answer = self.ui.te_answer.toPlainText()
            if answer != "Відповідь:":
                check = check_answer(course[4]["practical"], answer)
                if "+" in check:
                    self.ui.btn_day_5.setStyleSheet(green_style)
                    progress[5][0] = 1
                    progress[5][1] = answer
                else:
                    self.ui.btn_day_5.setStyleSheet(red_style)
        with open("data/progress.json", "w") as file:
            json.dump(progress, file)
        if check_progress():
            show_success()


if __name__ == "__main__":
    if check_internet_connection():
        app = QApplication(sys.argv)
        ex1 = Widget1()
        ex1.show()
        sys.exit(app.exec_())
    else:
        messagebox.showwarning(
            "Відсутнє з'єднання", "Будь ласка, перевірте підключення до Інтрнету."
        )
