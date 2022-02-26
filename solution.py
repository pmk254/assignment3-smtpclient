from socket import *
import sys

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    #mailserver = ("")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfrom = 'MAIL FROM:<pmk254@nyu.edu>\r\n'
    clientSocket.send(mailfrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    # Fill in end
    #print(recv2)
    #if recv2[:3] != '250':
    #    print('250 reply not received from server.')

    # Send RCPT TO command and handle server response.
    # Fill in start
    rccptto = 'RCPT TO:<pmk254@nyu.edu>\r\n'
    clientSocket.send(rccptto.encode())
    recv3 = clientSocket.recv(1024).decode()
    # Fill in end
    #print(recv3)
    #if recv3[:3] != '250':
    #    print('250 reply not received from server.')

    # Send DATA command and handle server response.
    # Fill in start
    data = '\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    # Fill in end
    #print(recv4)
    #if recv4[:3] != '354':
    #    print('354 reply not received from server.')

    # Send message data.
    # Fill in start
    clientSocket.send('Subject:Hello\r\n'.encode())
    clientSocket.send('Hello\r\n'.encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    # Fill in end
    #print(recv5)
    #if recv5[:3] != '250':
    #    print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    # Fill in start
    Quit = 'QUIT'
    clientSocket.send(Quit.encode())
    recv6 = clientSocket.recv(1024).decode()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')