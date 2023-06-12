#include "lists.h"

/**
 * pal - Recursive helper function to determine if a list is a palindrome.
 * @start: Start position of the list.
 * @end: End position of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int pal(listint_t **start, listint_t *end)
{
    if (end == NULL)
        return (1);

    if (pal(start, end->next) == 1 && (*start)->n == end->n)
    {
        *start = (*start)->next;
        return (1);
    }

    return (0);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: List to check.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL || (*head)->next == NULL)
        return (1);

    return pal(head, *head);
}
