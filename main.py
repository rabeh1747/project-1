import pandas as pd
# افترض أن الملف يستخدم فاصلة منقوطة كفاصل
df = pd.read_csv("excel_file.csv", sep=";")
# اطبع قيم col1
print(df["col1"])
# اطبع قيم col2
print(df["col2"])
# وهكذا


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        # إنشاء تخطيط شبكي بأربعة صفوف وعمود واحد
        layout = GridLayout(cols=1, rows=4)
        # إضافة lineedit2 وتعيينه كخاصية للاستخدام لاحقًا
        self.lineedit2 = TextInput()
        layout.add_widget(self.lineedit2)
        # إضافة button وتعيين دالة callback عند الضغط عليه
        self.button = Button(text="Show values")
        self.button.bind(on_press=self.on_button_press)
        layout.add_widget(self.button)
        # إضافة lineedit3 و lineedit4 وتعيينهم كخصائص للاستخدام لاحقًا
        self.lineedit3 = TextInput()
        layout.add_widget(self.lineedit3)
        self.lineedit4 = TextInput()
        layout.add_widget(self.lineedit4)
        # إرجاع التخطيط كعنصر جذر للتطبيق
        return layout

    def on_button_press(self, instance):
        # هذه الدالة تنفذ عند الضغط على button
        # احصل على قيمة col2 من lineedit2
        col2 = self.lineedit2.text
        # افترض أن الملف يستخدم فاصلة منقوطة كفاصل
        df = pd.read_csv("excel_file.csv", sep=";")
        # ابحث عن الصف الذي يحتوي على قيمة col2 في عمود col2
        df["col2"] = df["col2"].astype(str)
        # استخدام الشرط بعد التحويل
        row = df[df["col2"].str.contains(col2)]
        # حاول الوصول إلى قيم col3 و col4 من ذلك الصف
        try:
            # افحص طول الصف قبل قراءة قيمه
            if len(row) > 0:
                # احصل على قيم col3 و col4 من ذلك الصف
                col3 = row["col3"].values[0]
                col4 = row["col4"].values[0]
                # ضع قيم col3 و col4 في lineedit3 و lineedit4
                self.lineedit3.text = str(col3)
                self.lineedit4.text = str(col4)
            else:
                # إذا كان طول الصف يساوي 0 ، فإظهار رسالة توضيحية
                self.lineedit3.text = "No matching row found"
                self.lineedit4.text = "No matching row found"
        except IndexError:
            # إذا حدث خطأ في الفهرسة ، فإظهار رسالة توضيحية
            self.lineedit3.text = "Index error occurred"
            self.lineedit4.text = "Index error occurred"

# تشغيل التطبيق
MyApp().run()
