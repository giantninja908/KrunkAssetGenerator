from urllib.request import Request, urlopen

for v in range(1,18):
    if v in [3,12,13,16,17]:
        break
    for i in range(1,500):
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

            print("attempting to fetch emmision")
            try:
                url = 'https://assets.krunker.io/textures/weapons/skins/weapon_'+str(v)+'_'+str(i)+'_e.png'
                req = Request(url)
                req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
                content = urlopen(req).read()

                # Write data to file
                filename = str(v)+"/"+str(i)+"_e.png"
                file_ = open(filename, 'wb')
                file_.write(content)
                file_.close()
                print("fetch successful")
            except Exception as e:
                print("fetch failed")
        except Exception as e:
            print(e)
            print('https://assets.krunker.io/textures/weapons/skins/weapon_'+str(v)+'_'+str(i)+'.png is not valid ('+str(v)+' '+str(i)+')')
            #break
            
