from urllib.request import Request, urlopen

for i in range(1,100):
    for v in range(1,20):
        try:
            if v is 1:
                print("requesting obj...")
                url = 'https://assets.krunker.io/models/hats/hat_'+str(i)+'.obj'
                req = Request(url)
                req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
                content = urlopen(req).read()

                    # Write data to file
                filename = "hats/"+str(i)+".obj"
                file_ = open(filename, 'wb')
                file_.write(content)
                file_.close()

                print("requesting png...")
                url = 'https://assets.krunker.io/textures/hats/hat_'+str(i)+'.png'
                req = Request(url)
                req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
                content = urlopen(req).read()

                    # Write data to file
                filename = "hats/"+str(i)+".png"
                file_ = open(filename, 'wb')
                file_.write(content)
                file_.close()

                print("requesting prev...")
                url = 'https://assets.krunker.io/textures/previews/cosmetics/1_'+str(i)+'.png'
                req = Request(url)
                req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
                content = urlopen(req).read()

                    # Write data to file
                filename = "hats/"+str(i)+"_PREV.png"
                file_ = open(filename, 'wb')
                file_.write(content)
                file_.close()
            else:
                
                print("requesting png of others...")
                url = 'https://assets.krunker.io/textures/hats/hat_'+str(i)+'_'+str(v-1)+'.png'
                req = Request(url)
                req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
                content = urlopen(req).read()

                    # Write data to file
                filename = "hats/"+str(i)+'_'+str(v-1)+".png"
                file_ = open(filename, 'wb')
                file_.write(content)
                file_.close()
                print("requesting prev of others...")
                url = 'https://assets.krunker.io/textures/previews/cosmetics/1_'+str(i)+'_'+str(v-1)+'.png'
                req = Request(url)
                req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36')
                content = urlopen(req).read()

                    # Write data to file
                filename = "hats/"+str(i)+'_'+str(v-1)+"_PREV.png"
                file_ = open(filename, 'wb')
                file_.write(content)
                file_.close()

        except Exception as e:
            print(e)
            print(str(i)+'_'+str(v-1)+" is not a valid hat OBJ ID")
            break
            
