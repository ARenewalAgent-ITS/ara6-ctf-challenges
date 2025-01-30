#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 12345

int main()
{
    int sockfd;
    struct sockaddr_in server_addr;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0)
    {
        perror("socket");
        exit(1);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    printf("addr of server_addr: %p\n", &server_addr);
    printf("content of server_addr: %x\n", server_addr.sin_addr.s_addr);
    printf("content of server_addr: %x\n", server_addr.sin_port);
    printf("content of server_addr: %x\n", server_addr.sin_family);

    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        perror("connect");
        exit(1);
    }

    char *msg = "ARA6{just_trying_to_make_ur_life__a_little__harder_heheh_AYO_DAFTAR_SCH_NPC_CTF_2025}";
    if (sendto(sockfd, msg, strlen(msg), 0, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        perror("sendto");
        exit(1);
    }

    close(sockfd);

    return 0;
}