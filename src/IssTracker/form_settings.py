import tkinter as tk
from tkinter import messagebox


class SettingsForm(tk.Toplevel):
    l_email: tk.Label
    l_smtp_server: tk.Label
    l_smtp_password: tk.Label
    e_email: tk.Entry
    e_smtp_server: tk.Entry
    e_smtp_password: tk.Entry
    b_submit: tk.Button

    settings: dict = {}
    email = ""
    smtp_server = ""
    smtp_password = ""

    def __init__(self, parent):
        super().__init__(parent, padx=50, pady=50)
        from iss_position import IssPosition
        self.parent: IssPosition = parent
        # if self.parent.settings.email_me is None:
        #     self.p
        #
        #
        #

        self.create_form()
        self.grab_set()

    def create_form(self):
        self.wm_title("Change settings")
        self.l_email = tk.Label(self, text="Email address:")
        self.l_smtp_server = tk.Label(self, text="Smtp server:")
        self.l_smtp_password = tk.Label(self, text="Smtp password:")
        self.e_email = tk.Entry(self)
        self.e_email.insert(0, string=self.parent.settings.email_me)
        self.e_smtp_server = tk.Entry(self)
        self.e_smtp_server.insert(0, string=self.parent.settings.smtp_server)
        self.e_smtp_password = tk.Entry(self)
        self.e_smtp_password.insert(0, string=self.parent.settings.smtp_password)
        self.l_email.grid(row=0, column=0)
        self.e_email.grid(row=0, column=1)
        self.l_smtp_server.grid(row=1, column=0)
        self.e_smtp_server.grid(row=1, column=1)
        self.l_smtp_password.grid(row=2, column=0)
        self.e_smtp_password.grid(row=2, column=1)
        self.b_submit = tk.Button(self, text="Submit", command=self.validate)
        self.b_submit.grid(row=3, column=0, columnspan=2)

    def validate(self):
        """
        Validate user input
        Email and smtp either both have a value or none at all
        """
        if self.e_email.get() == "" and self.e_smtp_server.get() == "" and self.e_smtp_password.get() == "":
            self.parent.settings.email_me = self.e_email.get()
            self.parent.settings.smtp_server = self.e_smtp_server.get()
            self.parent.save_config(self.parent.settings.as_dict())
        elif (not self.e_email.get() == ""
              and not self.e_smtp_server.get() == ""
              and not self.e_smtp_password.get() == ""):
            self.parent.settings.email_me = self.e_email.get()
            self.parent.settings.smtp_server = self.e_smtp_server.get()
            self.parent.settings.smtp_password = self.e_smtp_password.get()
            self.parent.save_config(self.parent.settings.as_dict())
        else:
            messagebox.showwarning(message="You have to fill email and smtp server/password or none off them")
            return
        self.destroy()
