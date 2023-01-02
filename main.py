import tkinter
import typing
import os
from PIL import Image
from pathlib import Path
import customtkinter as ctk
import cv2
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = Path(BASE_DIR, 'assets')
STORAGE_DIR = Path(BASE_DIR, 'storage')

for i in dir(ctk):
    print(i)

class LityApp:
    theme: str = 'dark'
    is_dark =  True
    db= 'storage/LityTech.db'

    def __init__(self, ctk_app: ctk):
        self.app = ctk_app
        self.app_settings()
        self.screen()
        self.init_db()
        self.main_view()
        # self.login_view()
        # self.device_view()
        # self.update_view()

    def init_db(self):
        db_exists = os.path.exists(self.db)
        print('DB Exists:', db_exists)
        if not db_exists:
            con = sqlite3.connect(self.db)

            cur = con.cursor()

            cur.execute(
                "CREATE TABLE IF NOT EXISTS devices (id INTEGER PRIMARY KEY, phone_number TEXT, first_name TEXT NOT NULL, surname TEXT NOT NULL, device_name TEXT NOT NULL, device_model TEXT NOT NULL, device_color TEXT, device_issue TEXT NOT NULL, amount_charged INTEGER NOT NULL, amount_deposited REAL NOT NULL, date_added TEXT NOT NULL, coll_date TEXT NOT NULL, status TEXT NOT NULL)")

            cur.execute("CREATE TABLE IF NOT EXISTS authentication (username TEXT, password TEXT)")

            cur.execute("INSERT INTO authentication VALUES (?, ?)", ('litytech', 'litytech'))
            con.commit()
            con.close()

    def app_settings(self):
        self.width = 650
        self.height = 390
        self.app.geometry(f"{self.width}x{self.height}")
        self.app.title('LityTech')
        self.app.resizable(False, False)
        self.color_theme(self.theme)  # Default color theme Dark

    def screen(self):
        self.window = ctk.CTkFrame(self.app, width=self.width, height=self.height)
        self.window.place(relx=0, rely=0)

    def color_theme(self, theme: str):
        """
        chenges app theme dark or light

        theme   The selected theme(light or dark)
        """
        ctk.set_appearance_mode(theme)  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    def main_view(self):
        main_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        main_frame.place(relx=0, rely=0)

        self.bg_image = ctk.CTkImage(Image.open(str(Path(ASSETS_DIR, 'images', 'bg_2.jpg'))),
                                                size=(self.width, self.height))

        bg_image_label = ctk.CTkLabel(main_frame, image=self.bg_image)
        bg_image_label.place(relx=0, rely=0)

        text_frame = ctk.CTkFrame(main_frame, width=self.width)
        text_frame.place(relx=0, rely=0.3, relheight=0.4)

        text = ctk.CTkLabel(text_frame, text="LityTech Desktop App", font=ctk.CTkFont(size=20, weight="bold"))
        text.place(relx=0.08, rely=0.27)

        btn = ctk.CTkButton(text_frame, text='continue', command=self.login_view)
        btn.place(relx=0.08, rely=0.5, relwidth=0.3)

    def login_view(self):
        self.login_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        self.login_frame.place(relx=0, rely=0)

        child_frame = ctk.CTkFrame(self.login_frame, width=self.width, height=self.height, bg_color='#fff', corner_radius=0)
        child_frame.place(relx=0.3, rely=0, relwidth=0.4, relheight=1)

        self.login_username = ctk.CTkEntry(self.login_frame, placeholder_text="Username",)
        self.login_username.place(relx=0.35, rely=0.25, relwidth=0.3)
        # self.login_username.focus()

        self.login_password = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show='*')
        self.login_password.place(relx=0.35, rely=0.4, relwidth=0.3)

        btn = ctk.CTkButton(self.login_frame, text='login', command=self.login)
        btn.place(relx=0.35, rely=0.6, relwidth=0.3)

    def device_registration_view(self):
        self.reg_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        self.reg_frame.place(relx=0, rely=0)

        device_label = ctk.CTkLabel(self.reg_frame, text='Device info', font=ctk.CTkFont(size=14, weight="bold"))
        device_label.place(relx=0.055, rely=0.03)

        self.phone_name = ctk.CTkEntry(self.reg_frame, placeholder_text="Device name")
        self.phone_name.place(relx=0.05, rely=0.11, relwidth=0.34)

        self.model = ctk.CTkEntry(self.reg_frame, placeholder_text="Device model")
        self.model.place(relx=0.05, rely=0.21, relwidth=0.34)

        self.color = ctk.CTkEntry(self.reg_frame, placeholder_text="Device color")
        self.color.place(relx=0.05, rely=0.31, relwidth=0.34)

        self.issue = ctk.CTkEntry(self.reg_frame, placeholder_text="Device issue")
        self.issue.place(relx=0.05, rely=0.41, relwidth=0.34)

        customer_label = ctk.CTkLabel(self.reg_frame, text='Customer info', font=ctk.CTkFont(size=14, weight="bold"))
        customer_label.place(relx=0.055, rely=0.52)

        self.first_name = ctk.CTkEntry(self.reg_frame, placeholder_text="First name")
        self.first_name.place(relx=0.05, rely=0.6, relwidth=0.34)

        self.last_name = ctk.CTkEntry(self.reg_frame, placeholder_text="Surname")
        self.last_name.place(relx=0.05, rely=0.7, relwidth=0.34)

        self.phone_no = ctk.CTkEntry(self.reg_frame, placeholder_text="Phone number")
        self.phone_no.place(relx=0.05, rely=0.8, relwidth=0.34)

        self.amount_charged = ctk.CTkEntry(self.reg_frame, placeholder_text="Amount Charged")
        self.amount_charged.place(relx=0.55, rely=0.11, relwidth=0.34)

        self.amount_deposited = ctk.CTkEntry(self.reg_frame, placeholder_text="Amount deposited")
        self.amount_deposited.place(relx=0.55, rely=0.21, relwidth=0.34)

        date_label = ctk.CTkLabel(self.reg_frame, text='Date:', font=ctk.CTkFont(size=12))
        date_label.place(relx=0.555, rely=0.32)

        self.date = ctk.CTkEntry(self.reg_frame, placeholder_text="yyyy-mm-dd")
        self.date.place(relx=0.55, rely=0.38, relwidth=0.34)

        date2_label = ctk.CTkLabel(self.reg_frame, text='Date to be collected:', font=ctk.CTkFont(size=12))
        date2_label.place(relx=0.555, rely=0.47)

        self.coll_date = ctk.CTkEntry(self.reg_frame, placeholder_text="yyyy-mm-dd")
        self.coll_date.place(relx=0.55, rely=0.53, relwidth=0.34)

        btn = ctk.CTkButton(self.reg_frame, text='submit', command=self.register)
        btn.place(relx=0.55, rely=0.7, relwidth=0.34)

        btn = ctk.CTkButton(self.reg_frame, text='back', fg_color='#222', command=self.options_view)
        btn.place(relx=0.55, rely=0.8, relwidth=0.34)

    def set_password(self, password):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("UPDATE authentication SET password=? WHERE username=?", (password, 'litytech'))
        con.commit()
        con.close()

    def gets(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * FROM authentication")
        res = cur.fetchall()
        con.close()
        return res

    def get_password(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT password FROM authentication WHERE username=?", ('litytech',))
        password = cur.fetchone()
        con.close()
        return password

    def change_password(self):
        old_paswd = self.old_password.get()
        new_paswd = self.new_password.get()
        conf_paswd = self.conf_new_password.get()
        msg = ''

        if old_paswd != '' and new_paswd != '' and conf_paswd != '':
            paswd = self.get_password()

            if old_paswd == paswd[0]:
                if new_paswd == conf_paswd:
                    self.set_password(new_paswd)
                    msg = 'Password changed successfully'
                    self.old_password.delete(0, ctk.END)
                    self.new_password.delete(0, ctk.END)
                    self.conf_new_password.delete(0, ctk.END)
                else: msg = 'Password does not match'
            else: msg = 'That is not the the current password.'
        else:
            msg = 'Fill all entry.'
        self.paswd_lbl.configure(text=msg)


    def password_change_view(self):
        password_change_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        password_change_frame.place(relx=0, rely=0)

        self.old_password = ctk.CTkEntry(password_change_frame, placeholder_text='Current password', show='*')
        self.old_password.place(relx=0.1, rely=0.1)

        self.new_password = ctk.CTkEntry(password_change_frame, placeholder_text='New password', show='*')
        self.new_password.place(relx=0.1, rely=0.25)

        self.conf_new_password = ctk.CTkEntry(password_change_frame, placeholder_text='Confirm password', show='*')
        self.conf_new_password.place(relx=0.1, rely=0.4)

        btn = ctk.CTkButton(password_change_frame, text='Change', command=self.change_password)
        btn.place(relx=0.1, rely=0.55)

        btn = ctk.CTkButton(password_change_frame, text='back', fg_color='#222', text_color='white', command=self.options_view)
        btn.place(relx=0.1, rely=0.66)

        self.paswd_lbl = ctk.CTkLabel(password_change_frame, text='')
        self.paswd_lbl.place(relx=0.1, rely=0.75)

    def options_view(self):
        options_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        options_frame.place(relx=0, rely=0)

        btn = ctk.CTkButton(options_frame, text='Register Device', command=self.device_registration_view)
        btn.place(relx=0.05, rely=0.1)

        btn = ctk.CTkButton(options_frame, text='Search Record', command=self.device_view)
        btn.place(relx=0.05, rely=0.25)

        btn = ctk.CTkButton(options_frame, text='Change Password', command=self.password_change_view)
        btn.place(relx=0.05, rely=0.4)

    def find_records(self, search):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT id, device_name, status FROM devices WHERE phone_number=?", (search,))
        res = cur.fetchall()
        con.close()
        return res

    def get_records(self):
        phone_no = self.dev_phone_no.get()
        self.device_list.delete('0.0', 'end')
        if phone_no.strip != '':
            records = self.find_records(phone_no)
            print(records)
            for record in records:
                self.device_list.insert('0.0', f'{record[0]}---{record[1]}---{record[2]}\n\n')

    def find_record(self, search):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * FROM devices WHERE id=?", (search,))
        res = cur.fetchone()
        con.close()
        return res

    def get_record(self):
        device_id = self.dev_id.get()
        if device_id.strip != '':
            id = int(device_id)
            record = self.find_record(id)
            print(record)
            self.device_info.delete('0.0', 'end')
            self.device_info.insert('0.0',f'''
            Device status: {record[12]}
            
            Device name:  {record[4]}
            
            Device model:  {record[5]}
            
            Device color:  {record[6]}
            
            Amount charged:  {record[8]}
            
            Amount deposited:  {record[9]}
            
            balance:  {record[8] - record[9]}
            
            Date brought: {record[10]}
            
            To be collected: {record[11]}
            
            Customer Name:  {record[2]} {record[3]}
            
            Phone number: {record[1]}
            
            issue: {record[7]}
        ''')

            #except:
            #    message = 'ID does not exist'


    def device_view(self):
        device_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        device_frame.place(relx=0, rely=0)

        self.dev_phone_no = ctk.CTkEntry(device_frame, placeholder_text="Phone number")
        self.dev_phone_no.place(relx=0.05, rely=0.05)

        self.dev_id = ctk.CTkEntry(device_frame, placeholder_text="Device id")
        self.dev_id.place(relx=0.635, rely=0.05, relwidth=0.15)

        btn = ctk.CTkButton(device_frame, text='search records', fg_color='#fff', text_color='#333', command=self.get_records)
        btn.place(relx=0.05, rely=0.15)

        btn = ctk.CTkButton(device_frame, text='search', command=self.get_record)
        btn.place(relx=0.795, rely=0.05, relwidth=0.15)

        self.device_list = ctk.CTkTextbox(device_frame)
        self.device_list.place(relx=0.05, rely=0.28, relwidth=0.4)

        ctk.CTkFrame(device_frame, fg_color='#444').place(relx=0.475, rely=0, relwidth=0.005, relheight=1)

        self.device_info = ctk.CTkTextbox(device_frame)
        self.device_info.place(relx=0.5, rely=0.16, relwidth=0.45, relheight=0.76)

        btn = ctk.CTkButton(device_frame, text='back', fg_color='#222', command=self.options_view)
        btn.place(relx=0.05, rely=0.85, relwidth=0.18)

        btn = ctk.CTkButton(device_frame, text='update device', fg_color='#222', command=self.update_view)
        btn.place(relx=0.25, rely=0.85, relwidth=0.18)
        
    

    def update(self):
        id = self.update_id.get()
        status = self.status.get()
        charge = self.update_charge.get()
        deposit = self.update_deposit.get()
        issue = self.update_issue.get()
        coll_date = self.update_coll_date.get()
        
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        if id !='':
            cur.execute("UPDATE devices SET status=? WHERE id=?", (status, id))
            if charge !='':
                cur.execute("UPDATE devices SET amount_charged=? WHERE id=?", (charge, id))
            if deposit !='':
                cur.execute("UPDATE devices SET amount_deposited=? WHERE id=?", (deposit, id))
            if issue !='':
                cur.execute("UPDATE devices SET device_issue=? WHERE id=?", (issue, id))
            if coll_date !='':
                cur.execute("UPDATE devices SET coll_date=? WHERE id=?", (coll_date, id))
            con.commit()
            con.close()
            self.update_id.delete(0, ctk.END)
            self.update_charge.delete(0, ctk.END)
            self.update_deposit.delete(0, ctk.END)
            self.update_issue.delete(0, ctk.END)
            self.update_coll_date.delete(0, ctk.END)
        
    def update_view(self):
        update_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        update_frame.place(relx=0, rely=0)

        self.update_id = ctk.CTkEntry(update_frame, placeholder_text='id')
        self.update_id.place(relx=0.05, rely=0.05, relwidth=0.15)

        ctk.CTkFrame(update_frame, bg_color='#222').place(relx=0, rely=0.15, relwidth=1, relheight=0.02)

        ctk.CTkLabel(update_frame, text='Status:').place(relx=0.06, rely=0.2)

        self.status = ctk.CTkOptionMenu(master=update_frame, values=['RECEIVED', 'RETURNED', 'COLLECTED'])
        self.status.place(relx=0.05, rely=0.26, relwidth=0.15)

        self.update_charge = ctk.CTkEntry(update_frame, placeholder_text='Amount charged')
        self.update_charge.place(relx=0.05, rely=0.36, relwidth=0.4)

        self.update_deposit = ctk.CTkEntry(update_frame, placeholder_text='Amount Deposited')
        self.update_deposit.place(relx=0.05, rely=0.46, relwidth=0.4)

        self.update_issue = ctk.CTkEntry(update_frame, placeholder_text='Device issue')
        self.update_issue.place(relx=0.55, rely=0.36, relwidth=0.4)

        self.update_coll_date = ctk.CTkEntry(update_frame, placeholder_text='To be collected (yyyy-mm-dd)')
        self.update_coll_date.place(relx=0.55, rely=0.46, relwidth=0.4)

        ctk.CTkFrame(update_frame, bg_color='#222').place(relx=0, rely=0.69, relwidth=1, relheight=0.02)

        btn = ctk.CTkButton(update_frame, text='update', command=self.update)
        btn.place(relx=0.05, rely=0.75)

        btn = ctk.CTkButton(update_frame, text='back', fg_color='#222', command=self.device_view)
        btn.place(relx=0.05, rely=0.85)

    def get_data_length(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * FROM devices")
        res = cur.fetchall()
        return len(res)

    def authenticate(self, username, password):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * FROM authentication")
        users = cur.fetchall()
        if users[0][0] == username and users[0][1] == password:
            con.close()
            return True
        con.close()
        return False

    def save_data_to_db(self, data):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        con.commit()
        con.close()

    def register(self):
        phone_name = self.phone_name.get().strip()
        model = self.model.get().strip()
        color = self.color.get().strip()
        issue = self.issue.get().strip()
        first_name = self.first_name.get().strip()
        last_name = self.last_name.get().strip()
        phone_no = self.phone_no.get().strip()
        amount_charged = self.amount_charged.get().strip()
        amount_deposited = self.amount_deposited.get().strip()
        date = self.date.get().strip()
        coll_date = self.coll_date.get().strip()
        message = ''

        if phone_name.strip()!='' and model.strip()!='' and color.strip()!='' and issue.strip()!='' and first_name.strip()!='' and last_name.strip()!='' and phone_no.strip()!='' and amount_charged.strip()!='' and amount_deposited.strip()!='' and date.strip()!='' and coll_date.strip()!='':
            db_size = self.get_data_length()
            self.save_data_to_db((db_size+1, phone_no, first_name, last_name, phone_name, model, color, issue, amount_charged, amount_deposited, date, coll_date, 'RECEIVED'))
            message = 'Data successfully saved.'
            self.phone_name.delete(0, ctk.END)
            self.model.delete(0, ctk.END)
            self.color.delete(0, ctk.END)
            self.issue.delete(0, ctk.END)
            self.first_name.delete(0, ctk.END)
            self.last_name.delete(0, ctk.END)
            self.phone_no.delete(0, ctk.END)
            self.amount_charged.delete(0, ctk.END)
            self.amount_deposited.delete(0, ctk.END)
            self.date.delete(0, ctk.END)
            self.coll_date.delete(0, ctk.END)
        else:
            message = 'Fill all fields'

        ctk.CTkLabel(self.reg_frame, text=message).place(relx=0.55, rely=0.02)

    def login(self):
        message = ''
        username = self.login_username.get()
        password = self.login_password.get()

        if username != None and username.strip() != '' and password != None and password.strip() != '':
            is_user = self.authenticate(username, password)
            if is_user:
                self.options_view()
            else: message = 'Incorrect Username or Password.'
        else:
            message = 'Enter Username and Password.'

        ctk.CTkLabel(self.login_frame, text='    '+message+'    ', text_color='white').place(relx=0.32, rely=0.85)

    def change_theme(self):
        self.is_dark = not self.is_dark
        print(self.is_dark)

        if self.is_dark:
            self.theme = 'dark'
        else:
            self.theme = 'light'
        self.color_theme(self.theme)

if __name__ == '__main__':
    app = ctk.CTk()  # create CTk window like you do with the Tk window
    LityApp(app)
    app.mainloop()

# def change_image_ext():
#     files_dir = Path(ASSETS_DIR, 'images')
#     files = os.listdir(files_dir)
#     for file in files:
#         f = file.split('.')
#         file_name = f[0]
#         ext = f[1]
#         if ext == 'jpeg':
#             new_file_name = f'{file_name}.jpg'
#             img = cv2.imread(str(Path(files_dir, file)))
#             cv2.imwrite(str(Path(files_dir, new_file_name)), img)
