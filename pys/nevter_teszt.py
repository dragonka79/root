# 12.11.4. Nevter_teszt

import sajatmodul1
import sajatmodul2

# print( (sajatmodul2.sajatev - sajatmodul1.sajatev) ==
       # (sajatmodul2.ev - sajatmodul1.ev)  )

# print("Az én nevem", __name__)

if __name__ == "__main__":
    print ("File1 is being run directly")
else:
    print ("File1 is being imported")
