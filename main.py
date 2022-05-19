from cleaner import Cleaner
from message_prompt import MessageBox

if __name__ == '__main__':

    clr_obj = Cleaner("C:")

    mess_box = MessageBox(clr_obj.pathing())
    mess_box.popup()

    clr_obj.remover(clr_obj.pathing())
