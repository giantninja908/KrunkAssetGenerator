# Krunker Assets Generation Scripts
## made by GNU/Ninja#7650

**Prequisites**: Python3 must be installed on the users computer
**File Structure**: all folders provided are of the correct name, they are empty but once the script is run, they will fill up with the latest assets

**How it works**: using a request python module, just brute forces through every assets by counting upwards

Too lazy? Just want to see it get done? (code example for Linux, other systems may vary)
```
git clone https://github.com/giantninja908/KrunkAssetGenerator.git
cd *insert repo here*
python3 generator.py &
python3 generatorBody.py &
python3 generatorHats.py &
python3 generatorIcon.py &
python3 generatorMelee.py &
python3 generatorSprays.py &
```
this will start a coroutine of every single generator, alternatively you can use the following command to execute them sequentially:
```
git clone *insert repo here*
cd *insert repo here*
python3 generator.py
python3 generatorBody.py
python3 generatorHats.py
python3 generatorIcon.py
python3 generatorMelee.py
python3 generatorSprays.py
```


For any additional help, please consult GNU/Ninja#7650 on discord
