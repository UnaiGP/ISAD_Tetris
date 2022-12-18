import tkinter as tk
import view.Rankinga

class RankingMota(object):
    def __init__(self, erab):
        super(RankingMota, self).__init__()
        root = tk.Tk()
        root.title("Ranking-a aukeratu")

        label=tk.Label(root, text="Aukeratu Ranking maila",  width=20, font=("bold", 20))
        label.grid(row=0, column=1)

        def rankinMota():
            button1.grid_forget()
            button2.grid_forget()
            button3.grid_forget()
            button4 = tk.Button(root, text="Erraza ranking-a", bg='grey', command=lambda:[view.Rankinga.Rankinga(4,erab), root.destroy()]).grid(row=1, column=0, padx=10)
            button5 = tk.Button(root, text="Ertaina ranking-a", bg='grey', command=lambda:[view.Rankinga.Rankinga(5,erab), root.destroy()]).grid(row=1, column=1, padx=10)
            button6 = tk.Button(root, text="Zaila ranking-a", bg='grey', command=lambda:[view.Rankinga.Rankinga(6,erab), root.destroy()]).grid(row=1, column=2, padx=10)

        def atzera():
            root.destroy()

        button1 = tk.Button(root, text="Mailakako ranking-a", bg='grey', command= rankinMota)
        button1.grid(row=1, column=0, padx=10)
        button2 = tk.Button(root, text="Ranking pertsonala", bg='grey', command=lambda:[view.Rankinga.Rankinga(2, erab), root.destroy()])
        button2.grid(row=1, column=1, padx=10)
        button3= tk.Button(root, text="Ranking globalak", bg='grey', command=lambda:[view.Rankinga.Rankinga(3,erab), root.destroy()])
        button3.grid(row=1, column=2, padx=10)

        amaitu = tk.Button(root, text="Atzera", width=10, font=("bold", 10), bg='grey', command=atzera)
        amaitu.grid(row=2, column=1, pady= 20)

        root.mainloop()