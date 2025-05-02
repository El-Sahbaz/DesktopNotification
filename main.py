from plyer import notification
import time

inputTitle = input("Title : ")
inputMessage = input("Message : ")

if __name__ == "__main__":
    notification.notify(
        title = f"{inputTitle}",
        message = f"{inputMessage}",
        #displaying time
        timeout = 2,
    )

    #waiting time
    time.sleep(7)



