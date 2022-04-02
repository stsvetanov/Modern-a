import requests

main_url='http://www.regalia6.com/books/eU4ebnik-matematika-12klas_PP_Veroyatnosti_21/files/mobile/'
# main_url='http://www.regalia6.com/books/eU4ebnik-matematika-12klas_PP_Prakt-mat_21/files/mobile/'
# main_url='http://sales.anubis-bulvest.com/epub/12_klas/b12MatPP3Mod/'

urls=[main_url+str(i)+'.jpg' for i in range(1,101)]
fnames=[str(i)+'.jpg' for i  in range(1,101)]
for i in range(100):
    r = requests.get(urls[i], allow_redirects=True)
    open(fnames[i], 'wb').write(r.content)
    # close(fnames[i])