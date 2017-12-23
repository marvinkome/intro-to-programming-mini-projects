import webbrowser

def open_page(movies):

    html = '''<html>
                <head>
                    <title>Movie Site</title>
                </head>
            <body>'''


    for movie in movies:
        title = movie.title
        image = movie.poster_image
        link = movie.trailer_link
        html = html + division(link, image, title)

    html = html + '</body></html>'
    site = open('index.html','w')
    file = site.write(html)
    site.close()
    webbrowser.open('index.html')

    return html

def division(link,image,title):
    markup = '''
                <div>
                    <a href="{link}">
                        <img src="{image}"></img>
                    </a>
                    <p>{title}</p>
                </div>'''.format(link=link,image=image,title=title)

    return markup