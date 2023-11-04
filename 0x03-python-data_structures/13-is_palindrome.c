#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;  // An empty list or a single-element list is a palindrome

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *first_half = *head;
    listint_t *second_half;  // Declare the variable here

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

     listint_t *reverse_linked_list(listint_t *head);

    // Compare the first half and the reversed second half
    while (second_half)
    {
        if (first_half->n != second_half->n)
            return 0;  // Not a palindrome

        first_half = first_half->next;
        second_half = second_half->next;
    }

    return 1;  // It is a palindrome
}

listint_t *reverse_linked_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next_node;

    while (current != NULL)
    {
        next_node = current->next;
        current->next = prev;
        prev = current;
        current = next_node;
    }

    return prev;
}
