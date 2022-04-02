import wx
import requests


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.search_result = ''
        self.movie_name_input_text = ''
        self.poster_file_name = ''

        self.search_field = wx.SearchCtrl(
            self, style=wx.TE_PROCESS_ENTER, size=(-1, 25))
        self.search_field.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_search)
        self.search_field.Bind(wx.EVT_TEXT_ENTER, self.on_search)

        self.movie_description = wx.TextCtrl(self, pos=(150, 0), size=(-1, 200), style=wx.TE_MULTILINE | wx.TE_READONLY)

    def on_search(self, event):
        self.movie_name_input_text = event.GetString()
        self.request_fun()
        self.get_extract()

    def request_fun(self):
        shifting_file = len('File:')
        adding_jpg = len('.jpg')

        search_url = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles='

        start_url = f'{search_url}{self.movie_name_input_text}'

        response = requests.get(start_url)

        print(response.content)

        # ******************************************************************

        image_url = f'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=images&titles={self.movie_name_input_text}'
        response = requests.get(image_url)
        content = str(response.content)
        print(content)

        index = content.find("File:Poster")

        if index != -1:
            jpg_index = content.find(".jpg")
        else:
            print("Poster not found")
            exit()

        print(index)
        print(jpg_index)

        print(content[index + shifting_file:jpg_index + adding_jpg])

        self.poster_file_name = content[index + shifting_file:jpg_index + adding_jpg]
        print(self.poster_file_name)

        # кеширане
        # ако в тази папка съществува този файл, го взима от там
        # отваряне на файл
        # ако не -> продължаваме надолу с request

        image = requests.get(f'{search_url}{self.poster_file_name}')
        print(f'{search_url}{self.poster_file_name}')

        new_url = f'https://en.wikipedia.org/w/api.php?action=query&list=allimages&format=json&aifrom={self.poster_file_name}'
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

        file_handler = open(self.poster_file_name, 'wb')
        file_handler.write(image_response.content)
        file_handler.close()

        self.image_show()

    def get_extract(self):
        start_url = f'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={self.movie_name_input_text}'

        response = requests.get(start_url)
        content = str(response.content)

        index = content.find("extract")

        if index != -1:
            last_index = content.find('"', index + 11)
            extract = content[index + 10:last_index]

        self.movie_description.SetValue(extract)

    def search(self):
        self.request_fun()
        self.get_extract()
        self.movie_description.SetValue(self.get_extract(self.movie_title))

    def image_show(self):
        img = wx.Image(self.poster_file_name, wx.BITMAP_TYPE_ANY)
        imageCtrl = wx.StaticBitmap(self, wx.ID_ANY,
                                    wx.Bitmap(img), pos=(340, 0))
        imageCtrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()


class SearchFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Movie Info',
                         size=(1200, 800))
        panel = MainPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = SearchFrame()
    app.MainLoop()

# The Notebook