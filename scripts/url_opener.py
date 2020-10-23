import webbrowser

# this script opens a list of urls in firefox browser 
webbrowser.register(
    "firefox",
    None,
    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"),
)

urls = [
    "https://google.com",
    "https://outlook.com",
    "https://drive.com",
]

first = True 
for url in urls:
    if first:
        webbrowser.get("firefox").open(url)
        first = False
    else:
        webbrowser.get("firefox").open_new_tab(url)
