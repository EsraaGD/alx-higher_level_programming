#include "lists.h"

/**
 * check_cycle - checks if ssl has a cycle
 * @list: pointer to head of list
 * Return: 1 if true, 0 if false
 */

int check_cycle(listint_t *list)

{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
