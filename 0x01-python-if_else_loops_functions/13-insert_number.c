#include "lists.h"

listint_t *new_nodeint(const int n);
listint_t *insertNode(listint_t **head, listint_t *new, int order);
listint_t *doSingleNode(listint_t **head, listint_t *new, int order);

/**
 * insert_node - insert a number node into a sorted singly linked list
 * @head: address of the pointer to the head node
 * @number: the integer to be insereted
 * Return: pointer to the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new; /* new node to be inserted */
	int order = 0;  /* sort order  0 - ascending, 1 - descending */

	/* null check */
	if (head == NULL)
		return (NULL);

	/* check sort order: */
	if (*head) /* not empty list */
	{
		if ((*head)->next)  /* at least 2 nodes */
			if (((*head)->next)->n < (*head)->n)
				order = 1; /* descending */
	}

	/* make a new node */
	new = new_nodeint(number);

	/*insert the new node */
	insertNode(head, new, order);

	return (new);
}

/**
 * new_nodeint - creates a new node
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *new_nodeint(const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	return (new);
}

/**
 * insertNode - nsert the new node
 * @head: pointer to the pointer to the head node
 * @new: pointer to the new node to be inserted
 * @order: 0 if ascending, 1 if descending
 * Return: address of the new element or NULL if it fails
 */
listint_t *insertNode(listint_t **head, listint_t *new, int order)
{
	listint_t *nptr, *b4, *aft;

	if (*head == NULL) /* empty list */
	{
		*head = new;  /* set head to new node */
		return (new);
	}

	if ((*head)->next == NULL)  /* only one node */
	{
		/* insert in case of single node */
		doSingleNode(head, new, order);
	}
	else
	{
		/* locate the insertion point */
		nptr = *head;
		b4 = *head;
		while (nptr != NULL)
		{
			if (new->n < nptr->n)
			{
				aft = nptr;
				break;
			}
			b4 = nptr;
			nptr = nptr->next;
		}
		if (nptr == NULL)
			aft = NULL;
		new->next = aft;
		if (b4 == *head)
			*head = new;
		else
			b4->next = new;
	}
	return (new);
}

/**
 * doSingleNode - insert the new node in case of single node
 * @head: pointer to the pointer to the head node
 * @new: pointer to the new node to be inserted
 * @order: 0 if ascending, 1 if descending
 * Return: address of the new element or NULL if it fails
 */
listint_t *doSingleNode(listint_t **head, listint_t *new, int order)
{
	if (((order == 0) && (new->n <= (*head)->n))
		|| ((order == 1) && (new->n <= (*head)->n)))
	{
		/* insert at beginning */
		new->next = *head;
		*head = new;
	}
	else
	{
		/* insert at the end */
		new->next = NULL;
		(*head)->next = new;

	}
	return (new);
}
