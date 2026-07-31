# make_config(**settings) jo saari settings ek dict ke roop mein print kare.

def make_config(**settings):
    for key, value in settings.items():
        print(f" {key} : {value}")

make_config(  theam = 'dark',
              color = 'pink', 
              furniture = 'sofa')        