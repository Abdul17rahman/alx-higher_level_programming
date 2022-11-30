#include "lists.h"
#include <stdlib.h>

/**
*check_cycle - checks if the list has a cycle or not
*@list: singly linked list pointer
*Return: returns 1 if it has a cycle or 0 if not
*/

int check_cycle(listint_t *list)
{
	const listint_t *current;
	current = list;

	while (current != NULL)
	{
		if (current->next == list)
		{
			return (1);
		}
		current = current->next;
	}
	return (0);
}
