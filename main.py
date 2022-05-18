import cleaner

if __name__ == '__main__':
    clr_obj = cleaner.Cleaner("C:")
    print(clr_obj.pathing())
    clr_obj.remover(clr_obj.pathing())
