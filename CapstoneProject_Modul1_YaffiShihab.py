
stocksObat = [
    {
        'code':'Ci23',
        'nama_obat':'Citirizine',
        'stocks':'30',
        'satuan':'Strip',
        'ED':'Dec 2023',
        'pemakaian':'Obat Dalam'
    },
    {
        'code':'Ra23', 
        'nama_obat':'Ranitidine',
        'stocks':'25',
        'satuan':'Box',
        'ED':'August 2023',
        'pemakaian':'Obat Dalam'
    },
    {
        'code':'Ti23',
        'nama_obat':'Timol',
        'stocks':'20',
        'satuan':'Supp',
        'ED':'Sep 2023',
        'pemakaian':'Obat Luar'
    }
]

cart = []

def menampilkanDaftarObat() :
    print('\nDaftar Obat\n')
    print('Index\t| Code Barang \t| Nama Obat \t| Stocks\t| Satuan\t| Expired Date\t| Pemakaian')
    for i in range(len(stocksObat)) :
        print('{}\t| {}\t\t| {}  \t| {}\t\t| {}\t\t| {}\t| {}'.format(i,
                                                                stocksObat[i]['code'],
                                                                stocksObat[i]['nama_obat'],
                                                                stocksObat[i]['stocks'],
                                                                stocksObat[i]['satuan'],
                                                                stocksObat[i]['ED'],
                                                                stocksObat[i]['pemakaian']))


def menambahObat() :
    codeBarang = input ('Masukkan Code Barang : ')
    namaObat = input('Masukkan Nama Obat : ')
    stockObat = int(input('Masukkan Stock Obat : '))
    satuan = input('Masukkan Nama Satuan : ')
    expDate = input('Masukkan Expired Date : ')
    pemakaian = input('Masukkan Jenis Pemakaian : ')
    stocksObat.append({
            'code': codeBarang,
            'nama_obat': namaObat,
            'stocks': stockObat,
            'satuan': satuan,
            'ED': expDate,
            'pemakaian': pemakaian 
    })
    menampilkanDaftarObat()

def menghapusObat() :
    menampilkanDaftarObat()
    indexObat = int(input('Masukkan index obat yang ingin dihapus : '))
    del stocksObat[indexObat]
    menampilkanDaftarObat()

def updatejumlahStock() :
    menampilkanDaftarObat()
    code = input('Masukkan Code Barang: ')
    jmlStockBaru = input('Input Jumlah Stock Baru: ')

    for stock in stocksObat:
        print(stock)
        if (stock['code']==code):
            stock['stocks']=jmlStockBaru
            break
    menampilkanDaftarObat()

while True :
    pilihanMenu = input('''
        Selamat Datang di Pasar Buah

        List Menu :
        1. Menampilkan Daftar Obat
        2. Menambah Stock Obat
        3. Menghapus Stock Obat
        4. Update Jumlah Stock Obat 
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDaftarObat()
    elif(pilihanMenu == '2') :
        menambahObat()
    elif(pilihanMenu == '3') :
        menghapusObat()
    elif(pilihanMenu == '4') :
        updatejumlahStock()
    elif(pilihanMenu == '5') :
        break
    
