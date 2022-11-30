#include "lists.h"

/**
 * check_cycle - check if a singly linked list is cyclical
 * @list: the sigly linked list
 * Return: 0 if there is no cycle, if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list, *ptr2 = list;  /* for scanning */

	if (!list)			/* empty node case */
		return (0);
	if (!list->next)	/* single node null terminus case */
		return (0);
	if (list->next == list)	/* single self-referncing case */
		return (1);
	if (!list->next->next)	/* two node case */
		return (0);
	if (list->next->next == list) /* back reference */
		return (1);

	/* do step */
	do {
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;

		if (ptr1 == ptr2)
			return (1);
	} while (ptr1->next && ptr2->next && ptr2->next->next);

	return (0);
}


