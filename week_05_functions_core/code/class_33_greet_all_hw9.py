# greet_all(*names) jo har naam ko "Hello NAME" print kare (loop se).
  
def greet_all(*name):
    for n in name:
        print(f" Hello {n}")

greet_all('Akash', 'Prajwali', 'Zade')
        