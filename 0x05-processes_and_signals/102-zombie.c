#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop function
 *
 * Return: Always 0 (Success)
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
    pid_t zombie_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        zombie_pid = fork();
        if (zombie_pid == -1)
        {
            perror("fork");
            exit(1);
        }
        if (zombie_pid == 0)
        {
            exit(0);
        }
        else
        {
            printf("Zombie process created, PID: %d\n", zombie_pid);
        }
    }
    infinite_while();
    return (0);
}
