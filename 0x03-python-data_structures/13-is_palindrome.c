#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to a pointer of first node of listint_t list
 * Return: 0 if linked list is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *array, count, i;

	/* Assign pointer to first node of linked list to current */
	current = *head;

	/* If list is empty or has one node */
	if (current == NULL || current->next == NULL)
		return (1);

	count = 0;
	/* Calculate length of linked list */
	while (current != NULL)
	{
		count++;
		current = current->next;
	}

	/* Alloc memory for array */
	array = malloc(sizeof(int) * count);
	if (array == NULL)
		return (-1);

	/* Reset current pointer to the head of the list */
	current = *head;

	/* Store linked list elements in array */
	for (i = 0; i < count; i++)
	{
		array[i] = current->n;
		if (current->next != NULL)
			current = current->next;
	}

	/* Check if is palindrome */
	for (i = 0; i < count / 2; i++)
	{
		if (array[i] != array[count - i - 1])
		{
			free(array);
			return (0);
		}
	}

	free(array);
	return (1);
}
