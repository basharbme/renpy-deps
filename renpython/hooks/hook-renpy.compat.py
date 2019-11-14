import os.path


def hook(mod):

    import _renpy

    base = os.path.dirname(_renpy.__file__)
    moddir = mod.__name__.replace(".", "/")    
    modpath = os.path.join(base, moddir)
    mod.__path__.append(modpath)
    
    return mod
