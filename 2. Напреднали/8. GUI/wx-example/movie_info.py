import wx
import requests
import wx.grid as gridlib

def request_fun(movie_title):
    shifting_file = len('File:')
    adding_jpg = len('.jpg')

    search_url = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles='

    start_url = f'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={movie_title}'

    response = requests.get(start_url)

    print(response.content)

    image_url = f'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=images&titles={movie_title}'
    response = requests.get(image_url)
    content = str(response.content)
    print(content)

    index = content.find("File:Poster")

    if index != -1:
        jpg_index = content.find(".jpg")

    print(index)
    print(jpg_index)

    print(content[index + shifting_file:jpg_index + adding_jpg])

    poster_file_name = content[index + shifting_file:jpg_index + adding_jpg]
    print(poster_file_name)

    # кеширане
    # ако в тази папка съществува този файл, го взима от там
    # отваряне на файл
    # ако не -> продължаваме надолу с request

    image = requests.get(f'{search_url}{poster_file_name}')
    print(f'{search_url}{poster_file_name}')

    new_url = f'https://en.wikipedia.org/w/api.php?action=query&list=allimages&format=json&aifrom={poster_file_name}'
    print(new_url)
    new = requests.get(new_url)
    print(new.content)
    new_url_content = str(new.content)

    poster_url_index = new_url_content.find("url")
    if poster_url_index != -1:
        jpg_index = new_url_content.find(".jpg", poster_url_index)

    poster_url = new_url_content[poster_url_index + 6:jpg_index + adding_jpg]
    print(poster_url)

    image_response = requests.get(poster_url)

    file_hendller = open(poster_file_name, 'wb')
    file_hendller.write(image_response.content)
    file_hendller.close()

    return poster_file_name

def get_extract(movie_title):
    start_url = f'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={movie_title}'

    response = requests.get(start_url)
    content = str(response.content)

    index = content.find("extract")

    if index != -1:
        last_index = content.find('"', index + 11)
        extract = content[index+10:last_index]

    return extract


def search(text):
    movie_title = text_ctrl.GetValue()
    request_fun(movie_title)
    get_extract(movie_title)
    movie_text = movie_descpription.SetValue(get_extract(movie_title))


app = wx.App()
frame = wx.Frame(None, -1, 'IMDB movie search')
panel = wx.Panel(frame)
text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
my_btn = wx.Button(panel, label='Press Me', pos=(5, 55))

movie_descpription = wx.TextCtrl(panel, pos=(150, 5), size=(-1, 200), style = wx.TE_MULTILINE|wx.TE_READONLY)
my_btn.Bind(wx.EVT_BUTTON, search)

# image_col = wx.TextCtrl(panel, pos=(250, 5))

img = wx.Image('Posternotebook.jpg', wx.BITMAP_TYPE_ANY)
imageCtrl = wx.StaticBitmap(panel, wx.ID_ANY,
                                         wx.BitmapFromImage(img), pos=(355, 5))
imageCtrl.SetBitmap(wx.BitmapFromImage(img))
panel.Refresh()
frame.Show()
app.MainLoop()

# The Notebook