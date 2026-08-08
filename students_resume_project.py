###Students Resume #
class StudentsResume:
        def __init__(self, name, age, address, city, education, experience, job_roll):
            self.name = name
            self.age = age
            self.address = address
            self.city = city
            self.education = education
            self.experience = experience
            self.job_roll  = job_roll

        def display(self):
            print("****Students Resume******")
            print("Name:", self.name)
            print("Age:", self.age)
            print("Address:", self.address)
            print("City:", self.city)
            print("Educations:", self.education)
            print("Experinece:", self.experience)
            print("Job_Rol:", self.job_roll)


name = input("Enter You're Name: ")
age = int(input("Enter You're Age: "))
address = input("Enter You're Address: ")
city = input("Enter You're City: ")
education = input("Enter You're education: ")
experience = input("Enter You're Experinece: ")
job_roll = input("Enter You're Job Roll: ")

print("****************************************")

print("You're Resume is Ready")

print("****************************************")


student1 = StudentsResume(name, age, address, city, education, experience, job_roll)

#student2 = StudentsResume(name, age, address, city, education, experience, job_roll)

student1.display()




