from urllib.request import Request, urlopen

for v in range(1,17):
    for i in range(1,140):
        try:
            print("requesting png... of "+str(v)+' '+str(i))
            url = 'https://assets.krunker.io/textures/weapons/skins/weapon_'+str(v)+'_'+str(i)+'.png'
            req = Request(url)
            req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
            content = urlopen(req).read()

            # Write data to file
            print("requesting preview... of "+str(v)+' '+str(i))
            filename = str(v)+"/"+str(i)+".png"
            file_ = open(filename, 'wb')
            file_.write(content)
            file_.close()

            url = 'https://assets.krunker.io/textures/previews/weapons/weapon_'+str(v)+'_'+str(i)+'.png'
            req = Request(url)
            req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
            content = urlopen(req).read()

            # Write data to file
            filename = str(v)+"/"+str(i)+"_PREV.png"
            file_ = open(filename, 'wb')
            file_.write(content)
            file_.close()
        except Exception as e:
            print(e)
            print('https://assets.krunker.io/textures/weapons/skins/weapon_'+str(v)+'_'+str(i)+'.png is not valid ('+str(v)+' '+str(i)+')')
            #break
            
