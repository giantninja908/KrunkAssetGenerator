# Krunker Assets Generation Scripts
## made by GNU/Ninja#7650

**Prequisites**: Python3 must be installed on the users computer
**File Structure**: all folders provided are of the correct name, they are empty but once the script is run, they will fill up with the latest assets

**How it works**: using a request python module, just brute forces through every assets by counting upwards

Too lazy? Just want to see it get done? (code example for Linux, other systems may vary)
```
git clone https://github.com/giantninja908/KrunkAssetGenerator.git
cd KrunkAssetGenerator
mkdir 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 body hats icons melee sprays
./everything.sh
```
alternativly, instead of everything.sh, you can manually run each of the scripts
```
python3 generator.py &
python3 generatorBody.py &
python3 generatorHats.py &
python3 generatorIcon.py &
python3 generatorMelee.py &
python3 generatorSprays.py &
python3 generatorWaist.py &
```
this will start a coroutine of every single generator, alternatively you can use the following command to execute them sequentially:
```
git clone https://github.com/giantninja908/KrunkAssetGenerator.git
cd KrunkAssetGenerator
mkdir 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 body hats icons melee sprays waist
python3 generator.py
python3 generatorBody.py
python3 generatorHats.py
python3 generatorIcon.py
python3 generatorMelee.py
python3 generatorSprays.py
python3 generatorWaist.py
```


For any additional help, please consult Giant#7650 on discord, by reaching out at the server https://discord.gg/an2AytE
