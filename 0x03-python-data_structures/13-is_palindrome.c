#include "lists.h"

/**
 * is_palindrome - Determines whether a singly linked list is a palindrome.
 * @head: Pointer to pointer of the first node in the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (!head || !*head || !(*head)->next)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	if (fast)
		slow = slow->next;
	while (prev)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
