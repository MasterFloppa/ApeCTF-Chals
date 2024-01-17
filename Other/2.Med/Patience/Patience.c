#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_INPUT_LENGTH 1000

// Variable to store input
char input[MAX_INPUT_LENGTH];

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

    sleep(20);
    if (strlen(input) > 0)
        return 0;
    else
    {
        printf("\nShell\n");
        // system("/bin/sh");
    }

    return 0;
}
