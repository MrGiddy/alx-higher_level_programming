#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: Pointer to a pointer to the first node of a listint_t linked list
 * @number: The number to insert
 * Return: A pointer to the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *temp;

	new_node = malloc(sizeof(listint_t)); /* Create new_node */
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	if (current == NULL) /* if list is empty */
	{
		*head = new_node;
		return (new_node);
	}

	if (new_node->n < current->n) /* If number < first element */
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	temp = *head;
	current = current->next;
	while (current->next != NULL && current->n < new_node->n)
	{
		current = current->next;
		temp = temp->next;
	}

	if (current->next == NULL)
	{
		current->next = new_node;
	}
	else
	{
		temp->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
