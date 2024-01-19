#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_INPUT_LENGTH 1000
char input[MAX_INPUT_LENGTH];

void gib()
{
    // give shell
    system("/bin/sh");
}

void *waitForInput(void *arg)
{
    printf("Password: ");
    fflush(stdout);

    scanf("%s", input);

    if (strlen(input) > 0)
        exit(0);

    return NULL;
}

int main()
{
    char name[500];

    printf("Login: ");
    scanf("%s", name);
    if (strcmp(name, "admin") != 0)
        return 0;

    pthread_t inputThread;
    int threadResult = pthread_create(&inputThread, NULL, waitForInput, NULL);
    if (threadResult != 0)
        return 1;

    sleep(22);
    if (strlen(input) > 0)
        return 0;
    else
    {
        pthread_cancel(inputThread);
        printf("\n");
        gib();
    }

    pthread_join(inputThread, NULL);

    return 0;
}
