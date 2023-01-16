print("BahaaXdBahaaXdBahaaXd\nBahaaXdBahaaXdBahaaXd\nBahaaXdBahaaXdBahaaXd\nBahaaXdBahaaXdBahaaXd\nBahaaXdBahaaXdBahaaXd\nBahaaXdBahaaXdBahaaXd\nBahaaXdBahaaXdBahaaXd\nBahaaXdBahaaXdBahaaXd\nBahaaXdBahaaXdBahaaXd\n")
print("=================\n   YT: BahaaXD   \n=================")


from pytube import YouTube
url_input = input("Pleas enter ur URL: ")
all_streams = YouTube(url_input).streams.all()
v =-1
for i in all_streams:
    v = v+1
    print(str(v)+ " : "+str(i))
stm_input = int(input("Please Choose The Suitable Stream :"))
print("Pleas Choose Directly To Save : ")
place = input(" .")
choice = all_streams[stm_input].download(place)
print("Download Complete ......")
