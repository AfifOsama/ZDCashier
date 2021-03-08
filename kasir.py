from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time


class Customer:
    def __init__(self, roo):
        # --frontend--

        # main background
        self.root = root
        self.root.title("ZD Cashier")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")
        # grid table
        kotak1 = Frame(self.root, bg="powder blue", bd=20, relief=RIDGE)
        kotak1.grid()
        # kotak atas
        kotak2 = Frame(kotak1, bd=14, width=1250, height=100, padx=10,
                       bg="cadet blue",  relief=RIDGE)
        kotak2.grid(row=0, column=0, columnspan=4, sticky=W)
        # kotak bawah kiri
        kotak3 = Frame(kotak1, width=425, heigh=498, padx=10,
                       bg="cadet blue", bd=14, relief=RIDGE)
        kotak3.grid(row=1, column=0, sticky=W)
        # kotak bawah tengah
        kotak4 = Frame(kotak1, width=425, heigh=498, padx=10,
                       bg="powder blue", bd=14, relief=RIDGE)
        kotak4.grid(row=1, column=1, sticky=W)
        # kotak bawah kanan
        kotak5 = Frame(kotak1, width=300, heigh=498, padx=10,
                       bg="cadet blue", bd=14, relief=RIDGE)
        kotak5.grid(row=1, column=2, sticky=W)
        # kotak bawah kanan atas
        kotak6 = Frame(kotak5, width=330, heigh=345, padx=10,
                       bg="cadet blue", bd=14, relief=RIDGE)
        kotak6.grid(row=0, column=0, sticky=W)
        # kotak bawah kanan bawah
        kotak7 = Frame(kotak5, width=330, heigh=125, padx=10,
                       bg="cadet blue", bd=14, relief=RIDGE)
        kotak7.grid(row=1, column=0, columnspan=4, sticky=W)

        # date time title
        date1 = StringVar()
        time1 = StringVar()
        date1.set(time.strftime("%d/%m/%Y"))
        time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle = Label(kotak1, textvariable=date1, font=('Arial', 30), pady=9,
                              bd=4, bg='cadet blue', fg='Cornsilk').grid(row=0, column=0)

        self.lblTitle = Label(kotak1, text="ZD Cashier", font=('Arial', 30), pady=9,
                              bd=4, bg='cadet blue', fg='Cornsilk', justify=CENTER).grid(row=0, column=1)

        self.lblTitle = Label(kotak1, textvariable=time1, font=('Arial', 30), pady=9,
                              bd=4, bg='cadet blue', fg='Cornsilk').grid(row=0, column=2)

        # variable kotak kiri (data customer)

        customerRef = StringVar()
        nama = StringVar()
        alamat = StringVar()
        no_hp = StringVar()
        tgl_beli = StringVar()
        email = StringVar()
        reseller = StringVar()
        produk = StringVar()
        ukuran = StringVar()
        biayaTotal = StringVar()
        subTotal = StringVar()
        tax = StringVar()

        customerRef.set(random.randint(19700, 9875421))

        # variable kotak tengah
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()

        handSanitizer = StringVar()
        masker = StringVar()
        kalungmasker = StringVar()
        sanitizeRoom = StringVar()
        imbooster = StringVar()
        sabunDettol = StringVar()
        sampoDettol = StringVar()

        handSanitizer.set("0")
        masker.set("0")
        kalungmasker.set("0")
        sanitizeRoom.set("0")
        imbooster.set("0")
        sabunDettol.set("0")
        sampoDettol.set("0")

        cheetos = StringVar()
        lays = StringVar()
        chitato = StringVar()
        chikiballs = StringVar()
        jetz = StringVar()
        pringles = StringVar()
        piatto = StringVar()
        kitkat = StringVar()

        """
        cheetos.set("0")
        lays.set("0")
        chitat0.set("0")
        chikiballs.set("0")
        jetz.set("0")
        pringles.set("0")
        piatto.set("0")
        kitkat.set("0")
        """

        # ===========================================================================================
        # button action

        def exit():
            exit = tkinter.messagebox.askyesno(
                "ZD Cashier", "yakin ingin keluar?")
            if exit > 0:
                root.destroy()
                return

        def reset():
            self.txtNota.delete("1.0", END)
            handSanitizer.set("0")
            masker.set("0")
            kalungmasker.set("0")
            sanitizeRoom.set("0")
            imbooster.set("0")
            sabunDettol.set("0")
            sampoDettol.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)

            customerRef.set("")
            nama.set("")
            alamat.set("")
            no_hp.set("")
            tgl_beli.set("")
            email.set("")
            reseller.set("")
            produk.set("")
            ukuran.set("")
            biayaTotal.set("")
            subTotal.set("")
            tax.set("")

        # ========================================================================================================
        # backend kotak tengah

        def chkhandsanitizer():
            if (var1.get() == 1):
                self.txthandSanitizer.config(state=NORMAL)
                self.txthandSanitizer.focus()
                self.txthandSanitizer.delete('0', END)
                handSanitizer.set("")
            elif (var1.get() == 0):
                self.txthandSanitizer.config(state=DISABLED)
                handSanitizer.set("0")

        def chkmasker():
            if (var2.get() == 1):
                self.txtmasker.config(state=NORMAL)
                self.txtmasker.focus()
                self.txtmasker.delete('0', END)
                masker.set("")
            elif (var2.get() == 0):
                self.txtmasker.config(state=DISABLED)
                masker.set("0")

        def chkkalungmasker():
            if (var3.get() == 1):
                self.txtkalungmasker.config(state=NORMAL)
                self.txtkalungmasker.focus()
                self.txtkalungmasker.delete('0', END)
                kalungmasker.set("")
            elif (var3.get() == 0):
                self.txtkalungmasker.config(state=DISABLED)
                kalungmasker.set("0")

        def chksanitizeRoom():
            if (var4.get() == 1):
                self.txtsanitizeRoom.config(state=NORMAL)
                self.txtsanitizeRoom.focus()
                self.txtsanitizeRoom.delete('0', END)
                sanitizeRoom.set("")
            elif (var4.get() == 0):
                self.txtsanitizeRoom.config(state=DISABLED)
                sanitizeRoom.set("0")

        def chkimbooster():
            if (var5.get() == 1):
                self.txtimbooster.config(state=NORMAL)
                self.txtimbooster.focus()
                self.txtimbooster.delete('0', END)
                imbooster.set("")
            elif (var5.get() == 0):
                self.txtimbooster.config(state=DISABLED)
                imbooster.set("0")

        def chksabunDettol():
            if (var6.get() == 1):
                self.txtsabunDettol.config(state=NORMAL)
                self.txtsabunDettol.focus()
                self.txtsabunDettol.delete('0', END)
                sabunDettol.set("")
            elif (var6.get() == 0):
                self.txtsabunDettol.config(state=DISABLED)
                sabunDettol.set("0")

        def chksampoDettol():
            if (var7.get() == 1):
                self.txtsampoDettol.config(state=NORMAL)
                self.txtsampoDettol.focus()
                self.txtsampoDettol.delete('0', END)
                sampoDettol.set("")
            elif (var7.get() == 0):
                self.txtsampoDettol.config(state=DISABLED)
                sampoDettol.set("0")

        # =========================================================================================================
        # action button total
        def costItem():
            customerRef.set(random.randint(19700, 9875421))
            item1 = float(handSanitizer.get())
            item2 = float(masker.get())
            item3 = float(kalungmasker.get())
            item4 = float(sanitizeRoom.get())
            item5 = float(imbooster.get())
            item6 = float(sabunDettol.get())
            item7 = float(sampoDettol.get())

            priceOfMedicines = (item1*17.500)+(item2*13.000)+(item3*40.000) + \
                (item4*35.000)+(item5*7.500)+(item6*15.000)+(item7*17.000)
            subTotalOfItems = "Rp.", str('%.2f' % (priceOfMedicines))
            subTotal.set(subTotalOfItems)
            pajak = "Rp.", str('%.2f' % ((priceOfMedicines)*0.10))
            tax.set(pajak)
            totalTax = (priceOfMedicines)*0.10
            totalCost = "Rp.", str('%.2f' % (priceOfMedicines+totalTax))
            biayaTotal.set(totalCost)

            self.txtNota.insert(
                END, 'Customer Ref: \t\t\t\t'+customerRef.get()+"\n\n")
            self.txtNota.insert(END, 'Items\t\t\t\t'+"total harga \n")

            self.txtNota.insert(
                END, 'Hand Sanitizer\t\t\t\t\t'+handSanitizer.get()+"\n")
            self.txtNota.insert(END, 'Masker\t\t\t\t\t'+masker.get()+"\n")
            self.txtNota.insert(
                END, 'Kalung Masker\t\t\t\t\t'+kalungmasker.get()+"\n")
            self.txtNota.insert(
                END, 'Sanitize Room\t\t\t\t\t'+sanitizeRoom.get()+"\n")
            self.txtNota.insert(
                END, 'Imbooster\t\t\t\t\t'+imbooster.get()+"\n")
            self.txtNota.insert(
                END, 'Sabun Dettol\t\t\t\t\t'+sabunDettol.get()+"\n")
            self.txtNota.insert(
                END, 'Sampo Dettol\t\t\t\t\t'+sampoDettol.get()+"\n")

            self.txtNota.insert(END, '\nTax PPN:\t\t\t\t'+tax.get()+"\n")
            self.txtNota.insert(
                END, '\nSub Total:\t\t\t\t'+str(subTotal.get())+"\n")
            self.txtNota.insert(
                END, '\nBiaya Total:\t\t\t\t'+str(biayaTotal.get()))

        # =========================================================================================================
        # frontend kotak kiri

        self.lblCusId = Label(kotak3, font=(
            'arial', 12, 'bold'), text="Customer Ref:", padx=2, fg="Cornsilk", bg="cadet blue")
        self.lblCusId.grid(row=0, column=0, sticky=W)
        self.txtCusId = Entry(kotak3, font=('arial', 12),
                              textvariable=customerRef, width=20)
        self.txtCusId.grid(row=0, column=1, pady=14, padx=20)

        self.lblnama = Label(kotak3, font=(
            'arial', 12, 'bold'), text="Nama Customer:", padx=2, fg="Cornsilk", bg="cadet blue")
        self.lblnama.grid(row=1, column=0, sticky=W)
        self.txtnama = Entry(kotak3, font=('arial', 12),
                             textvariable=nama, width=20)
        self.txtnama.grid(row=1, column=1, pady=14, padx=20)

        self.lblAlamat = Label(kotak3, font=(
            'arial', 12, 'bold'), text="Alamat:", padx=2, fg="Cornsilk", bg="cadet blue")
        self.lblAlamat.grid(row=2, column=0, sticky=W)
        self.txtAlamat = Entry(kotak3, font=(
            'arial', 12), textvariable=alamat, width=20)
        self.txtAlamat.grid(row=2, column=1, pady=14, padx=20)

        self.lblNoHp = Label(kotak3, font=(
            'arial', 12, 'bold'), text="No HP:", padx=2, fg="Cornsilk", bg="cadet blue")
        self.lblNoHp.grid(row=3, column=0, sticky=W)
        self.txtNoHp = Entry(kotak3, font=('arial', 12),
                             textvariable=no_hp, width=20)
        self.txtNoHp.grid(row=3, column=1, pady=14, padx=20)

        self.lblTglEmail = Label(kotak3, font=(
            'arial', 12, 'bold'), text="Email:", padx=2, fg="Cornsilk", bg="cadet blue")
        self.lblTglEmail.grid(row=4, column=0, sticky=W)
        self.txtTglEmail = Entry(kotak3, font=(
            'arial', 12), textvariable=email, width=20)
        self.txtTglEmail.grid(row=4, column=1, pady=14, padx=20)

        self.lblTglBeli = Label(kotak3, font=(
            'arial', 12, 'bold'), text="Tanggal Beli:", padx=2, fg="Cornsilk", bg="cadet blue")
        self.lblTglBeli.grid(row=5, column=0, sticky=W)
        self.txtTglBeli = Entry(kotak3, font=(
            'arial', 12), textvariable=date1, width=20)
        self.txtTglBeli.grid(row=5, column=1, pady=14, padx=20)

        self.lblReseller = Label(kotak3, font=(
            'arial', 12, 'bold'), text="Reseller:", padx=2, pady=2, fg="Cornsilk", bg='cadet Blue')
        self.lblReseller.grid(row=6, column=0, sticky=W)
        self.cboReseller = ttk.Combobox(
            kotak3, textvariable=reseller, state='readonly', font=('arial', 12), width=18)
        self.cboReseller['value'] = ('', 'Iya', 'Tidak', 'Pending')
        self.cboReseller.current(0)
        self.cboReseller.grid(row=6, column=1, pady=14, padx=20)

        self.lblProduk = Label(kotak3, font=(
            'arial', 12, 'bold'), text="Produk:", padx=2, pady=2, fg="Cornsilk", bg='cadet Blue')
        self.lblProduk.grid(row=7, column=0, sticky=W)
        self.cboProduk = ttk.Combobox(
            kotak3, textvariable=produk, state='readonly', font=('arial', 12), width=18)
        self.cboProduk['value'] = ('', 'Hutan', 'Randu', 'Kelengkeng', 'Hitam')
        self.cboProduk.current(0)
        self.cboProduk.grid(row=7, column=1, pady=14, padx=20)

        self.lblUkuran = Label(kotak3, font=(
            'arial', 12, 'bold'), text="Ukuran:", padx=2, pady=2, fg="Cornsilk", bg='cadet Blue')
        self.lblUkuran.grid(row=8, column=0, sticky=W)
        self.cboUkuran = ttk.Combobox(
            kotak3, textvariable=ukuran, state='readonly', font=('arial', 12), width=18)
        self.cboUkuran['value'] = ('', '100ml', '250ml', '500ml', '1000ml')
        self.cboUkuran.current(0)
        self.cboUkuran.grid(row=8, column=1, pady=14, padx=20)

        # =========================================================================================================
        # frontend kotak tengah

        self.handSanitizer = Checkbutton(kotak4, text="Hand Sanitizer ", variable=var1, onvalue=1, offvalue=0, font=(
            'arial', 12, 'bold'), bg="powder blue", command=chkhandsanitizer).grid(row=0, sticky=W)
        self.txthandSanitizer = Entry(kotak4, font=(
            'arial', 12, 'bold'), textvariable=handSanitizer, bd=8, width=20, justify='left', state=DISABLED)
        self.txthandSanitizer.grid(row=0, column=1)

        self.masker = Checkbutton(kotak4, text="Masker ", variable=var2, onvalue=1, offvalue=0, font=(
            'arial', 12, 'bold'), bg="powder blue", command=chkmasker).grid(row=1, sticky=W)
        self.txtmasker = Entry(kotak4, font=(
            'arial', 12, 'bold'), textvariable=masker, bd=8, width=20, justify='left', state=DISABLED)
        self.txtmasker.grid(row=1, column=1)

        self.kalungmasker = Checkbutton(kotak4, text="Kalung Masker ", variable=var3, onvalue=1, offvalue=0, font=(
            'arial', 12, 'bold'), bg="powder blue", command=chkkalungmasker).grid(row=2, sticky=W)
        self.txtkalungmasker = Entry(kotak4, font=(
            'arial', 12, 'bold'), textvariable=kalungmasker, bd=8, width=20, justify='left', state=DISABLED)
        self.txtkalungmasker.grid(row=2, column=1)

        self.sanitizeRoom = Checkbutton(kotak4, text="Sanitize Room ", variable=var4, onvalue=1, offvalue=0, font=(
            'arial', 12, 'bold'), bg="powder blue", command=chksanitizeRoom).grid(row=3, sticky=W)
        self.txtsanitizeRoom = Entry(kotak4, font=(
            'arial', 12, 'bold'), textvariable=sanitizeRoom, bd=8, width=20, justify='left', state=DISABLED)
        self.txtsanitizeRoom.grid(row=3, column=1)

        self.imbooster = Checkbutton(kotak4, text="Imbooster ", variable=var5, onvalue=1, offvalue=0, font=(
            'arial', 12, 'bold'), bg="powder blue", command=chkimbooster).grid(row=4, sticky=W)
        self.txtimbooster = Entry(kotak4, font=(
            'arial', 12, 'bold'), textvariable=imbooster, bd=8, width=20, justify='left', state=DISABLED)
        self.txtimbooster.grid(row=4, column=1)

        self.sabunDettol = Checkbutton(kotak4, text="Sabun Dettol ", variable=var6, onvalue=1, offvalue=0, font=(
            'arial', 12, 'bold'), bg="powder blue", command=chksabunDettol).grid(row=5, sticky=W)
        self.txtsabunDettol = Entry(kotak4, font=(
            'arial', 12, 'bold'), textvariable=sabunDettol, bd=8, width=20, justify='left', state=DISABLED)
        self.txtsabunDettol.grid(row=5, column=1)

        self.sampoDettol = Checkbutton(kotak4, text="Sampo Dettol ", variable=var7, onvalue=1, offvalue=0, font=(
            'arial', 12, 'bold'), bg="powder blue", command=chksampoDettol).grid(row=6, sticky=W)
        self.txtsampoDettol = Entry(kotak4, font=(
            'arial', 12, 'bold'), textvariable=sampoDettol, bd=8, width=20, justify='left', state=DISABLED)
        self.txtsampoDettol.grid(row=6, column=1)

        self.lbltotal = Label(kotak4, text="Tax dan Biaya Total", font=('Arial', 15), pady=10, padx=60,
                              bd=4, bg='cadet blue', fg='Cornsilk').grid(row=7, column=0, columnspan=2)

        self.lblTax = Label(kotak4, font=(
            'arial', 12, 'bold'), text="Tax PPN:", padx=2, bg="powder blue")
        self.lblTax.grid(row=8, column=0, sticky=W)
        self.txtTax = Entry(kotak4, font=('arial', 12),
                            textvariable=tax, width=20)
        self.txtTax.grid(row=8, column=1, pady=12, padx=20)

        self.lblsubTotal = Label(kotak4, font=(
            'arial', 12, 'bold'), text="Sub Total:", padx=2, bg="powder blue")
        self.lblsubTotal.grid(row=9, column=0, sticky=W)
        self.txtsubTotal = Entry(kotak4, font=('arial', 12),
                                 textvariable=subTotal, width=20)
        self.txtsubTotal.grid(row=9, column=1, pady=12, padx=20)

        self.lblbiayaTotal = Label(kotak4, font=(
            'arial', 12, 'bold'), text="Biaya Total:", padx=2, bg="powder blue")
        self.lblbiayaTotal.grid(row=10, column=0, sticky=W)
        self.txtbiayaTotal = Entry(kotak4, font=('arial', 12),
                                   textvariable=biayaTotal, width=20)
        self.txtbiayaTotal.grid(row=10, column=1, pady=12, padx=20)

        # ========================================================================================================

        # text nota
        self.txtNota = Text(kotak6, height=19, width=43,
                            bd=10, font=('arial', 9))
        self.txtNota.grid(row=0, column=0)

        # =========================================================================================================

        # button kasir

        # frontend button kasir
        self.btnTotal = Button(kotak7, padx=14, pady=7, bd=5, fg='black', font=('arial', 16), width=5, height=2, bg="powder blue", text="Total", command=costItem).grid(
            row=0, column=0)
        self.btnReset = Button(kotak7, padx=14, pady=7, bd=5, fg='black', font=('arial', 16), width=5, height=2, bg="powder blue", text="Reset", command=reset).grid(
            row=0, column=1)
        self.btnExit = Button(kotak7, padx=14, pady=7, bd=5, fg='black', font=('arial', 16), width=5, height=2, bg="powder blue", text="Exit", command=exit).grid(
            row=0, column=2)


if __name__ == '__main__':
    root = Tk()
    application = Customer(root)
    root.mainloop()
