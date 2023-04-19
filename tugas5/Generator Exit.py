# Generator Exit
zoo = ['lion', 'cat', 'tiger']
def animals (xlist) :
    for animal in xlist :
        try :
            yield animal
        except GeneratorExit as e :
            print (type(e))
            print ('Generator exit')
            return
        
        x = animals(zoo)
        for a in x :
            print(next(x))
            x.close()