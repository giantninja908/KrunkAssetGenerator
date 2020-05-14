from urllib.request import Request, urlopen

for i in range(0,100):
    try:
        url ="https://assets.krunker.io/textures/sprays/"+str(i)+".png"
        req = Request(url)
        req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
        content = urlopen(req).read()

        filename = "sprays/"+str(i)+".png"
        file_ = open(filename, 'wb')
        file_.write(content)
        file_.close()
    except:
        print("bruh")
