#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Determines whether a singly linked list contains a cycle.
 * @list: The singly linked list to examine.
 *
 * Return: 1 if a cycle is present, or 0 if no cycle is found.
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
