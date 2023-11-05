#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return 1;

	listint_t *slow = *head, *fast = *head, *first_half = *head, *dup = NULL;

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && first_half)
	{
		if (first_half->n == dup->n)
		{
			dup = dup->next;
			first_half = first_half->next;
		}
		else
			return 0;
	}

	if (!dup)
		return (1);
	return (0);
}

void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next_node;

	while (current)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}

	*head =  prev;
}
