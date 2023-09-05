#include "lists.h"

/**
 * insert_node - Adds a specified number to a singly-linked
 * list while maintaining sorting order.
 * @head: A reference to the head of the linked list.
 * @number: The number to be inserted.
 *
 * Return: If the operation fails - NULL.
 * Otherwise - a pointer to the newly inserted node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}
