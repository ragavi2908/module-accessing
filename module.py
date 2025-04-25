import movies
def main():
    language=int(input("Enter your number:"))
    if language==1:
        movies.tamil()
    elif language==2:
        movies.korean()
    elif language==3:
        movies.malayalam()
    else:
        print("sorry unavailable")
main()
